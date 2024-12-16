
# uwifi - Wi-Fi Manager for MicroPython

`uwifi` is a Wi-Fi management library for MicroPython that allows easy connection, disconnection, and configuration of Wi-Fi interfaces. It supports both **Station (STA)** and **Access Point (AP)** modes and provides useful features like static IP configuration, ping testing, network scanning, and retry logic for connectivity issues. The library is specifically designed for use with microcontrollers and embedded systems, such as **ESP32** and **ESP8266**, making it an ideal choice for IoT projects and embedded Wi-Fi applications.

## Features

- **Connect**: Connect to a Wi-Fi network using SSID and password.
- **Disconnect**: Disconnect from the current Wi-Fi network.
- **Check Connection**: Check if the device is connected to a network.
- **Static IP Setup**: Set a static IP address, subnet mask, gateway, and DNS.
- **Ping Test**: Ping an external server to check for internet access.
- **Reconnect**: Automatically retry connecting to a network multiple times if initial attempts fail.
- **List Available Networks**: Scan and list available Wi-Fi networks (SSIDs).
- **Access Point Mode**: Set the device as an Access Point with configurable SSID, password, and authentication mode.
- **Disable AP Mode**: Disable Access Point mode when not in use.
- **Wi-Fi Status**: Display the current connection status (either connected or disconnected).

## Installation

To use `uwifi`, simply copy the `uwifi.py` file to your MicroPython project. There are no external dependencies required.

## Example Usage

```python
import time
from uwifi.core import uwifi

# Initialize the Wi-Fi Manager
wifi = uwifi()

# Connect to a Wi-Fi network
ssid = "YourWiFiSSID"  # Replace with your SSID
password = "YourWiFiPassword"  # Replace with your Wi-Fi password
if wifi.connect(ssid, password, timeout=10):
    print("Connected successfully!")
else:
    print("Connection failed. Please check your credentials.")

# Check the current Wi-Fi status
status = wifi.check_wifi_status()
print("Wi-Fi Status:", status)

# Set static IP
wifi.set_static_ip("192.168.1.100", "255.255.255.0", "192.168.1.1", "8.8.8.8")

# Get current IP configuration
print("Current IP configuration:", wifi.get_ip_config())

# Ping a server
if wifi.ping("8.8.8.8"):
    print("Ping successful!")
else:
    print("Ping failed!")

# List available networks
networks = wifi.list_available_networks()
print("Available Networks:", networks)

# Attempt to reconnect
if not wifi.connect(ssid, password, timeout=10):
    print("Attempting to reconnect...")
    if wifi.reconnect(ssid, password, timeout=10, retry_count=3):
        print("Reconnected successfully!")
    else:
        print("Failed to reconnect.")

# Create an Access Point (AP)
wifi.create_access_point("MyAP", "myAPpassword")

# Disable the AP when done
wifi.disable_access_point()

# Disconnect from the network
wifi.disconnect()
```

## Methods

### connect(ssid, password, timeout=10)
**Description**: Connects to a Wi-Fi network with the given SSID and password.  
**Parameters**:  
- `ssid`: The SSID of the Wi-Fi network.  
- `password`: The password of the Wi-Fi network.  
- `timeout`: The maximum time (in seconds) to attempt the connection.  
**Returns**: `True` if the connection is successful, `False` otherwise.

### disconnect()
**Description**: Disconnects from the currently connected Wi-Fi network.  
**Returns**: None.

### is_connected()
**Description**: Checks if the device is connected to a Wi-Fi network.  
**Returns**: `True` if connected, `False` otherwise.

### set_static_ip(ip, subnet, gateway, dns=None)
**Description**: Configures a static IP address, subnet mask, gateway, and DNS.  
**Parameters**:  
- `ip`: The static IP address.  
- `subnet`: The subnet mask.  
- `gateway`: The gateway address.  
- `dns`: (Optional) The DNS server address. Defaults to gateway if not provided.  
**Returns**: None.

### get_ip_config()
**Description**: Retrieves the current IP configuration (IP, Subnet Mask, Gateway, DNS).  
**Returns**: A tuple containing the IP address, subnet mask, gateway, and DNS.

### ping(host="8.8.8.8", count=4)
**Description**: Pings a server to check internet connectivity.  
**Parameters**:  
- `host`: The server to ping (default is 8.8.8.8).  
- `count`: The number of ping attempts to make.  
**Returns**: `True` if any ping is successful, `False` otherwise.

### reconnect(ssid, password, timeout=10, retry_count=3)
**Description**: Attempts to reconnect to a Wi-Fi network multiple times in case of failure.  
**Parameters**:  
- `ssid`: The SSID of the network.  
- `password`: The password of the network.  
- `timeout`: The timeout duration in seconds for each attempt.  
- `retry_count`: The number of retry attempts.  
**Returns**: `True` if connected successfully after retries, `False` otherwise.

### list_available_networks()
**Description**: Scans for available Wi-Fi networks and returns a list of their SSIDs.  
**Returns**: A list of SSIDs.

### create_access_point(ssid, password=None, authmode=4, channel=1, max_clients=4)
**Description**: Configures the device as an Access Point (AP).  
**Parameters**:  
- `ssid`: The SSID of the AP.  
- `password`: (Optional) The password for the AP.  
- `authmode`: The authentication mode (default is WPA2).  
- `channel`: The channel for the AP (default is 1).  
- `max_clients`: Maximum number of clients (default is 4).  
**Returns**: None.

### disable_access_point()
**Description**: Disables the Access Point mode.  
**Returns**: None.

### check_wifi_status()
**Description**: Checks the current Wi-Fi status.  
**Returns**: A string indicating the connection status (e.g., "Connected" or "Not connected").

## Requirements
- **MicroPython**: This library is designed for use with MicroPython on ESP32, ESP8266, or other compatible boards.
- **Network Interface**: The device must have a Wi-Fi interface (e.g., ESP32 or ESP8266).

## License
This project is licensed under the MIT License - see the LICENSE file for details.


## Test Images


![uwifi in Test-file](./tests/test.png)