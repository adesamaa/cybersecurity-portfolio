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
| Subject | Undeliverable: Website contact information |
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
Email should be viewed with caution because there are lots of malicious threat actors hiding behind what appears to be a valid email, SOC analyst should always pay attention when analyzing mails such as these and also advise other employees to be more cautious and to report anything suspicious, if they spot any.

## Conclusion
This was a malicious mail in order to gain access to the victims system, as an junior SOC analysts, such mails should be flagged with the appropriate reasons and then escalated to a higher tier for the issue to be addressed.

-
