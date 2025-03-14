import subprocess
import re

def scan_wifi():
    #text = input("hey show me available networks: ")
    
    """Scans for available WiFi networks and displays their details."""
    try:
        result = subprocess.run(["netsh", "wlan", "show", "networks", "mode=Bssid"], capture_output=True, text=True)
        output = result.stdout

        networks = re.findall(r"SSID\s+\d+\s+:\s(.+)", output)
        signal_strengths = re.findall(r"Signal\s+:\s(.+%)", output)
        security_types = re.findall(r"Authentication\s+:\s(.+)", output)

        print("\nAvailable WiFi Networks:")
        print("------------------------------------------------")
        print("SSID\t\tSignal Strength\tSecurity")
        print("------------------------------------------------")

        # Ensure the lists are the same length
        max_length = min(len(networks), len(signal_strengths), len(security_types))
        
        for i in range(max_length):
            ssid = networks[i] if i < len(networks) else "Unknown"
            signal = signal_strengths[i] if i < len(signal_strengths) else "N/A"
            security = security_types[i] if i < len(security_types) else "N/A"
           
            print(f"{ssid[:15]:<15} {signal:<10} {security}")

            

    except Exception as e:
        print(f"Error scanning WiFi networks: {e}")

if __name__ == "__main__":
    print("Scanning for WiFi networks...\n")
    scan_wifi()
