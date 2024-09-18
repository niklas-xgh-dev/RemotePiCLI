#!/usr/bin/env python3

import os
import sys
import subprocess
import psutil

class UbuntuRPiControlCLI:
    def __init__(self):
        self.commands = {
            'help': self.show_help,
            'sys': self.system_info,
            'temp': self.cpu_temperature,
            'disk': self.disk_usage,
            'mem': self.memory_usage,
            'ps': self.process_list,
            'net': self.network_info,
            'update': self.update_system,
            'reboot': self.reboot_system,
            'shutdown': self.shutdown_system,
            'services': self.list_services,
            'wifi': self.wifi_status,
            'ls': self.list_files,
            'exit': self.exit_cli
        }

    def run_command(self, command):
        return subprocess.check_output(command, shell=True, universal_newlines=True).strip()

    def show_help(self):
        """Show available commands"""
        print("Available commands:")
        for cmd, func in self.commands.items():
            print(f"  {cmd}: {func.__doc__}")

    def system_info(self):
        """Display system information"""
        print(self.run_command("uname -a"))
        print(self.run_command("cat /etc/os-release | grep PRETTY_NAME"))

    def cpu_temperature(self):
        """Show CPU temperature"""
        try:
            temp = psutil.sensors_temperatures()['cpu_thermal'][0].current
            print(f"CPU Temperature: {temp}°C")
        except:
            print("Unable to read CPU temperature. Ensure 'psutil' is installed.")

    def disk_usage(self):
        """Show disk usage"""
        print(self.run_command("df -h"))

    def memory_usage(self):
        """Display memory usage"""
        print(self.run_command("free -h"))

    def process_list(self):
        """List running processes"""
        print(self.run_command("ps aux"))

    def network_info(self):
        """Display network information"""
        print("IP Address:")
        print(self.run_command("hostname -I"))
        print("\nNetwork Interfaces:")
        print(self.run_command("ip addr show"))

    def update_system(self):
        """Update the system"""
        print("Updating system...")
        print(self.run_command("sudo apt update && sudo apt upgrade -y"))

    def reboot_system(self):
        """Reboot the system"""
        print("Rebooting...")
        os.system("sudo reboot")

    def shutdown_system(self):
        """Shutdown the system"""
        print("Shutting down...")
        os.system("sudo shutdown -h now")

    def list_services(self):
        """List active services"""
        print(self.run_command("systemctl list-units --type=service --state=running"))

    def wifi_status(self):
        """Show Wi-Fi status"""
        print(self.run_command("nmcli device wifi list"))

    def list_files(self):
        """List files in the current directory"""
        print(self.run_command("ls -la"))

    def exit_cli(self):
        """Exit the CLI"""
        print("Exiting CLI...")
        sys.exit(0)

    def run(self):
        print("Welcome to Ubuntu on Raspberry Pi Control CLI")
        print("Type 'help' for a list of commands")

        while True:
            try:
                command = input("Ubuntu-RPi> ").strip().lower()
                if command in self.commands:
                    self.commands[command]()
                else:
                    print(f"Unknown command: {command}")
                    print("Type 'help' for a list of commands")
            except Exception as e:
                print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    cli = UbuntuRPiControlCLI()
    cli.run()