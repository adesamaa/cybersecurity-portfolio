# BRUTE FORCE INCIDENT RESPONSE PLAYBOOK

A brute force attack attempts to gain unauthorized access by
systematically trying passwords until the correct one is found.
This playbook guides Tier 1 SOC analysts through responding
to brute force incidents.

## Purpose
To provide a structured response process for brute force
and credential-based attacks detected by SOC analysts.

## Scope
- SSH brute force attacks
- RDP brute force attacks
- Web application login brute force
- Credential stuffing attacks
- Password spraying attacks

## Severity Classification
| Severity | Criteria |
|---|---|
| Low | Failed attempts detected, no successful login |
| Medium | High volume of attempts from single IP |
| High | Successful login detected after failed attempts |
| Critical | Successful login with privilege escalation detected |

## Phase 1 — Preparation
- Configure SIEM to alert on 5+ failed logins from same IP
- Implement account lockout policy after repeated failures
- Deploy fail2ban on Linux systems to auto-block attackers
- Enforce MFA across all user accounts
- Ensure all systems and services are patched regularly
- Maintain an asset inventory of all internet-facing services
- Disable root SSH login on all Linux systems
- Conduct regular password strength audits

## Phase 2 — Detection & Analysis
When a brute force alert fires:

**Step 1 — Review SIEM Alert**
- Note the attacking IP, target account, and timestamp
- Count total failed attempts and timeframe
- Determine if any attempts returned success (HTTP 200/
  SSH accepted)

**Step 2 — Check Attacking IP**
- Run attacking IP through AbuseIPDB for reputation score
- Check if IP appears in threat intelligence feeds
- Determine if IP is from a known VPN, Tor exit node,
  or foreign country

**Step 3 — Determine if Login Succeeded**
- Search logs for successful authentication from same IP
- If success found — escalate severity immediately
- Check what actions were taken after successful login

**Step 4 — Scope the Attack**
- Check if same IP targeted other accounts or systems
- Determine if multiple IPs are coordinating (distributed
  brute force)

## Phase 3 — Containment
If attack is still ongoing (no successful login):
- Block attacking IP at the firewall immediately
- Implement temporary account lockout for targeted account
- Enable fail2ban if not already active
- Alert the account owner

If attacker has successfully logged in:
- Isolate the compromised system from the network
  immediately to prevent lateral movement
- Disable the compromised account
- Force password reset for the affected account
- Notify the account owner

## Phase 4 — Eradication
- Block attacking IP permanently at firewall level
- Block attacking IP range if part of a known malicious range
- Add attacking IP to SIEM watchlist
- If credentials were stolen — invalidate all active sessions
  for the compromised account
- Review and strengthen password policy
- Enable MFA on the compromised account if not already enabled

## Phase 5 — Recovery
- Restore the isolated system to the network after verification
- Set up new strong password for compromised account
- Enable MFA on all affected accounts
- Monitor the previously compromised account for 72 hours
- Verify all blocking rules are in place and working
- Conduct a brief check of neighbouring systems for
  signs of lateral movement during the incident

## Phase 6 — Lessons Learned
- Document the full incident timeline with timestamps
- Record the attacking IP, targeted accounts, and outcome
- Note whether the attack succeeded and how it was detected
- Identify any gaps in detection that allowed the attack
  to go unnoticed
- Review and update SIEM detection thresholds if needed
- Submit attacking IP to threat intelligence feeds as IOC
- Verify blocked IPs remain blocked after 30 days

## MITRE ATT&CK Reference
| Technique ID | Name |
|---|---|
| T1110.001 | Brute Force — Password Guessing |
| T1110.003 | Brute Force — Password Spraying |
| T1110.004 | Brute Force — Credential Stuffing |
| T1078 | Valid Accounts (if login succeeded) |
| T1021 | Remote Services (lateral movement after login) |

## Appendix — Key Tools
| Tool | Purpose |
|---|---|
| Wazuh/Splunk | SIEM alert detection and log analysis |
| AbuseIPDB | Attacking IP reputation check |
| fail2ban | Automatic IP blocking on Linux systems |
| Firewall | IP blocking and network isolation |
| Active Directory | Account lockout and password reset |
