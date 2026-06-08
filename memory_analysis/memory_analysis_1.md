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
| Windows Version | Windows 7 SPI x86 |
| Image Capture Date| 2021-01-31 18:24:57 UTC |
| Memory Dump Formate | VMEM |

## Investigation Process

### Step 1 - Image Identification
Ran imageinfo plugin to identify the Windows profile needed for all subsequent volatility commands.
.\volatility_2.6_win64_standalone.exe -f infected.vmem imageinfo

### Step 2 — Process List Analysis
Ran pslist and psscan to identify all running processes and the following suspicious process was identified: or4qtckT.exe
.\volatility_2.6_win64_standalone.exe -f infected.vmem --profile=Win73P1x86 pslist

### Step 3 — Malicious Process Investigation
Drilled into the suspicious PID using psscan to identify the process used to delete files.
.\volatility_2.6_win64_standalone.exe -f infected.vmem --profile=Win73P1x86 psscan | findstr 2732

### Step 4 — Execution Path
Used cmdline plugin to find the full path where the malicious file was first executed.
.\volatility_2.6_win64_standalone.exe -f infected.vmem --profile=Win73P1x86 cmdline

### Step 5 — Ransomware Identification
Researched or4qtckT.exe and identified the ransomware as WannaCry — one of the most destructive ransomware attacks in history, responsible for the 2017 global attack affecting NHS, FedEx and thousands of organisations.

### Step 6 — Public Key Recovery
Used filescan plugin to locate the ransomware public key file used to encrypt the victim's private key. 
.\volatility_2.6_win64_standalone.exe -f infected.vmem --profile=Win73P1x86 filescan | findstr '.eky'
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
- It is important to isolate any infected system once it has been compromised, after this, the system must be kept on and an image be taken, this will enable further analysis and investigation. A lot of hidden processes run behind the scene so it is very important to be able to link isolated events through the pstree and know how they relate with each other.

## Conclusion
When an event like this occurs, the first step is to isolate the infected system, then take a memory dump of the RAM. Using suitable tools, the required information is extracted, and the various processes and applications involved in the attack are enumerated, this event is then marked with the appropraite flag based on the findings and then escalated to a senior SOC analyst for action.
be as a SOC analyst if this was a live incident?
