# SSH Brute Force Attack - Detection with WAZUH SIEM

## Objective
Stimulate a brute force SSH attack and detect it in real time using wazuh SIEM.

## Environment
- **SIEM:** Wazuh v4.9.1
- **Attacker Machine:** Kali Linux (VIrtualBox VM)
- **Target Machine:** Wazuh Server (VirtualBox VM)
- **Network:** NAT Network

## Tools Used
- **Hydra** - brute force tool
- **rockyou.txt** - password wordlist (14 million real-world passwords)

## Attack Simulation
Ran Hydra on Kali Linux to stimulate a brute force SSH attacj against the Wazuh server, targeting the root account with 5,000+ password attempts.

Command used:
hydra -l root -P /usr/share/wordlists/rockyou.txt.gz ssh://192.168.5.8 -t 4 -V

## What Wazuh Detected
- 7,735 total alerts generated
- 7,623 authentication failures
- Rule 5557 fired - "Password check failed" (Severity Level 5)
- Attack automatically mapped to MITRE ATT&CK: T1110 - Brute Force / Password Guessing
- Rule 5760 fired - "authentication failed"
- Attack automatically mapped to MITRE ATT&CK: T1110.001, T1021.004 - Password Guessing, SSH

## Investigation Findings
| Field | Value |
| --- | --- |
| rule.description | Password check failed |
| rule.id | 5557 |
| rule.level | 5 (Medium) |
| agent.name | wazuh-server |
| MITRE Tactic | Credential Access |
| MITRE Technique | T1110 - Brute Force |

## Lessons Learned
- SSH Brute force generates massive alert volume within seconds
- Wazuh automatically maps attack patterns to the MITRE ATT&CK framework
- Disabling root SSH login entirely removes this attack vector completely
- A real SOC analyst would escalate this alert and block the source IP immediately

##Remediation Recommendations
1. Disable root SSH login - edit `/etc/ssh/sshd_config`, set `PermitRootLogin no`
2. Implement fail2ban - automatically block IPs after repeated failures
3. Use SSH key authentication instead of passwords
4. Restrict SSH access to trusted IP addresses only

##Screenshots
See screenshots folder for:
- Wazuh Threat Hunting dashboard flowing 7,735
- Events tab showing individual alert entries
- Expanded event showing rule fields
