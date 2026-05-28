# Port Scan Detection - Nmap Reconnaissance

## Objective
Stimulate a network reconnaissance port scan and detect it using Wazuh SIEM.

## Tools Used
- Nmap (Kali Linux)
- Wazuh SIEM

## Attack Simulation
Ran Nmap aggressive scan against Wazuh server:
nmap -A -p 1-1000 [target-ip]

## Results
- 998 closed ports
- 2 open ports: SSH (22) and HTTPS (443)
- OS fingerprinting and version detection completed successfully

## SIEM Detection Challenge
Wazuh did not generate port scan alerts out of the box.
Custom rule added to local_rules.xml mapping to MITRE T1046.
Rule did not fire -- root cause: Wazuh requires a network sensor (Suricata/Zeek) feeding network traffic logs to detect port-scans.
Authentication-based events are detected natively; network recoannaissance requires additional log sources.

## Key Lessons Learned
- Nmap -A flag combines version detection, OS fingerprinting and banner grabbing
- Port scan = MITRE ATT&CK T1046 -- Network Service Discovery
- SIEMs require proper log sources to detect specific attack types
- Port scan detection requires a network IDS like suricata alongside Wazuh
- SIEM tuning is an ongoing process, not a one-time setup

## Next Steps
- Install Suricata as network sensor feeding into Wazuh
- Re-run port scan to confirm detection with proper log source
