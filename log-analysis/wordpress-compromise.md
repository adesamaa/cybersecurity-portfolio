# Log Analysis - Compromised WordPress Investigation

## Scenario 
A Linux web server running WordPress was compromised. Analyse the Apache access logs to reconstruct the attack.

## Platforms
Blue Tean Labs Online - Log Analysis Challenge

## Tools Used
- Kali Linux terminal
- grep, awk, sort, uniq, less, head (command line log analysis)

## Attacker Information
| Artifact | Value |
| --- | --- |
| Attacker IP | 197.23.128.35 |
| Attack Date | 14 January, 2021 |
| First Successful Login | 05:51:37 UTC |

## Attack Chain (What happened step by step)
### Step 1 - Reconnaissance
Attacker used WPScan to fingerprint the WordPress site. WPScan discovered the honeypot login URL created by iThemes Security plugin.

### Step 2 - Brute Force
Attacker used the discovered login URL: /wp-login.php?itsec-hb-token=adminlogin Repeatedly attempted logins until successful at 05:51:37.

### Step 3 - Exploitation
Exploited CVE-2020-35489 in Contact Form 7 plugin - an unrestricted file upload vulnerability. Used Simple File List plugin (v4.2.2) to upload a PHP web shell.

### Step 4 - Web Shell Upload
Successfully uploaded fr34k.php to the server. A PHP web shell gives the attacker browser-based terminal access to run commands on the server.

### Step 5 - Lockout and Cleanup
Security plugin detected the attack and locked the attacker out. Attacker attempted path traversal to bypass lockout - all failed (403). Final access to fr34k.php returned 404 - shell was removed.

## Key Artifacts 
| Artifact | Value | 
| --- | --- |
| Admin Login URI | /wp-login.php?itsec-hb-token=adminlogin |
| Tools Used | WPScan, SQLmap |
| CVE Exploited | CVE-2020-35489 |
| Plugin Exploited | Simple File List v4.2.2 |
| Web Shell Filename | fr34k.php |
| Final Web Shell Response | 404 |

## MITRE ATT&CK Mapping
| Tactic | Technique | 
| --- | --- |
| Reconnaissance | T1595 - Active Scanning |
| Initial Access | T1190 - Exploit Public-Facing Application |
| Persistence | T1505.003 - Web Shell |
| Defense Evasion | T1036 - Masquerading |

## grep Commands Used 
- grep 'wp-login.php' log_analysis.txt | awk '{print $1}' | sort | uniq -c | sort -rn 
- grep '197.23.128.35' log_analysis.txt
- grep '197.23.128.35' log_analysis.txt | grep 'POST' | grep '200'
- grep '197.23.128.35' log_analysis.txt | grep 'wp-admin' | grep '200'
- grep '197.23.128.35' log_analysis.txt | grep -E 'plugin|upload|theme|shell|php'
- grep '197.23.128.35' log_analysis.txt | grep '200' | awk '{print $7}' | sort | uniq
- grep -E 'wpscan|sqlmap|wpscaN|' -i log_analysis.txt
- grep -i 'contact-form-7' log_analysis.txt
- grep -i 'wp-content/plugin' log_analysis.txt | cut -d ' ' -f7 | cut -d '/' -f4 | sort | uniq -c | sort -nr
- grep -i 'wp-content/upload' log_analysis.txt | grep '\.php'
- grep -i 'simple-file-list' log_analysis.txt

## Key Lessons Learned
- Reading through the logs meticously is very important in order not to miss indicators of compromise.
- A successful login (HTTP 200) on wp-login.php is not the end of the attack - it's the beginning. Always investigate what the attacker did AFTER gaining access, not just how they got in.
- PHP web shells like fr34k.php are dangerous because they give attackers persistent browser-based access to run system comands, always check upload directories for unexpected .php files.

## Conclusion
This was a confirmed compromise. As a SOC analyst, this is a classic situation of going through logs to identify brute force attempts, my immediate response actions would be:
1. Block 197.23.123.35 at the firewall immediately.
2. Take the WordPress site offline to prevent further damage.
3. Search all upload directories for additional web shells.
4. Reset all WordPress admin credentials.
5. Patch Contact Form 7 and Simple File List plugins immediately.
6. Escalate to Tier 2 with full artifact report and attack timeline.
7. Notify site owner of the breach.
