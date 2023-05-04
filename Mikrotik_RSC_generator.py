with open('ip_cidrs.txt', 'r') as f:
    content = f.read()

cidrs = content.split('\n')
cidrs = [cidr.strip() for cidr in cidrs if cidr.strip() != '']

with open('kharej.rsc', 'w') as f:
    f.write('/ip firewall address-list\n')
    for cidr in cidrs:
        f.write(f'add address={cidr} list=kharej\n')
