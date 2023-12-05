from scapy.all import *
import re

# Read the pcap file
pcap_file = "meerkat.pcap"  # Replace with your pcap file name
packets = rdpcap(pcap_file)

unique_credentials = []

for packet in packets:
    if packet.haslayer(TCP):
        if packet.dport == 8080:
            if packet.haslayer(Raw):
                r = packet[0].load
                if b'username' and b'password' in r:
                    r_decoded = r.decode(errors='ignore')  # Convert bytes to string
                    # Use regex to extract username and password
                    username_match = re.search(r'username=\s*([^&\s]+)', r_decoded)
                    password_match = re.search(r'password=\s*([^&\s]+)', r_decoded)
                    if username_match and password_match:
                        username = username_match.group(1)
                        password = password_match.group(1)
                        credentials = (username, password)
                        if credentials not in unique_credentials:
                            unique_credentials.append(credentials)

print("Unique credentials tried: ", len(unique_credentials)) 

# 1 credential worked, so total failed creds is unique_creds - 1
print("Failed attempts: ", len(unique_credentials) - 1)