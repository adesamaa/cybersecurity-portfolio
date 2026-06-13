# SOC335 - CVE-2024-49138 Privilege Escalation

## Alert Details
| Field | Value |
| --- | --- |
| Event ID | 313 |
| Date | Jan 22, 2025 02:37 AM |
| Severity | Medium |
| Type | Privilege Escalation |
| Hostname | Victor |
| IP Address | 172.16.17.207 |
| Process Name | svohost.exe |
| Process Path | C:\temp\service_installer\svohost.exe |
| File Hash | b432dcf4a0f0b601b1d79848467137a5e25cab5a0b7b1224be9d3b6540122db9 |
| Device Action | Allowed |

## Investigation Process 
### Step 1 - CVE Research 
Researched CVE-2024-49138 on NVD. Windows Common Log File System (CLFS) driver vulnerability allowing local privilege escalation to SYSTEM level.
### Step 2 - Process Analysis:
svohost.exe identified as typosquatting svchost.exe. Process path C:\temp\service_installer\ is not a legitimate system directory. Parent process Powershell indicates living off the land technique.
### Step 3 - Hash Check (VirusTotal):
Hash(b432dcf4a0f0b601b1d79848467137a5e25cab5a0b7b1224be9d3b6540122db9) checked on VirusTotal. Flagged as malicious by multiple detection engines. Relations tab revealed C2 IP addresses.
### Step 4 - C2 Check:
Searched C2 IP from VirusTotal Relations tab in LetsDefend Log Management. Checked if Victor's machine 172.16.17.207 made outbound connections to C2 server.
### Step 5 - Endpoint security review:
Checked Victor's machine on LetsDefend Endpoint Security. Confirmed svohost.exe executed successfully - device action was Allowed.

## Key Findings
- svohost.exe - typosquatting svchost.exe
- Executed from C:\temp - not a legitimate system path
- Spawned by Powershell - living off the land technique
- Hash confirmed malicious on VirusTotal
- CVE-2024-49138 - Windows CLFS privilege escalation

## Verdict 
True Positive - Privilege Escalation

## Response Actions
1. Isolate Victor's machine from network immediately.
2. Capture memory dump before shutdown.
3. Block hash across all endpoint security tools.
4. Search for svohost.exe on all machines in 172.16.17.x subnet.
5. Patch CVE-2024-49138 on all Windows machines.
6. Escalate to Tier 2 with full artifact report.


## MITRE ATT&CK
| Tactic | Technique |
| --- | --- |
| Execution | T1059.001 - PowerShell |
| Privilege Escalation | T1068 - Exploitation for privilege Escalation |
| Defense Evasion | T1036 - Masquerading |

## Lessons Learned 
- Running processes on a system should always be paid attention to, in order to spot any malicious process as soon as possible, malicious processes can pose as legitmate ones under the guise of using similar name that is easy to ignore like in this case (svohost.exe).
- Processes that spawn from the 'C:\temp' directory are almost always a red flag, this is because the \temp directory gives users executable and writable permissions that they wouldn't normally get if they were to run the program in \Progam Files or \System32 directory.
- After researching CVE, always take active steps to ensure that the systems are patched for this vulnerability in order to avoid future attacks that may want to exploit this weakness. Patching should be included as a recommendation when preparing your report that would be submitted to the senior SOC Analyst.


