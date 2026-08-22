# Phishing Incident Response Playbook
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


## Phase 1 — Preparation
Preparation happens before any incident occurs:
- Configure SIEM rules to flag suspicious emails including
  typosquatted domains, unusual sender IPs, and known
  malicious indicators
- Define and document escalation procedures for each
  severity level
- Ensure email gateway is configured for quarantine
  capabilities
- Conduct regular phishing awareness training for all staff
- Maintain updated blocklists for known malicious domains,
  IPs, and URLs
- Ensure analysts have access to VirusTotal, AbuseIPDB,
  and MXToolbox

## Phase 2 — Detection & Analysis
When a phishing alert is received, the analyst investigates
by following these steps in order:

**Step 1 — Sender Analysis**
- Examine the From field for typosquatting or impersonation
- Check the sender domain against known legitimate domains
- Look for subtle misspellings (e.g. coffeeshooop.com)

**Step 2 — Header Analysis**
- Extract raw email headers
- Check Return-Path, X-Sender-IP, and Received fields
- Verify if the sending IP matches the claimed sender domain
- Run the sender IP through AbuseIPDB

**Step 3 — URL and Attachment Analysis**
- Extract any URLs from the email body
- Check URLs on VirusTotal and URLScan.io
- If attachments present, compute SHA256 hash
- Check hash on VirusTotal for malicious detections

**Step 4 — Email Body Analysis**
- Identify social engineering techniques used
- Note urgency, fear, or reward-based language
- Document the lure type (voucher, invoice, delivery, etc.)

**Step 5 — Determine Verdict**
- True Positive: Email is confirmed malicious
- False Positive: Email is legitimate, close alert

## Phase 3 — Containment
Containment prevents the incident from spreading:
- Quarantine the malicious email from the recipient's inbox
- Check if other users received the same email and quarantine
  across all affected mailboxes
- Block the sender domain on the email gateway
- Block malicious URLs at the web proxy
- If user clicked a link — isolate their machine from the
  network immediately to prevent lateral movement
- Notify the affected user not to interact with the email
- Alert all staff about the phishing campaign

## Phase 4 — Eradication
Complete removal of the threat from the environment:
- Delete the phishing email from all mailboxes across
  the organisation
- Remove any downloaded attachments from affected devices
- Block the sender domain permanently on the email gateway
- Block malicious IP addresses at the firewall
- Block malicious URLs at the proxy and DNS level
- Add malicious file hashes to endpoint security blocklist

## Phase 5 — Recovery
Restore normal operations and verify the environment is clean:
- Verify all malicious emails have been removed from
  all mailboxes
- Confirm all malicious domains, IPs, and URLs are blocked
- If credentials were compromised — force password reset
  for affected accounts immediately
- Enable MFA on affected accounts if not already enabled
- Clear the affected user to resume normal work
- Monitor affected accounts for 48 hours post-incident
  for any suspicious activity

## Phase 6 — Lessons Learned
Document and improve after every incident:
- Write a full incident report covering timeline, artifacts,
  actions taken, and outcome
- Identify what detection rule fired and whether it needs tuning
- Note any gaps in the response process
- Conduct a brief staff awareness session about the specific
  phishing technique used
- Update SIEM rules and blocklists based on new indicators
- Submit indicators of compromise (IOCs) to threat intel feeds
- Business resumes normal operations


## MITRE ATT&CK Reference
| Technique ID | Name |
| --- | --- |
| T1566.001 | Spearphishing attachment |
| T1566.002 | Spearphishing link |
| T1078 | Valid Accounts (if credentials were stolen) |
| T1110 | Brute Force (credentials stuffing after harvest) |
| T1589 | Gather Victim Information |

## Appendix - Key tools used
| Tool | Purpose |
| --- | --- |
| VirusTotal | URL and hash reputation checking |
| AbuseIPDB | IP reputation checking |
| MXToolbox | Email header analysis |
| WhoIs/DomainTools | Domain investigation |
| Web proxy | URL blocking |
| Email gateway | Quarantine and blocking |



