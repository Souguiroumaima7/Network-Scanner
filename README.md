# Network-Scanner
Here's a sample README for a **Network Scanner** tool. You can adjust the details based on your specific implementation and features:

---

# Network Scanner

A simple and efficient network scanner tool to discover active devices in a network, check open ports, and gather basic information about devices (such as IP address, MAC address, and device type). This tool can be used for network management, security assessments, and troubleshooting.

## Features
- **Discover Active Hosts**: Scan a given subnet or IP range to discover active devices.
- **Port Scanning**: Identify open ports on the discovered devices.
- **MAC Address Identification**: Retrieve the MAC address of devices in the network.
- **Service Information**: Fetch basic information about services running on open ports (HTTP, FTP, SSH, etc.).
- **OS Detection**: Optionally, attempt to identify the operating system of the device based on open ports and network behavior.
- **User-friendly Output**: Display results in an easy-to-read format.

## Requirements

- Python 3.x or higher
- `scapy` library for sending/receiving packets
- `socket` library for handling network connections
- `nmap` (optional, for enhanced port scanning and OS fingerprinting)

### Installing Required Libraries

```bash
pip install scapy
pip install python-nmap
```

## Installation

1. Clone or download the repository:

   ```bash
   git clone https://github.com/yourusername/network-scanner.git
   cd network-scanner
   ```

2. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the script to discover active devices and perform network scans. Basic usage involves providing a target IP range or subnet.

### Discover Active Hosts in a Network

```bash
python network_scanner.py <subnet_or_range>
```

**Arguments**:
- `<subnet_or_range>`: The IP subnet or range to scan, e.g., `192.168.1.0/24` or `192.168.1.1-254`.

#### Example:

```bash
python network_scanner.py 192.168.1.0/24
```

This will scan all devices on the `192.168.1.x` subnet.

### Scan Specific Ports for a Host

```bash
python network_scanner.py <target_ip> --ports <port_range>
```

**Arguments**:
- `<target_ip>`: The IP address of the target device to scan.
- `--ports`: A comma-separated list of ports or a range, e.g., `80,443` or `22-1024`.

#### Example:

```bash
python network_scanner.py 192.168.1.10 --ports 22,80,443
```

This will scan ports 22 (SSH), 80 (HTTP), and 443 (HTTPS) on `192.168.1.10`.

### Output Format

The output will display the following information:

1. **Active Hosts**: List of IP addresses that responded during the scan.
2. **Open Ports**: A list of open ports discovered on each device.
3. **MAC Addresses**: The MAC addresses of the devices in the network.
4. **Service Information**: Services running on open ports (e.g., HTTP, FTP, SSH).
5. **OS Detection** (if supported and configured): Possible OS of the device based on open ports and behavior.

#### Example Output:

```
Scanning subnet: 192.168.1.0/24

Active Hosts:
  192.168.1.1 - Mac Address: 00:14:22:01:23:45
  192.168.1.10 - Mac Address: 00:14:22:67:89:AB

Host 192.168.1.1:
  Open Ports: 80 (HTTP), 22 (SSH)
  OS: Linux

Host 192.168.1.10:
  Open Ports: 443 (HTTPS)
  OS: Windows
```

## Advanced Features (Optional)

### OS Fingerprinting

If you have `nmap` installed, the tool can try to perform OS fingerprinting on each discovered device. You can enable this feature by adding the `--os-fingerprint` flag.

```bash
python network_scanner.py 192.168.1.0/24 --os-fingerprint
```

### Scan Multiple Subnets/Ranges

You can also provide multiple IP ranges or subnets for scanning by separating them with commas.

```bash
python network_scanner.py 192.168.1.0/24,10.0.0.0/24
```

### Save Scan Results to File

You can save the scan results to a file by adding the `--output` option:

```bash
python network_scanner.py 192.168.1.0/24 --output scan_results.txt
```

This will save the results in a text file called `scan_results.txt`.

## Contributing

Contributions are welcome! If you'd like to contribute, please follow these steps:
1. Fork this repository.
2. Create a new branch for your feature or bugfix.
3. Commit your changes and push to the branch.
4. Open a pull request with a clear description of your changes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Disclaimer

Use this tool responsibly. Unauthorized scanning of networks may be illegal and can result in severe consequences. Ensure you have explicit permission before scanning any network or device.

---

Feel free to customize the instructions and details based on how your Network Scanner is designed!
