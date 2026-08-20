# PHISHING INCIDENT RESPONSE PLAYBOOK
a phishing email can come in any form, this is a proper way to handle any phishing incident you come across.

## Purpose
 A step-by-step guide to handle a phishing alert received by a tier 1 SOC analyst

## Scope
- Phishing emails
- voice phishing 
- credential harvesting

## Severity Classification


## Phase 1 - Preparation
This involves setting up the alert rules for correctly flagging a phishing event alert as dangerous or not. Policies are defined as to how to handle the phishing attempts, SIEM tools are finetuned to detect occasions of typosquatting etc.
part of preparation is to educate employees on how to properly identifying/recognise a phishing attempt, informing them about the different techniques that might be employed and how to carefully detecct them.

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


## Appendix - Key tools used



