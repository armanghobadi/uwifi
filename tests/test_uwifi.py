
from uwifi.core import uwifi
import time

# Initialize WiFiManager
uwifi = uwifi()

# Try to connect to a Wi-Fi network
ssid = "ssid"  # Replace with your Wi-Fi SSID
password = "password"  # Replace with your Wi-Fi password

# Connect to the Wi-Fi network with a 10-second timeout
if uwifi.connect(ssid, password, timeout=10):
    print("Connected successfully!")
else:
    print("Failed to connect. Please check your credentials.")

# Check the current Wi-Fi status
status = uwifi.check_wifi_status()
print("Current Wi-Fi status:", status)

# Set a static IP configuration
static_ip = "192.168.1.100"
subnet = "255.255.255.0"
gateway = "192.168.1.1"
dns = "8.8.8.8"  # Optional, set DNS server address
uwifi.set_static_ip(static_ip, subnet, gateway, dns)

# Check the IP configuration
ip_config = uwifi.get_ip_config()
print("Current IP configuration:", ip_config)

# Ping a server to check internet access
host = "8.8.8.8"  # Google's public DNS
if uwifi.ping(host, count=4):
    print(f"Ping to {host} successful.")
else:
    print(f"Ping to {host} failed.")

# Scan for available networks
available_networks = uwifi.list_available_networks()
print("Available networks:")
for network in available_networks:
    print(network)

# Reconnect with retry logic
if not uwifi.connect(ssid, password, timeout=10):
    print("Attempting to reconnect...")
    if uwifi.reconnect(ssid, password, timeout=10, retry_count=3):
        print("Reconnected successfully!")
    else:
        print("Failed to reconnect after multiple attempts.")

# Create an Access Point (AP)
ap_ssid = "MyAccessPoint"
ap_password = "apPassword123"  # Optional, leave as None for an open AP
uwifi.create_access_point(ap_ssid, ap_password)

# After usage, you can disable the AP
uwifi.disable_access_point()

# Disconnect from the current Wi-Fi network
uwifi.disconnect()
