# 🎣 Phishing Email Detection & Awareness System

> **Decode Labs Internship · Cyber Security Project 3**  
> An analytical investigation methodology and risk-classification framework designed to bridge the gap between human error and system security.
> 
> **Prepared by:** Abdul Rahman Abdul Aleem (Cybersecurity Intern)

---

## 📋 Project Overview
This repository hosts the investigation methodology, toolkits, and case studies developed for **Project 3: Phishing Awareness Analysis**. 

Rather than treating email security as a matter of "random clicking", this project outlines a structured approach to **Threat Identification** and forensic analysis of email headers, links, and domains. It establishes a defensive "Zero Trust Inbox" model to neutralize social engineering vectors before they compromise system boundaries.

---

## 📂 Repository Contents
```text
phishing-threat-analysis/
├── Assets/
│   └── Evidence.pdf                             # Supporting evidence / forensic analysis output
├── Report/
│   ├── DecodeLabs_Project3_Guidelines.pdf      # Original project guidelines
│   └── Phishing_Awareness_Analysis_Report.pdf   # Completed, professional internship report
├── LICENSE                                      # MIT Open-source license
├── .gitignore                                   # Standard ignore configurations
└── README.md                                    # Project documentation
```

---

## 🛠️ The Analyst's Forensic Toolkit

A professional cybersecurity analyst relies on structured intelligence to verify incoming communications. This framework leverages the following resources:

1. **Header Parsing (Google Admin Toolbox / MxToolbox)**
   * Decodes raw message headers to inspect transit paths and mail transfer agent (MTA) hops.
   * Audits security compliance protocols: **SPF (Sender Policy Framework)**, **DKIM (DomainKeys Identified Mail)**, and **DMARC**.
2. **Domain Intelligence (ICANN WHOIS / CentralOps)**
   * Uncovers domain registration dates, registrars, and ownership details.
   * Flag fresh, newly registered, or throwaway domains commonly used in campaign launches.
3. **URL Inspection (URLScan.io / CyberChef)**
   * Safely inspects and takes screenshots of destination URLs in isolated, virtual sandboxes.
   * Decodes obfuscated redirect paths and URL shorteners without exposing host environments.

---

## 🚩 The 4 Red Flags Checklist

A simple mental model to quickly evaluate incoming messages:

| Indicator | Visual Clue | Defensive Risk | Example |
| :--- | :--- | :--- | :--- |
| **Suspicious Domain** | Mispelled brand, unexpected TLD (`.xyz`, `.info`), or fake subdomains. | Look-alike domains harvest credentials via typosquatting. | `paypa1.com` instead of `paypal.com` |
| **Generic Greeting** | "Dear Customer", "Hello User", or greeting by email prefix. | Mass-mailing scripts lack database-backed personalization. | `"Dear costumer"` (often with spelling errors) |
| **Fake Links** | Hovered destination URL does not match anchor text; HTTP protocol. | Traps users into landing pages designed to grab passwords or push malware. | Text displays `microsoft.com` but hovers `login-secure-m1crosoft.com` |
| **Urgency / Threat** | "Act now", "Your account will be locked in 2 hours", "Immediate payment required". | Exploits human panic to bypass critical logical checks. | `"Warning! Secure your account immediately or access will be restricted."` |

---

## 🔬 Forensic Case Studies

### 🔍 Case Study 1: The Credential Harvester 🎣
* **Subject:** *"Secure your account"*
* **Sender/Return-Path:** `jose@monkey.org` (Return Path: `riddler.com`)
* **Analysis:** The sender masquerades as a service provider but originates from an unrelated, generic domain (`monkey.org`). The body utilizes high urgency and features a generic greeting (`"Dear you"`). The call-to-action button links to a non-validated destination designed to intercept authentication credentials.

### 🔍 Case Study 2: The Trust Exploit (DocuSign Spoof) 🤝
* **Subject:** *"Signature required 1/6/2025"*
* **Sender/Return-Path:** `andre.chacra@zg-www...`
* **Analysis:** Attempts to spoof DocuSign workflow updates to exploit trust. The greeting uses the raw recipient email address (`"Hi jose@monkey.org"`), indicating an automated list scrape. The target button redirects to a staging environment hosted on a public cloud bucket (`oortstorage.com`) to extract Microsoft/Google workspace session tokens.

### 🔍 Case Study 3: The Billing Scare (Netflix Spoof) 💳
* **Subject:** *"Update Payment Method"*
* **Sender/Return-Path:** `noreply_help...@em872.ramnet.co.za`
* **Analysis:** Plays on the fear of service interruption. The body contains spelling mistakes (`"Dear costumer,"`). The interactive anchor link points to a compromised or rogue domain (`nham24.com`) designed to collect credit card credentials, CVV codes, and billing details.

---

## 🟢 🟡 🔴 Email Risk Classification Framework

This standard operational table categorizes inbox communications and defines the corresponding action required:

| Risk Level | Visual Indicators | Required Action |
| :--- | :--- | :--- |
| **SAFE** 🟢 | Known sender, matched corporate domain, expected context, no urgent requests. | **Proceed Normally**: Safe to open, reply, and interact with contents. |
| **SUSPICIOUS** 🟡 | Unexpected external sender, slightly unusual tone, generic greeting, no obvious threats. | **Verify Independently**: Do not click links. Validate with the sender via an offline channel. |
| **PHISHING** 🔴 | Spoofed headers, mismatched domains, high-pressure urgency, malicious link destinations. | **Stop & Report**: Do not click or download. Forward to the IT Security Response team immediately. |

---

## 🛡️ "Zero Trust Inbox" Defensive Habits
* **Hover Before Clicking:** Make it a reflex to inspect target links.
* **Avoid Logins via Links:** Navigate to services by typing the address directly in your browser.
* **MFA Enablement:** Even if a credential harvester intercepts your password, Multi-Factor Authentication prevents unauthorized session logins.
* **Report, Don't Just Delete:** Reporting threats ensures security teams can blacklist malicious IPs and domains globally to protect the entire network.

---

*Project completed as part of the Decode Labs Cyber Security Internship Portfolio.*
