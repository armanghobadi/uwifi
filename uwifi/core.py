import network
import time
import socket

class uwifi:
    def __init__(self):
        """
        Initialize the Wi-Fi manager with both Station (STA) and Access Point (AP) interfaces.
        """
        self.sta_if = network.WLAN(network.STA_IF)
        self.ap_if = network.WLAN(network.AP_IF)
        self.sta_if.active(True)  # Enable Station mode
        self.ap_if.active(False)  # Disable Access Point mode

    def connect(self, ssid, password, timeout=10):
        """
        Connect to a Wi-Fi network.
        
        :param ssid: The SSID of the network.
        :param password: The password of the network.
        :param timeout: The maximum time (in seconds) to attempt connection before giving up.
        :return: True if the connection is successful, False otherwise.
        """
        print(f"Attempting to connect to network: {ssid}")
        self.sta_if.connect(ssid, password)
        start_time = time.time()
        
        while not self.sta_if.isconnected():
            if time.time() - start_time > timeout:
                print("Connection failed.")
                return False
            time.sleep(1)
        
        print("Connected successfully!")
        print(f"IP address: {self.sta_if.ifconfig()[0]}")
        return True

    def disconnect(self):
        """
        Disconnect from the currently connected Wi-Fi network.
        """
        if self.sta_if.isconnected():
            self.sta_if.disconnect()
            print("Disconnected from the network.")

    def is_connected(self):
        """
        Check if the device is currently connected to a Wi-Fi network.
        
        :return: True if connected, False otherwise.
        """
        return self.sta_if.isconnected()

    def set_static_ip(self, ip, subnet, gateway, dns=None):
        """
        Set a static IP configuration for the Wi-Fi connection.
        
        :param ip: The static IP address.
        :param subnet: The subnet mask.
        :param gateway: The gateway address.
        :param dns: (Optional) DNS server address. Defaults to gateway if not provided.
        """
        dns = dns or gateway
        self.sta_if.ifconfig((ip, subnet, gateway, dns))
        print(f"Static IP address set to: {ip}")

    def get_ip_config(self):
        """
        Get the current IP configuration (IP, Subnet Mask, Gateway, DNS).
        
        :return: A tuple containing (IP, Subnet Mask, Gateway, DNS).
        """
        return self.sta_if.ifconfig()

    def ping(self, host="8.8.8.8", count=4):
        """
        Ping a server to check if the device has internet access.
        
        :param host: The host address to ping (default is Google's public DNS: 8.8.8.8).
        :param count: The number of ping attempts to make (default is 4).
        :return: True if any ping is successful, False otherwise.
        """
        print(f"Pinging {host}...")
        for _ in range(count):
            try:
                addr = socket.getaddrinfo(host, 1)[0][-1]
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.settimeout(1)
                s.connect(addr)
                s.close()
                print(f"Received response from {host}")
                return True
            except Exception:
                pass
        print(f"No response received from {host}.")
        return False

    def reconnect(self, ssid, password, timeout=10, retry_count=3):
        """
        Attempt to reconnect to a Wi-Fi network multiple times in case of failure.
        
        :param ssid: The SSID of the network.
        :param password: The password of the network.
        :param timeout: The maximum time (in seconds) to attempt connection before giving up.
        :param retry_count: The number of retry attempts before failing.
        :return: True if connected successfully after retries, False otherwise.
        """
        attempt = 0
        while attempt < retry_count:
            print(f"Retry {attempt + 1}/{retry_count}")
            if self.connect(ssid, password, timeout):
                return True
            attempt += 1
            print("Retrying...")
        print("Failed to connect after multiple attempts.")
        return False

    def list_available_networks(self):
        """
        Scan for available Wi-Fi networks and return their SSIDs.
        
        :return: A list of SSIDs of the available networks.
        """
        print("Scanning for available networks...")
        networks = self.sta_if.scan()
        ssids = [network[0].decode('utf-8') for network in networks]
        return ssids

    def create_access_point(self, ssid, password=None, authmode=4, channel=1, max_clients=4):
        """
        Set up the device as an Access Point (AP).
        
        :param ssid: The SSID of the Access Point.
        :param password: The password for the AP. If None, no password will be set.
        :param authmode: The authentication mode for the AP. Default is WPA2.
        :param channel: The channel for the AP. Default is 1.
        :param max_clients: Maximum number of clients allowed to connect. Default is 4.
        :return: None
        """
        self.ap_if.active(True)
        self.ap_if.config(essid=ssid, password=password, authmode=authmode, channel=channel, max_clients=max_clients)
        print(f"Access Point '{ssid}' created successfully.")
        
    def disable_access_point(self):
        """
        Disable the Access Point (AP) mode if enabled.
        """
        self.ap_if.active(False)
        print("Access Point mode disabled.")
        
    def check_wifi_status(self):
        """
        Check the current status of the Wi-Fi interface.
        
        :return: A string with the current status (Connected or Disconnected).
        """
        if self.is_connected():
            return f"Connected to {self.sta_if.config('essid')} with IP {self.sta_if.ifconfig()[0]}"
        else:
            return "Not connected to any network."



