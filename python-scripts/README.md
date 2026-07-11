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
- 're' - is used in order to match regular expressions for the ip addresses.
- 'datetime' - is used in order to get the exact time the log analysis is being carried out.
- 'collections.Counter' - so as to count the number of occurence of a particular ip address.

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
