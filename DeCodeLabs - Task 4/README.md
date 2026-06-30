# Windows 11 Workstation - System Vulnerability Audit & Hardening
A hands-on cybersecurity audit and local hardening project completed as part of my Cyber Security Intern role at DecodeLabs (Project 4).

## 🎯 Project Overview
This project focuses on **proactive defense (Blue Teaming)** by auditing, identifying, and remediating security misconfigurations on a personal workstation. It covers identity controls, software patch management, privilege levels, and endpoint security hygiene.

## 🛠️ Skills Demonstrated
- **Operating System Security & Baseline Hardening** (Windows 11)
- **Identity & Access Management (IAM)** (Password controls, privilege auditing)
- **Endpoint Protection** (BitLocker disk encryption, Windows Defender Firewall)
- **Vulnerability Reporting & Risk Scoring** (Using CVSS v4.0 metrics)

---

## 🔍 Identified Vulnerabilities & CVSS Ratings

| Vulnerability | Initial Configuration | Security Risk | CVSS v4.0 | Remediation Status |
| :--- | :--- | :--- | :---: | :--- |
| **Weak Password Length** | Min Length: `0` | Medium | **5.3** | Hardened to `8` chars |
| **Password History Disabled** | Retained: `None` | Medium | **4.0** | Configured to remember `5` passwords |
| **Storage Encryption Disabled** | Status: `FullyDecrypted` | High | **7.5** | Documented BitLocker plan |

---

## 🛡️ Implementation & Remediation Commands

Below are the PowerShell commands executed in an elevated administrative session to resolve the findings:

### 1. Password Policy Hardening
```powershell
# Enforce a minimum password length of 8 characters
net accounts /minpwlen:8

# Prevent password reuse by keeping track of the last 5 unique passwords
net accounts /uniquepw:5
