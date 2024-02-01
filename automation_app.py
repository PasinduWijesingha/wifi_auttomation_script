import os
import subprocess
import time

def check_internet():
    try:
        subprocess.check_output(["ping", "8.8.8.8"], timeout=5)
        return True
    except subprocess.CalledProcessError as e:
        print(f"Error checking internet connectivity: {e}")
        return False
    except Exception as e:
        print(f"Unexpected error: {e}")
        return False

def switch_wifi(new_wifi_ssid, new_wifi_password):
    # This example assumes you are on a Windows system
    # Adjust the command based on your operating system if needed
    command = f'netsh wlan connect name="{new_wifi_ssid}" password="{new_wifi_password}"'
    try:
        subprocess.run(command, shell=True, check=True)
        print("WiFi switched successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error switching WiFi: {e}")

def main():
    current_wifi_ssid = "Redmi Note 9 Pro"
    new_wifi_ssid = "ConnexTechnical"
    new_wifi_password = "C0nnexTechnic@l"

    while True:
        if not check_internet():
            print("Lost internet connection. Switching to new WiFi...")
            switch_wifi(new_wifi_ssid, new_wifi_password)
            time.sleep(5)  # Wait for 30 seconds before checking again
        else:
            print("Internet connection is stable.")
            time.sleep(5)  # Check every 5 minutes

if __name__ == "__main__":
    main()
