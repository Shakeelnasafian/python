import nmap

scanner = nmap.PortScanner()
scanner.scan('35.154.254.12', '20-1000', arguments='-sS -sV')  # SYN scan + version detection

for host in scanner.all_hosts():
    print(f"Host: {host}")
    for proto in scanner[host].all_protocols():
        ports = scanner[host][proto].keys()
        for port in ports:
            state = scanner[host][proto][port]['state']
            if state == 'open':
                print(f"Open port: {port}/{proto}")
