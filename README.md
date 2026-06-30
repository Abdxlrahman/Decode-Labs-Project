# 🛡️ DeCode Labs — Cybersecurity Analyst Internship

<div align="center">

![DeCode Labs](https://img.shields.io/badge/DeCode%20Labs-Cybersecurity%20Internship-blue?style=for-the-badge&logo=shield&logoColor=white)
![Batch](https://img.shields.io/badge/Batch-2026-green?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Completed-success?style=for-the-badge)
![Projects](https://img.shields.io/badge/Projects-4%20Completed-orange?style=for-the-badge)

**A complete collection of 4 hands-on cybersecurity projects completed during the DeCode Labs Internship Program (2026).**

*Covering Password Security · Cryptography · Network Analysis · System Hardening*

</div>

---

## 👨‍💻 About This Repository

This repository contains all **4 projects** completed as part of the **DeCode Labs Cybersecurity Analyst Internship Program – Batch 2026**.

Each project covers a distinct domain of cybersecurity — from building security tools and implementing cryptographic ciphers, to performing real network traffic analysis and hardening a live Windows workstation.

| # | Project | Domain | Deliverable |
|:---:|:---|:---|:---|
| 🔐 | [Task 1 — Password Strength Checker](#task-1---password-strength-checker) | Application Security | Python CLI + Web App |
| 🔒 | [Task 2 — CryptoVault](#task-2---cryptovault) | Cryptography | Python CLI + Web Dashboard |
| 📡 | [Task 3 — Network Traffic Analysis](#task-3---network-traffic-analysis) | Network Security | Wireshark Analysis + Report |
| 🖥️ | [Task 4 — System Vulnerability Audit](#task-4---system-vulnerability-audit) | Endpoint Security / Blue Team | Audit Report + Hardening |

---

## 📁 Repository Structure

```
Decode-Labs-Project/
│
├── 📁 DeCodeLabs - Task 1/       ← Password Strength Checker
│   ├── 📁 Code/
│   │   ├── password_analyzer.py
│   │   └── requirements.txt
│   ├── 📁 Website/
│   │   ├── index.html
│   │   ├── style.css
│   │   └── script.js
│   ├── 📁 Word doc/
│   └── README.md
│
├── 📁 DeCodeLabs - Task 2/       ← CryptoVault
│   ├── 📁 python_app/
│   │   ├── crypto_vault.py
│   │   └── requirements.txt
│   ├── index.html
│   ├── .gitignore
│   └── README.md
│
├── 📁 DeCodeLabs - Task 3/       ← Network Traffic Analysis
│   └── README.md
│
├── 📁 DeCodeLabs - Task 4/       ← System Vulnerability Audit
│   ├── 📁 Assets/
│   ├── 📁 Report/
│   └── README.md
│
└── README.md                     ← You are here
```

---

## Task 1 — Password Strength Checker

> **Domain:** Application Security · **Stack:** Python, HTML, CSS, JavaScript

A dual-interface password security tool that evaluates the strength of any password using advanced security principles.

### 🎯 What It Does
- Scores passwords from **0–100** across multiple security criteria
- Detects **sequential patterns** (`abc`, `123`, `qwerty`) and **repeated characters**
- Integrates the **HaveIBeenPwned API** to check against real breach databases
- Calculates **Shannon Entropy** to measure true randomness
- Estimates **GPU crack time** for a given password
- Generates a **cryptographically secure password** as a suggestion
- Exports a **PDF Security Report**

### ⚙️ Tech Stack
`Python 3.x` · `HTML5/CSS3/JavaScript` · `HaveIBeenPwned API` · `Argon2id` · `Scrypt`

### 🔗 [→ View Task 1 Folder](./DeCodeLabs%20-%20Task%201/)

---

## Task 2 — CryptoVault

> **Domain:** Cryptography · **Stack:** Python, HTML, CSS, JavaScript

An advanced cryptography engine and cryptanalysis suite implementing 6 classic ciphers, with a full brute-force simulation and integrity verification.

### 🎯 What It Does
- Implements **Caesar, Vigenère, Atbash, ROT13, XOR, and Reverse** ciphers
- **Round-Trip Integrity Verification**: validates `Decrypt(Encrypt(M)) == M` in real-time
- **Brute-Force Cryptanalysis Simulator** — automated Caesar cracking via dictionary heuristics
- **Client-side only** — zero network transmission; all processing is local
- Exports a **PDF Audit Report** of cipher operations
- Full **Web Dashboard** (Glassmorphic UI) + Python CLI

### ⚙️ Tech Stack
`Python 3.x` · `HTML5/CSS3/JavaScript` · `Web Crypto API`

### 🔗 [→ View Task 2 Folder](./DeCodeLabs%20-%20Task%202/)

---

## Task 3 — Network Traffic Analysis

> **Domain:** Network Security · **Stack:** Wireshark, Python

A real-world network forensics investigation using Wireshark to capture, filter, and analyze live network traffic for signs of malicious activity and protocol anomalies.

### 🎯 What It Does
- Captured and analyzed **live network packets** using Wireshark
- Identified **suspicious traffic patterns**, protocol anomalies, and potential threats
- Performed **protocol dissection** across TCP/IP, DNS, HTTP, HTTPS, and ICMP
- Generated a professional **Threat Detection Report** with findings
- Applied **Blue Team** methodology: traffic capture → analysis → triage → report

### ⚙️ Tech Stack
`Wireshark` · `Python (Scapy/PyShark)` · `TCP/IP Protocol Stack` · `PCAP Analysis`

### 🔗 [→ View Task 3 Folder](./DeCodeLabs%20-%20Task%203/)

---

## Task 4 — System Vulnerability Audit & Hardening

> **Domain:** Endpoint Security / Blue Teaming · **Stack:** Windows 11, PowerShell

A hands-on security audit and hardening engagement performed on a live Windows 11 workstation — identifying misconfigurations, scoring them with CVSS v4.0, and remediating them via PowerShell.

### 🎯 What It Does
- Audited a live **Windows 11 workstation** for security misconfigurations
- Identified and scored vulnerabilities using **CVSS v4.0** metrics
- Hardened **identity controls**: password length, password history, account policies
- Audited **local administrator group** membership and privilege levels
- Verified **BitLocker disk encryption** status and documented remediation plan
- Confirmed **Windows Defender Firewall** active across all network profiles
- Documented all findings in a professional **Vulnerability Report (PDF + DOCX)**

### 🔍 Findings Summary

| Vulnerability | CVSS v4.0 | Status |
|:---|:---:|:---|
| Weak Password Length (Min: 0) | **5.3** | ✅ Hardened to 8 chars |
| Password History Disabled | **4.0** | ✅ Set to remember 5 passwords |
| BitLocker Encryption Disabled | **7.5** | 📄 Documented & Planned |

### ⚙️ Tech Stack
`Windows 11` · `PowerShell` · `BitLocker` · `Windows Defender Firewall` · `CVSS v4.0`

### 🔗 [→ View Task 4 Folder](./DeCodeLabs%20-%20Task%204/)

---

## 🛠️ Technologies Used

| Category | Tools & Technologies |
|:---|:---|
| **Languages** | Python 3.x, JavaScript (ES6+), HTML5, CSS3, PowerShell |
| **Security Tools** | Wireshark, HaveIBeenPwned API, BitLocker, Windows Defender |
| **Cryptography** | Shannon Entropy, Argon2id, Scrypt, Caesar, Vigenère, XOR |
| **Network** | TCP/IP, DNS, HTTP/S, ICMP, Wireshark PCAP |
| **Frameworks** | NIST CSF, OWASP, CVSS v4.0, NIST SP 800-63B |
| **Reporting** | PDF, DOCX, Markdown |

---

## 📊 Internship Summary

```
Total Projects Completed  : 4 / 4
Domains Covered           : Application Security, Cryptography,
                            Network Security, Endpoint Security
Tools Mastered            : Wireshark, Python, PowerShell, Web APIs
Frameworks Applied        : NIST, OWASP, CVSS v4.0
Report Format             : PDF + DOCX + GitHub README
```

---

## 👤 Author

**Abdul Rahman**
Cybersecurity Analyst Intern — DeCode Labs, Batch 2026

[![GitHub](https://img.shields.io/badge/GitHub-Abdxlrahman-181717?style=flat&logo=github)](https://github.com/Abdxlrahman)

---

<div align="center">

*DeCode Labs Cybersecurity Internship | Batch 2026 | All 4 Projects Completed*

</div>
