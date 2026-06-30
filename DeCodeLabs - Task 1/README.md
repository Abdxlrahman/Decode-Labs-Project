# 🛡️ DeCodeLabs Internship — Task 1: Password Strength Checker

**Batch:** 2026 | **Role:** Cybersecurity Analyst Intern | **Platform:** DeCodeLabs

---

## 📌 Project Overview

This is **Project 1** of the DeCodeLabs Cybersecurity Internship Program.  
The goal was to build a **Password Strength Checker** that evaluates whether a password is **Weak, Medium, or Strong** using string handling, conditional logic, and security principles.

---

## 🗂️ Folder Structure

```
DeCodeLabs - Task1/
│
├── 📁 Code/
│   ├── password_analyzer.py      ← Main Python program (CLI)
│   └── requirements.txt          ← Required Python libraries
│
├── 📁 Website/
│   ├── index.html                ← Web interface (open in browser)
│   ├── style.css                 ← Styling
│   └── script.js                 ← Password analysis logic
│
├── 📁 Word doc/
│   └── DecodeLab - Task 1.docx   ← Project documentation & report
│
└── README.md                     ← This file
```

---

## ✅ Key Requirements Completed

| Requirement | Status |
|---|---|
| Check password length | ✅ Done |
| Check uppercase letters | ✅ Done |
| Check numbers | ✅ Done |
| Check special/symbol characters | ✅ Done |
| Display Weak / Medium / Strong result | ✅ Done |

---

## 🚀 Bonus Features Added

- 🔢 **Shannon Entropy** calculation (measures true randomness)
- 💥 **HaveIBeenPwned API** — checks real breach databases
- ⏱️ **GPU Crack Time** estimator
- 🔁 Repeated character detection (`aaa`, `111`)
- 📶 Sequential pattern detection (`abc`, `123`, `qwerty`)
- 🎲 **Cryptographic Password Generator**
- 🔒 **Scrypt/Argon2id** password hashing
- 🧠 RAM scraping protection via SecureBuffer
- 📄 Export PDF Security Report

---

## 🖥️ How to Run

### Python CLI:
```bash
# Navigate to the Code directory
cd Code

# Install dependencies
pip install -r requirements.txt

# Run the program
python password_analyzer.py
```

### Website:
Just open `website/index.html` in any browser — no setup needed!

---

## 🧪 Test Results

| Test | Password | Score | Result |
|---|---|---|---|
| Test 1 | `12345ABCDE` | 0/100 | 🔴 IMMEDIATE FAIL |
| Test 2 | `pWs84e<%ST-8g=)FNy` | 100/100 | 🟢 EXCELLENT |

---

## 🛠️ Technologies Used

- **Python 3.x** — CLI tool
- **HTML5, CSS3, JavaScript** — Web interface
- **colorama** — Terminal colors
- **HaveIBeenPwned API** — Breach detection
- **Shannon Entropy Formula** — Randomness measurement

---

## 📚 References

- DeCodeLabs Internship Project 1 Guidelines (2026)
- HaveIBeenPwned API — haveibeenpwned.com
- NIST Password Guidelines — SP 800-63B
- Shannon Entropy — Information Theory

---

*DeCodeLabs Cybersecurity Internship | Project 1 | Batch 2026*
