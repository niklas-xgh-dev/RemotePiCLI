#!/usr/bin/env python3

import os
import sys
import subprocess
import psutil
import json

class UbuntuRPiControlCLI:
    def __init__(self):
        self.commands = {
            '1': ('System Info', self.system_info),
            '2': ('CPU Temp', self.cpu_temperature),
            '3': ('Disk Usage', self.disk_usage),
            '4': ('Memory Usage', self.memory_usage),
            '5': ('Network Info', self.network_info),
            '6': ('Update System', self.update_system),
            '7': ('Reboot', self.reboot_system),
            '8': ('Shutdown', self.shutdown_system),
            '9': ('WiFi Status', self.wifi_status),
            '10': ('List Files', self.list_files),
            'c': ('Custom Commands', self.custom_commands),
            'h': ('Help', self.show_help),
            'q': ('Quit', self.exit_cli)
        }
        self.custom_commands = self.load_custom_commands()

    def run_command(self, command):
        return subprocess.check_output(command, shell=True, universal_newlines=True).strip()

    def show_menu(self):
        print("\n=== Ubuntu RPi Control ===")
        for key, (name, _) in self.commands.items():
            print(f"{key}: {name}")
        print("========================")

    def show_help(self):
        """Show available commands"""
        self.show_menu()

    def system_info(self):
        """Display system information"""
        info = self.run_command("uname -a")
        print(info)
        self.copy_to_clipboard(info)

    def cpu_temperature(self):
        """Show CPU temperature"""
        try:
            temp = psutil.sensors_temperatures()['cpu_thermal'][0].current
            info = f"CPU Temperature: {temp}°C"
            print(info)
            self.copy_to_clipboard(info)
        except:
            print("Unable to read CPU temperature. Ensure 'psutil' is installed.")

    def disk_usage(self):
        """Show disk usage"""
        usage = self.run_command("df -h")
        print(usage)
        self.copy_to_clipboard(usage)

    def memory_usage(self):
        """Display memory usage"""
        usage = self.run_command("free -h")
        print(usage)
        self.copy_to_clipboard(usage)

    def network_info(self):
        """Display network information"""
        info = f"IP Address:\n{self.run_command('hostname -I')}\n"
        info += f"\nNetwork Interfaces:\n{self.run_command('ip addr show')}"
        print(info)
        self.copy_to_clipboard(info)

    def update_system(self):
        """Update the system"""
        print("Updating system...")
        result = self.run_command("sudo apt update && sudo apt upgrade -y")
        print(result)

    def reboot_system(self):
        """Reboot the system"""
        print("Rebooting...")
        os.system("sudo reboot")

    def shutdown_system(self):
        """Shutdown the system"""
        print("Shutting down...")
        os.system("sudo shutdown -h now")

    def wifi_status(self):
        """Show Wi-Fi status"""
        status = self.run_command("nmcli device wifi list")
        print(status)
        self.copy_to_clipboard(status)

    def list_files(self):
        """List files in the current directory"""
        files = self.run_command("ls -la")
        print(files)
        self.copy_to_clipboard(files)

    def custom_commands(self):
        """Manage custom commands"""
        while True:
            print("\n=== Custom Commands ===")
            for i, (name, cmd) in enumerate(self.custom_commands.items(), 1):
                print(f"{i}: {name}: {cmd}")
            print("a: Add new command")
            print("r: Remove command")
            print("b: Back to main menu")
            choice = input("Choose an option: ").strip().lower()
            
            if choice == 'a':
                name = input("Enter command name: ")
                cmd = input("Enter command: ")
                self.custom_commands[name] = cmd
                self.save_custom_commands()
            elif choice == 'r':
                name = input("Enter command name to remove: ")
                if name in self.custom_commands:
                    del self.custom_commands[name]
                    self.save_custom_commands()
                else:
                    print("Command not found.")
            elif choice == 'b':
                break
            elif choice.isdigit() and 1 <= int(choice) <= len(self.custom_commands):
                name = list(self.custom_commands.keys())[int(choice) - 1]
                result = self.run_command(self.custom_commands[name])
                print(result)
                #self.copy_to_clipboard(result)
            else:
                print("Invalid choice.")

    def load_custom_commands(self):
        try:
            with open('custom_commands.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return {}

    def save_custom_commands(self):
        with open('custom_commands.json', 'w') as f:
            json.dump(self.custom_commands, f)

    def exit_cli(self):
        """Exit the CLI"""
        print("Exiting CLI...")
        sys.exit(0)

    def run(self):
        print("Welcome to iPhone-Friendly Ubuntu on Raspberry Pi Control CLI")
        print("Type 'h' for help or 'q' to quit")

        while True:
            self.show_menu()
            try:
                command = input("Choose an option: ").strip().lower()
                if command in self.commands:
                    self.commands[command][1]()
                else:
                    print(f"Unknown command: {command}")
            except Exception as e:
                print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    cli = UbuntuRPiControlCLI()
    cli.run()
