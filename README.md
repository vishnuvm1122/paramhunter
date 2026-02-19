✅ Step-by-Step: Run pwntools Version

 1️⃣ Check Python Version
 python3 --version
 You need Python 3.8+

 2️⃣ Create Virtual Environment (Recommended)
 python3 -m venv venv
 source venv/bin/activate
 If you're on Kali/Linux, this is best practice.

 3️⃣ Install pwntools
 If you have requirements.txt:
 pip install -r requirements.txt
 Or install directly:
 pip install pwntools
 After install, test:
 python3 -c "from pwn import remote; print('pwntools working')"
 If no error → good ✅

 4️⃣ Check Your Script Settings
 Inside your file:
 target_ip = "10.10.98.190"
target_port = 8000
wordlist = "/usr/share/seclists/Passwords/500-worst-passwords.txt"
 Make sure:
 
 IP is reachable
 Port is correct
 Wordlist path exists
 
 Test wordlist:
 ls /usr/share/seclists/Passwords/500-worst-passwords.txt
 If not found:
 sudo apt install seclists

 5️⃣ Run the Script
 python3 username_brute.py
 OR if executable:
 chmod +x username_brute.py
 ./username_brute.py

🔥 Common Errors & Fix

 ❌ ModuleNotFoundError: No module named 'pwn'
 Solution:
 pip install pwntools

 ❌ Connection Refused
 Means:
 
 Target machine is down
 Wrong port
 Firewall blocking
 
 Check:
 nc -nv 10.10.98.190 8000

 ❌ Timeout Issues
 You may need to adjust:
 r.recvline(timeout=1)
 Increase timeout if network is slow.

⚠️ Important
Only run this against:

 TryHackMe machines
 HackTheBox labs
 Your own lab server
 Authorized pentest targets

Never random public servers.
