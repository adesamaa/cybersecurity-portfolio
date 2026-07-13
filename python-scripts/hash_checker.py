import hashlib
import requests 
import os

def get_file_hash(filepath):
    sha256 = hashlib.sha256()

    try:
        with open(filepath, 'rb') as f:
            for chunk in iter(lambda: f.read(4096), b''):
                sha256.update(chunk)
        return sha256.hexdigest() 
    
    except FileNotFoundError:
        print(f'Error: FIle {filepath} not found')
        return None
    
def check_virustotal(file_hash, api_key):
    url = f'https://www.virustotal.com/api/v3/files/{file_hash}'
    headers = {'x-apikey': api_key}

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        stats = data['data']['attributes']['last_analysis_stats']
        malicious = stats['malicious']
        undetected = stats['undetected']

        print(f'\n--- VIRUSTOTAL RESULTS ---')
        print(f'Malicious detections: {malicious}')
        print(f'Undetected: {undetected}')

        if malicious > 0:
            print(f'[ALERT] File is MALICIOUS - {malicious} engines flagged it')
        else: 
            print('[CLEAN] No malicious detections found')
    elif response.status_code == 404:
        print('[INFO] Hash not found in VirusTotal database')

    else:
        print(f'Error: {response.status_code}')

# Configuration
API_KEY = 'e3cb2f932c9601eb5db0ca8824b8d1be7c1e5cd22c2c3eb59bb12a1b9a8b863d'
filepath = input('Enter file path to check: ')
file_hash = get_file_hash(filepath)

if file_hash:
    print(f'SHA256: {file_hash}')
    check_virustotal(file_hash, API_KEY)
        
