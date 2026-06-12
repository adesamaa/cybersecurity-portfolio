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
### Step 2 - Process Analysis 
### Step 3 - Hash Check (VirusTotal)
### Step 4 - C2 Check
### Step 5 - Endpoitn security review

## Key Findings
- svohost.exe - typosquatting svchost.exe
- Executed from C:\temp - not a legitimate system path
- Spawned by Powershell - living off the land technique
- Hash confirmed malicious on VirusTotal
- CVE-2024-49138 - Windows CLFS privilege escalation

## Verdict 
True Positive - Privilege Escalation

## Response Actions


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


