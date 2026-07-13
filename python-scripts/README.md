# Python Security Automation Scripts
Security automation scripts written in Python for SOC operations.

## Scripts
###  1. Log Parser (log_parser.py)
Analyses Linux auth.log files to detect brute force SSH attacks.

**what does this script do?**
- Reads auth.log line by line
- Detects failed SSH login attempts
- Counts attempts per IP address
- Flags IPs with 5+ attempts as potential brute force
- Generates a timestamped report file

**libraries used:**
- `re` - is used in order to match regular expressions for the ip addresses.
- `datetime` - is used in order to get the exact time the log analysis is being carried out.
- `collections.Counter` -  to count the number of occurence of a particular ip address.

**How to run the script:**
- save your log file in the same folder as your python script
- in order to ensure the filename in the script is the same as that of your file, open the script and input the filename in the line where the log_parser function is called.
- open your command line tool or visual code and run the python script.
- the output will be available to you as a file saved in the same folder as your python script.

**Sample output**

Log analysis started: 2026-07-11 23:05:55.777948
[FAILED LOGIN] IP: 192.168.1.100
--- BRUTE FORCE ANALYSIS ---
[ALERT] Possible brute force from 192.168.1.100 - 5 attempts

Report saved to brute_force_report.txt

### 2. Hash Checker (hash_checker.py)
Computes SHA256 hash of a file and checks it against VirusTotal's threat intelligence database.

**What it does**
- Accepts a file path as input
- Computes the file's SHA256 hash
- Queries VirusTotal API for threat intelligence
- Reports how many engines flagged the file malicious
- Supports direct hash input for checkng known hashes without needing the actual file

**Libraries used:**
- `hashlib` - computing SHA256 file hashes
- `requests` - making API calls to VirusTotal
- `os` - file path handling

**How to run**

Add your VirustTotal API key to use script the run: python hash_checker.py

**Sample output:**

Enter file path to check: test.txt
SHA256: e2e36aee69006796138168a0ace5ecd5...
[INFO] Hash not found in VirusTotal database

--- DIRECT HASH CHECK ---

Enter a hash to check directly (or press Enter to skip): b432dcf4a0f0b601b...

--- VIRUSTOTAL RESULTS ---

Malicious detections: 48
Undetected: 21
[ALERT] File is MALICIOUS - 48 engines flagged it

**Real world use case:**

During the LetsDefend SOC335 investigation, the file hash: 'b432dcf4a0f0b601b1d79848467137a5e25cab5a0b7b1224be9d3b6540122db9' was checked and confirmed malicious by 48 engines. This script automates that exact process.

  
