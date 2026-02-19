# Username Brute Force Tool (pwntools Version)

## 📌 Overview

This project is a Python-based multi-threaded username/password brute-force script built using pwntools.  
It is intended for educational purposes and authorized penetration testing labs such as TryHackMe or HackTheBox.

---

## 🛠 Requirements

- Python 3.8+
- pwntools
- SecLists (for wordlists)
- Linux/Kali recommended

---

## 🚀 Setup & Installation

### 1️⃣ Check Python Version

python3 --version


Make sure you are using Python 3.8 or higher.

---

### 2️⃣ Create Virtual Environment (Recommended)

python3 -m venv venv
source venv/bin/activate


Using a virtual environment is recommended for Kali/Linux systems.

---

### 3️⃣ Install pwntools

If you have a `requirements.txt` file:

pip install -r requirements.txt


Or install directly:

pip install pwntools


### Verify Installation

python3 -c "from pwn import remote; print('pwntools working')"


If no error appears, installation is successful ✅

---

## ⚙️ Configure Script Settings

Open your script file and verify:

```python
target_ip = "10.10.98.190"
target_port = 8000
wordlist = "/usr/share/seclists/Passwords/500-worst-passwords.txt"

Make sure:

    Target IP is reachable

    Target port is correct

    Wordlist file exists

Check Wordlist Path

ls /usr/share/seclists/Passwords/500-worst-passwords.txt

If not installed:

sudo apt install seclists

▶️ Run the Script

python3 username_brute.py

Or make it executable:

chmod +x username_brute.py
./username_brute.py

🔥 Common Errors & Fixes
❌ ModuleNotFoundError: No module named 'pwn'

Solution:

pip install pwntools

❌ Connection Refused

Possible reasons:

    Target machine is down

    Wrong port number

    Firewall blocking connection

Check connectivity:

nc -nv 10.10.98.190 8000

❌ Timeout Issues

You may need to increase timeout inside the script:

r.recvline(timeout=1)

Increase the timeout value if network latency is high.
⚠️ Important Notice

This tool must only be used in:

    TryHackMe labs

    HackTheBox labs

    Your own lab environment

    Authorized penetration testing engagements

Do NOT use this tool on systems or networks without explicit permission.
📜 Disclaimer

This project is created strictly for educational and authorized security testing purposes. The author is not responsible for misuse of this tool.
