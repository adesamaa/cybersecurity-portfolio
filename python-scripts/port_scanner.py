import socket
from datetime import datetime

def scan_port(target, start_port, end_port):
    print(f'\nScanning {target}')
    print(f'Start time: {datetime.now()}')
    print('-' * 40)

    open_ports = []

    try: 
        target_ip = socket.gethostbyname(target)
        print(f'Target IP: {target_ip}\n')

    except socket.gaierror:
        print(f'Error: Could not resolve {target}')
        return
    
    for port in range(start_port, end_port + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)

        result = sock.connect_ex((target_ip, port))

        if result == 0:
            try:
                service = socket.getservbyport(port)
            except: 
                service = 'unknown'
            print(f'[OPEN] Port {port} - {service}')
            open_ports.append(port)

        sock.close()

    print('-' * 40)
    print(f'Scan complete: {len(open_ports)} open ports found')
    print(f'End time: {datetime.now()}')

    return open_ports

# Run scanner
target = input('Enter target IP or hostname: ')
start = int(input('Start port: '))
end = int(input('End port: '))

scan_port(target, start, end)
