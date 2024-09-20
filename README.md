# RPi Control CLI

A command-line interface (CLI) for remote management of Ubuntu-based Raspberry Pi systems, optimized for iPhone SSH access.

## Features

- System information retrieval
- Hardware monitoring (CPU temperature, disk usage, memory usage)
- Network diagnostics
- System maintenance (updates, reboot, shutdown)
- Wi-Fi status checking
- File system navigation
- Custom command management

## Requirements

- Python 3.6+
- psutil library
- Ubuntu-based Raspberry Pi system

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/niklas-xgh-dev/RemotePiCLI.git
   ```

2. Install dependencies:
   ```
   sudo apt install python3-psutil
   ```

3. Make the script executable:
   ```
   chmod +x rpi_control.py
   ```

4. (Optional) Move to system path:
   ```
   sudo mv rpi_control.py /usr/local/bin/rpicli
   ```

## Usage

Run the CLI:
```
./rpi_control.py
```
Or if moved to system path:
```
rpicli
```

Navigate using the numbered menu system. Use 'h' for help and 'q' to quit.

## Custom Commands

Add, remove, and execute custom commands through the CLI interface. Custom commands are stored in `custom_commands.json`.

## Note

Ensure proper security measures when enabling remote access to your Raspberry Pi.