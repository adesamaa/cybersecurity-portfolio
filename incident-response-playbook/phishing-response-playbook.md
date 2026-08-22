# PHISHING INCIDENT RESPONSE PLAYBOOK
A phishing email can come in any for. This playbook provides a structured approach for Tier 1 SOC analysts to handle any phishing incident from detection to resolution.

## Purpose
To provide a step-by-step guide for handling phishing alerts
received by a Tier 1 SOC analyst, ensuring consistent and
thorough incident response

## Scope
This playbook covers the following phishing attack types:
- Phishing emails (malicious links and attachments)
- Spear phishing (targeted phishing against specific individuals)
- Voice phishing (vishing)
- Credential harvesting attempts

## Severity Classification
| Severity | Criteria |
| --- | --- |
| Low | Phishing email received, not interacted with |
| Medium | User clicked link, but no credentials entered | 
| High | User clinked link and entered credentials |
| Critical | Muktiple users affected, active compromise detected |


## Phase 1 - Preparation
This involves setting up the alert rules for correctly flagging a phishing event alert as dangerous or not. 
Policies are defined as to how to handle the phishing attempts, SIEM tools are finetuned to detect occasions of typosquatting etc.
part of preparation is to educate employees on how to properly identifying/recognise a phishing attempt, 
informing them about the different techniques that might be employed and how to carefully detecct them.

## Phase 2 - Detection & Analysis
When a new phishing alert is received, it is the job of the SOC analyst to investigate it. This id carried oout by doing:
• analyse the sender's details, watching out for typosquatting or impersonation or any errors.
• check the email header for the return path, sender's IP,and run them across detection tools
• check for any attach files or URL and look up its hash on virustotal
• Next, analyse the email body for spooking, ransoming, etc. 

## Phase 3 - Containment
containment is done in order to prevent the whole netwrok from the ongoing incident.
firstky, emails that have been confirmed to be malicious are quarantined from the inbox.
• next, the sender was blocked from the email gateway to prevent future msils from coming in.
• other the employee is informed not to open the email from the said sendder 
• you can then alert the employees about the email.

## Phase 4 - Eradication
how can we do away with the phishing email:
- deleting the email from the employee's device as well as any downloaded attachment
- blocking the sender's domain 
- blocking domain IP from the proxy

## Phase 5 - Recovery
the point of this is to return to normalcy like before the incident happened;
firstly, verify that the blocked ip, domains, urls are blocked.
- confirm the email is no longer on any system in the network
- clear the employee to continue working
- confirm credentials weren't lost during the attack and if they were, employees have to reset passwords

## Phase 6 - Lessons Learned
this is where reports are written and the whole incident from phase 1 to phase 5 is documented.
- recommendations for future incidents are given
- employees are once again educated on phishing emails and how to identify them
- system is patched to be up to date
business reumes as usual 


## MITRE ATT&CK Reference
- T1566.001 - Spearphishing attachment
- T1566.002 - Spearphishing link
- T1078 - Valid Accounts (if credentials were stolen)
- T1110 - Brute Force (credentials stuffing after harvest)

## Appendix - Key tools used
- VirusTotal - URL and hash reputation checking
- AbuseIPDB - IP reputation checking
- MXToolbox - Email header analysis
- WhoIs/DomainTools - Domain investigation
- Email gateway - Quarantine and blocking



