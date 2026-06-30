# CryptoVault v2.0 PRO

**DecodeLabs Internship | Cybersecurity Analyst Program (Project 2)**

An advanced cryptography engine and cryptanalysis suite implementing symmetric ciphers, background integrity verification, client-side file encryption, and a brute-force cryptanalysis simulator.

---

## 🛠️ Architecture

* **Web UI (`index.html`)**: Glassmorphic dashboard featuring text/file encryption, brute-force dictionary matching, and PDF audit reporting.
* **CLI Engine (`python_app/`)**: Terminal-based Python utility implementing core ciphers.

### Repository Layout
```text
CryptoVault/
├── index.html          # Web Cryptography Dashboard
├── README.md           # Documentation
└── python_app/         # Python CLI Module
    ├── crypto_vault.py
    └── requirements.txt
```

---

## 🔐 Cryptographic Specifications

| Cipher | Key Type | Mechanics | Reversible |
| :--- | :--- | :--- | :---: |
| **Caesar** | Numeric Shift (1–25) | Alphabet substitution shifting | Yes |
| **Vigenère**| Keyword (Alpha) | Polyalphabetic substitution | Yes |
| **Atbash** | Keyless | Monoalphabetic reflection (A↔Z) | Yes |
| **ROT13** | Fixed (Shift 13) | Standard ROT13 rotation | Yes |
| **XOR** | Byte Key (1–255) | Bitwise logical XOR operation | Yes |
| **Reverse** | Keyless | Reversal of character sequence | Yes |

---

## 🛡️ Key Features

* **Round-Trip Integrity Verification**: Real-time validation checks (`Decrypt(Encrypt(M)) == M`) ensuring zero payload data loss.
* **Brute-Force Cryptanalysis Simulator**: Automated Caesar cipher cracking utilizing English word scoring and dictionary-based heuristics.
* **Local Processing Guarantee**: 100% client-side execution; text and files are processed in-browser without network transmission.

---

## 🚀 Execution

### Web Application
Open `index.html` in any web browser, or visit the [Live Demo](https://abdxlrahman.github.io/DecodeLabs-Task2/).

### Python CLI App
```bash
cd python_app
pip install -r requirements.txt
python crypto_vault.py
```

---
*Submitted for DecodeLabs Cybersecurity Internship — Task 2: Data Confidentiality.*
