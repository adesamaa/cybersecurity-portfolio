# Phishing Email Investigation - NDR Spoofing Attack

## Scenario 
A user received a suspicious email and forwarded it to the SOC for analysis. Investigate the email and collect useful artifacts.

## Platform
Blue Team Labs Online - Phishing Analysis Challenge

## Tools Used
- Thunder bird (mail viewing)
- Notepad (raw .eml header analysis)
- WhoIs (domain lookup)
- URL2PNG (webpage snapshot)
- VirusTotal (URL/IP reputation check)

## Investigation Process
| Artifact | Value |
| --- | --- |
| Primary Recipient | kinnar1975@yahoo.co.uk |
| Subject | Undeliverable: Website contact form submission |
| Date Sent | 18, March 2021 04:14 |
| Originating IP | 103.9.171.10 |
| Resolved Host | c5s2-1e-syd.hosting-services.net.au |
| Attached File | Website contact form submission.eml |
| Malicious URL | 35000usdperwwekpodf.blogspot.sg |
| Hosting Service | Blogger (Google Blogpost) |
| Page Status | Blog has been removed | 

## Attack Type
NDR Spoofing -- attacker sent email from a disabled mailbox triggering an automatic bounce that delivered malicious content to the victim embedded inside the NDR.
## MITRE ATT&CK Mapping
- Tactic: Initial Access
- Technique: T1566 - Phishing

## Key Lessons Learned
1. The displayed From field can be completely spoofed - always check Return-Path and X-Sender-IP for the true origin.
2. NDR bounce emails are used to deliver malicious content because victims trust automated system messages.
3. A malicious URL doesn't need to be active to be evidence - URL2PNG captures snaapshots even of taken-down pages.

## Conclusion
This was a malicious mail sent in order to gain access to the victims system. As a SOC analysts, such mails should be flagged with the appropriate reasons and then escalated to a higher tier for the issue to be addressed.
ways to handle it are:
- Block the originating IP 103.9.171.10 at the firewall to prevent future mails from coming in from that source.
- Add the malicious domain to the blocklist
- Notify the recepient to change credentials.
- FInally, escalate to tier 2 with fulll artifact report.

