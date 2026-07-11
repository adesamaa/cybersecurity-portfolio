import re 
from collections import Counter
from datetime import datetime
print(f'Log analysis started: {datetime.now()}')

def parse_log(filename):
    failed_ips = []

    try:
        with open(filename, 'r') as f:
            for line in f:
                if 'Failed password' in line:
                    match = re.search(r'from (\d+\.\d+\.\d+\.\d+)', line)
                    if match:
                        ip = match.group(1)
                        failed_ips.append(ip) 
                        print(f'[FAILED LOGIN] IP: {ip}')

    except FileNotFoundError:
        print(f'Error: File {filename} not found')
        return
    print('\n--- BRUTE FORCE ANALYSIS ---')
    ip_counts = Counter(failed_ips)

    with open('brute_force_report.txt', 'w') as report:
        report.write('BRUTE FORCE ANALYSIS REPORT\n')
        report.write('='*30 + '\n')
        report.write(f'Analysis time: {datetime.now()}\n\n')

        for ip, count in ip_counts.most_common():
            if count >= 5:
                print(f'[ALERT] Possible brute force from {ip} - {count} attempts')
                report.write(f'[ALERT] {ip} - {count} attempts\n')

    print('\nReport saved to brute_force_report.txt')


parse_log('auth.log')                     
