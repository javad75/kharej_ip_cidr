import requests
import re

# URLs to fetch IP CIDR ranges from
urls = [
    "https://raw.githubusercontent.com/lord-alfred/ipranges/main/all/ipv4_merged.txt",
    "https://core.telegram.org/resources/cidr.txt",
    "https://www.cloudflare.com/ips-v4",
    "https://raw.githubusercontent.com/HybridNetworks/whatsapp-cidr/main/WhatsApp/whatsapp_cidr_ipv4.netset",
    "https://api.fastly.com/public-ip-list",
    "https://api.gcore.com/cdn/public-ip-list"
]

# Set to store all unique IP CIDR ranges
ip_cidrs = set()

# Loop through each URL and fetch the IP CIDR ranges
for url in urls:
    response = requests.get(url)
    # Remove comments and IPv6 addresses using regular expressions
    response_text = re.sub(r'#.*\n', '\n', response.text)
    response_text = re.sub(r'[\da-fA-F]{1,4}:[\da-fA-F]{1,4}:[\da-fA-F]{1,4}:[\da-fA-F]{1,4}:[\da-fA-F]{1,4}:[\da-fA-F]{1,4}:[\da-fA-F]{1,4}:[\da-fA-F]{1,4}/\d{1,3}\n', '', response_text)
    # Extract IP CIDR ranges using regular expression
    cidrs = re.findall(r'\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}/\d{1,2}\b', response_text)
    # Add all unique IP CIDR ranges to set
    ip_cidrs.update(cidrs)

# Write unique IP CIDR ranges to file
with open("ip_cidrs.txt", "w") as f:
    for ip_cidr in ip_cidrs:
        f.write(ip_cidr + "\n")

# Remove empty lines and duplicate lines from the file
with open("ip_cidrs.txt", "r") as f:
    lines = f.readlines()

# Remove empty lines and duplicates
lines = list(filter(lambda x: x.strip() != "", lines))
lines = list(set(lines))

# Write the cleaned lines back to the file
with open("ip_cidrs.txt", "w") as f:
    f.writelines(lines)
