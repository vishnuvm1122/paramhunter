# 🔐 Brute Force Tools (pwntools Version)

> ⚠️ For Educational & Authorized Testing Only

This repository contains two Python-based multi-threaded brute-force scripts built using **pwntools**:

- `username_brute.py`
- `password_brute.py`

Designed for:
- TryHackMe Labs
- HackTheBox Labs
- Personal lab environments
- Authorized penetration testing

---

## 📌 Features

- Remote TCP connection handling
- Multi-threading support
- Wordlist automation (SecLists)
- Response-based authentication detection
- Lightweight and easy to configure

---

## 🛠 Requirements

- Python 3.8+
- pwntools
- SecLists wordlists
- Linux / Kali Linux (Recommended)

---

## 🚀 Installation

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/yourusername/bruteforce-tools.git
cd bruteforce-tools

2️⃣ Create Virtual Environment (Recommended)

python3 -m venv venv
source venv/bin/activate

3️⃣ Install Dependencies

pip install pwntools

Or if using requirements.txt:

pip install -r requirements.txt

⚙️ Configuration

Open the script and modify:

target_ip = "10.10.98.190"
target_port = 8000
wordlist = "/usr/share/seclists/Passwords/500-worst-passwords.txt"

Make sure:

    Target IP is reachable

    Target port is correct

    Wordlist exists

📂 Install SecLists (If Not Installed)

sudo apt install seclists

Verify:

ls /usr/share/seclists/Passwords/500-worst-passwords.txt

▶️ Usage
Run Username Brute Force

python3 username_brute.py

Run Password Brute Force

python3 password_brute.py

🔥 Common Errors
❌ ModuleNotFoundError: No module named 'pwn'

pip install pwntools

❌ Connection Refused

Possible Causes:

    Target machine is down

    Wrong port

    Firewall blocking

Test connection:

nc -nv 10.10.98.190 8000

❌ Timeout Issues

Increase timeout inside script:

r.recvline(timeout=2)

⚠️ Legal Disclaimer

This project is strictly for:

    Educational purposes

    Authorized security testing

    Lab environments

Unauthorized use against systems without explicit permission is illegal.

The author is not responsible for misuse of this tool.
