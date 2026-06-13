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
### Step 1 - Initial Alert Review
Reviewed alert details noting: SMTP address - free@coffeeshooop.com, destination - Felix@letsdefend.io, subject - "Free Coffee Voucher", device action - Allowed meaning the email reached the recipient inbox. 
Flagged for immediate investigation.
### Step 2 - Sender Domain Analysis 
Carefully examined sender address free@coffeeshooop.com, identified typosquatting - coffeesshooop.com contains three o's instead of two, mimicking a legitimae coffee brand domain.
This is a clear indicator of phishing intent.
### Step 3 - IP Reputation Check (AbuseIPDB)
Checked SMTP IP 103.80.134.63 on AbuseIPDB. Result: 0% abuse confidence score - IP appears clean. 
Note: Clean IP does not clear the alert - attackers regularly use fresh IPs to avoid reputation-based detection.
### Step 4 - URL Analysis (VirusTotal)
Extracted URL from email body and checked on VirusTotal. 
Result: Flagged as malicious by multiple detection engines. This confirmed the email as malicious regardless of clean IP.
### Step 5 - Email Content Review
Email body containeda free coffee voucher lure with an attached document. Classic social engineering technique - reward-based urgency designed to get victim to click without thinking critically.

## Key Findings
- Typosquatted domain: coffeeshooop.com (3 o's)
- Malicious URL confirmed by VirusTotal
- SMTP IP clean but domain is suspicious
- Attached document present

## Verdict
True Positive - Phishing

## Response Action
1. Quarantine the email from Felix's inbox immediately.
2. Block sender domain coffeeshooop.com on email gateway
3. Block SMTP IP 103.80.134.63 at the firewall
4. Add malicious URL to web proxy blocklist
5. Notify Felix not to click any links or open attachments
6. Search email gateway logs for other recipients of emails from the same domain
7. Escalate to Tier 2 with full artifact report

 
## MITRE ATT&CK
- Tactic: Initial Access
- Technique: T1566 - Phishing

## Lessons Learned
- Emails are one of the most common pathways by which attackers try to gain access to a network. Using various social enginnering techniques, the attacker tries to prey on human weakness or negligince by filling the email body with enticing offers and promos. This is just on way phishing attack are carried out so it is important to always carefully analyse any incoming mail whether personal or for the company. The sender details, Subject of the mail and body should be checked for typos, mimickry, typosquatting, etc.
- To take it further, the attackers usually attached malicious URLs and files to the mail hoping for someone to click on them thereby gaining access to the victims system, It is important to raise awareness that email attachments and link should not be opened carelessly so as not to install mailicious payload on your system accidentally.
- After every successful phishing email spotting, the senders domain and attachment file hash should be added to the IPS/IDS in order to block any future or subsequent attacks from the respectfully source.
