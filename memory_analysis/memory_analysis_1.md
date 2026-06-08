# MEMORY ANALYSIS - WANNACRY RANSOMWARE INVESTIGATION

## Scenario
A Windows machine was infected with ransomware. A memory dump was captured during the incident. Analyse the dump to identify ransomware and collect forensic artifacts.

## Platform
Blue Team Labs Online - Memory Analysis Ransomware Challenge

## Tools Used 
- Volatility2 (Windows standalone executable)
- Windows Powershell

## System Information
| Field | Value |
| --- | --- |
| Windows Version | Windows 7 SP1 x86 |
| Image Capture Date| 2021-01-31 18:24:57 UTC |
| Memory Dump Formate | VMEM |

## Investigation Process

### Step 1 - Image Identification
Ran imageinfo plugin to identify the Windows profile needed for all subsequent volatility commands.
.\volatility_2.6_win64_standalone.exe -f infected.vmem imageinfo

### Step 2 — Process List Analysis
Ran pslist and psscan to identify all running processes and the following suspicious process was identified: or4qtckT.exe
.\volatility_2.6_win64_standalone.exe -f infected.vmem --profile=Win7SP1x86 pslist

### Step 3 — Malicious Process Investigation
Drilled into the suspicious PID using psscan to identify the process used to delete files.
.\volatility_2.6_win64_standalone.exe -f infected.vmem --profile=Win7SP1x86 psscan | findstr 2732

### Step 4 — Execution Path
Used cmdline plugin to find the full path where the malicious file was first executed.
.\volatility_2.6_win64_standalone.exe -f infected.vmem --profile=Win7SP1x86 cmdline

### Step 5 — Ransomware Identification
Researched or4qtckT.exe and identified the ransomware as WannaCry — one of the most destructive ransomware attacks in history, responsible for the 2017 global attack affecting NHS, FedEx and thousands of organisations.

### Step 6 — Public Key Recovery
Used filescan plugin to locate the ransomware public key file used to encrypt the victim's private key. 
.\volatility_2.6_win64_standalone.exe -f infected.vmem --profile=Win7SP1x86 filescan | findstr '.eky'
Found: 00000000.eky

## Key Artifacts
| Artifact | Value |
|---|---|
| Malicious Process | or4qtckT.exe |
| Ransomware Family | WannaCry |
| Public Key File | 00000000.eky |
| Execution Path | C:\Users\hacker\Desktop\or4qtckT.exe |
| File Deletion Tool | taskdl.exe |

## Volatility Commands Used
- imageinfo
- pslist
- psscan
- cmdline
- filescan

## MITRE ATT&CK Mapping
| Tactic | Technique |
|---|---|
| Execution | T1204 - User Execution |
| Impact | T1486 - Data Encrypted for Impact |
| Defense Evasion | T1036 - Masquerading |
| Discovery | T1057 - Process Discovery |

## Key Lessons Learned
1. RAM is volatile so make sure you always capture a memory dump before shutting down an infected machine. Shutting it down destroys any amount of evidence that only exist in memory (running processes, network connections, encryption keys).
2. Malware hides in plain sight. For example, or4qtckT.exe had a random name designed so as to avoid detection. Knowing this, always cross-reference unfamiliar process names agianst threat intelligence tools before dismissing them.
3. Memory forensics reveals the full attack chain - pslist, psscan, cmdline and filescan which were used in this lab together told the complete story - how WannaCry got on the machine, where it ran from, what it used to delete files and where it stored its keys.

## Conclusion
This was a confirmed WannaCry ransomware infection. As a SOC analyst, my immediate response actions would be: isolate the infected machine from the network immediately to prevent lateral movements, preserve the memory dump as forensic evidence, block the hash of or4qtckT.exe on all endpoint security tools across the organisation, check neighbouring machines for signs of the same infection, notify affected users and management, recover files from the restore point taken before encryption, and escalate to Tier 2 with the full Volatility artifact report and attack timeline. WannaCry spreads aggressively via EternalBlue. Therefore, speed of containment is very critical.
