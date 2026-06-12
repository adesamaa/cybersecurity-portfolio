# SOC282 - Phishing Alert: Deceptive Mail

## Alert Details
| Field | Value |
| --- | --- |
| Event ID | 257 |
| Date | May 13, 2024 09:22 AM |
| Severity | Medium |
| Type | Exchange/Phishing |
| SMTP Address | free@coffeeshooop.com |
| Destination | Felix@letsdefend.io |
| Subject | Free Coffee Voucher |
| Device Action | Allowed |

## Investigation Process
### Step 1 - Initial Alert Review: I started the analysis but taking an overview of the alert and noting down the necessary details like source_ip, hostname etc. 
### Step 2 - Sender Domain Analysis: Upon opening the mail, the sender's SMTP address was carefully to spot any anamoly our phishing possibbility.
### Step 3 - IP Reputation Check (AbuseIPDB): 
### Step 4 - URL Analysis (VirusTotal)
### Step 5 - Email Content Review 

## Key Findings
- Typosquatted domain: coffeeshooop.com (3 o's)
- Malicious URL confirmed by VirusTotal
- SMTP IP clean but domain is suspicious
- Attached document present

## Verdict
True Positive - Phishing

## Response Action

## MITRE ATT&CK
- Tactic: Initial Access
- Technique: T1556 - Phishing

## Lessons Learned
- Emails are one of the most common pathways by which attackers try to gain access to a network. Using various social enginnering techniques, the attacker tries to prey on human weakness or negligince by filling the email body with enticing offers and promos. This is just on way phishing attack are carried out so it is important to always carefully analyse any incoming mail whether personal or for the company. The sender details, Subject of the mail and body should be checked for typos, mimickry, typosquatting, etc.
- To take it further, the attackers usually attached malicious URLs and files to the mail hoping for someone to click on them thereby gaining access to the victims system, It is important to raise awareness that email attachments and link should not be opened carelessly so as not to install mailicious payload on your system accidentally.
- After every successful phishing email spotting, the senders domain and attachment file hash should be added to the IPS/IDS in order to block any future or subsequent attacks from the respectfully source.
