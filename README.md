# GeoIP Packet Analysis to KML

This project processes packets from a `.pcap` file and uses IP geolocation to map the source and destination of each packet. The result is output as a `.kml` file for visualization in tools like Google Earth. 

![KML Output](https://i.imgur.com/TIWuRuf.jpeg)

## Table of Contents
- [Requirements](#requirements)
- [Setup](#setup)
- [Usage](#usage)
- [File Structure](#file-structure)
- [Explanation of the Code](#explanation-of-the-code)
- [Troubleshooting](#troubleshooting)
- [License](#license)

## Requirements
This project requires Python and the following Python packages:
- `dpkt`: For parsing `.pcap` files
- `pygeoip`: For IP geolocation (using the `GeoLiteCity.dat` database)

Install these requirements using:
```bash
pip install -r requirements.txt
```

The `GeoLiteCity.dat` file is also required for IP geolocation. You can download it from the [MaxMind GeoLite2](https://dev.maxmind.com/geoip/geolite2-free-geolocation-data) website.

## Setup
1. Place the `GeoLiteCity.dat` database in the same directory as your script.
2. Ensure your `.pcap` file (e.g., `wire.pcap`) is also in the same directory or update the file path in the script as needed.

## Usage
To run the script:
```bash
python script_name.py
```

The script reads packets from `wire.pcap`, extracts IPs, determines their geolocation, and outputs `myplaces.kml` for visualization in Google Earth.

## File Structure
- `script_name.py`: Main Python script for processing `.pcap` data and generating `.kml`
- `GeoLiteCity.dat`: Database file for geolocation
- `wire.pcap`: Sample `.pcap` file containing packet data
- `myplaces.kml`: Generated KML file with geolocation information

## Explanation of the Code
- **`retKML(dstip, srcip)`**: Generates a KML `<Placemark>` entry with source and destination locations from the provided IPs.
- **`plotIPs(pcap)`**: Processes each packet in the `.pcap` file, extracting IPs and creating KML entries.
- **`main()`**: Sets up the KML document structure, combines entries, and writes them to `myplaces.kml`.

## Troubleshooting
1. **No output in `myplaces.kml`**: Check that IP addresses in your `.pcap` file are mappable using `GeoLiteCity.dat`.
2. **File Errors**: Ensure that `GeoLiteCity.dat` and `wire.pcap` are correctly referenced in the same directory as your script.

## License
This project is licensed under the MIT License. Please see `LICENSE` for more details.