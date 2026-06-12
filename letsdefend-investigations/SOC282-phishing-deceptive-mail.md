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
### Step 2 - Sender Domain Analysis
### Step 3 - IP Reputation Check (AbuseIPDB)
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
