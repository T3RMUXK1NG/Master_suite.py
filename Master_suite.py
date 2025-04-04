#!/usr/bin/env python3
"""
███████╗██╗░░░██╗███████╗██████╗░███████╗░█████╗░████████╗░█████╗░██████╗░
██╔════╝██║░░░██║██╔════╝██╔══██╗██╔════╝██╔══██╗╚══██╔══╝██╔══██╗██╔══██╗
█████╗░░██║░░░██║█████╗░░██████╔╝█████╗░░██║░░╚═╝░░░██║░░░██║░░██║██████╔╝
██╔══╝░░██║░░░██║██╔══╝░░██╔══██╗██╔══╝░░██║░░██╗░░░██║░░░██║░░██║██╔══██╗
███████╗╚██████╔╝███████╗██║░░██║███████╗╚█████╔╝░░░██║░░░╚█████╔╝██║░░██║
╚══════╝░╚═════╝░╚══════╝╚═╝░░╚═╝╚══════╝░╚════╝░░░░╚═╝░░░░╚════╝░╚═╝░░╚═╝

Version: MASTER SUITE 12.0 | By: Rajsaraswati Jatav
"""

import os
import sys
import json
import time
import uuid
import random
import socket
import smtplib
import sqlite3
import requests
import threading
import subprocess
from bs4 import BeautifulSoup
from datetime import datetime

# ====== [CONSTANTS] ======
class Brand:
    AUTHOR = "Rajsaraswati Jatav"
    YOUTUBE = "@growwithrajsaraswati"
    INSTAGRAM = "@official_rajsaraswati_jatav"
    VERSION = "MASTER SUITE 12.0"
    
    BANNER = f"""
    \033[1;35m
    ███╗░░░███╗░█████╗░░██████╗████████╗███████╗██████╗░  ░██████╗██╗░░░██╗██╗████████╗███████╗
    ████╗░████║██╔══██╗██╔════╝╚══██╔══╝██╔════╝██╔══██╗  ██╔════╝██║░░░██║██║╚══██╔══╝██╔════╝
    ██╔████╔██║███████║╚█████╗░░░░██║░░░█████╗░░██████╔╝  ╚█████╗░██║░░░██║██║░░░██║░░░█████╗░░
    ██║╚██╔╝██║██╔══██║░╚═══██╗░░░██║░░░██╔══╝░░██╔══██╗  ░╚═══██╗██║░░░██║██║░░░██║░░░██╔══╝░░
    ██║░╚═╝░██║██║░░██║██████╔╝░░░██║░░░███████╗██║░░██║  ██████╔╝╚██████╔╝██║░░░██║░░░███████╗
    ╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═════╝░░░░╚═╝░░░╚══════╝╚═╝░░╚═╝  ╚═════╝░░╚═════╝░╚═╝░░░╚═╝░░░╚══════╝
    
    \033[1;36m{Brand.AUTHOR} | {Brand.VERSION}
    \033[1;33mYouTube: {Brand.YOUTUBE} | Instagram: {Brand.INSTAGRAM}
    \033[0m"""

class AllTools:
    # ====== INFORMATION GATHERING ======
    INFO_GATHERING = {
        'nmap': 'nmap -sV -A -T4 {target}',
        'recon-ng': 'recon-ng -w {workspace} -m {module}',
        'theharvester': 'theHarvester -d {domain} -b all',
        'sherlock': 'sherlock {username}',
        'maltego': 'maltego',
        'spiderfoot': 'spiderfoot -l 127.0.0.1:5001',
        'osint': 'python3 osint.py {target}',
        'dnsenum': 'dnsenum {domain}',
        'fierce': 'fierce --domain {domain}',
        'whois': 'whois {domain}'
    }

    # ====== VULNERABILITY ANALYSIS ======
    VULN_ANALYSIS = {
        'nikto': 'nikto -h {target}',
        'openvas': 'openvas-start',
        'nessus': 'nessus',
        'lynis': 'lynis audit system',
        'golismero': 'golismero scan {target}',
        'vuls': 'vuls scan',
        'trivy': 'trivy fs --security-checks vuln ./',
        'wpscan': 'wpscan --url {target}',
        'joomscan': 'joomscan -u {target}',
        'droopescan': 'droopescan scan drupal -u {target}'
    }

    # ====== WEB APPLICATION TOOLS ======
    WEB_APPS = {
        'burpsuite': 'burpsuite',
        'zap': 'owasp-zap',
        'sqlmap': 'sqlmap -u "{url}" --batch',
        'commix': 'commix --url={url}',
        'xsstrike': 'python3 xsstrike.py -u {url}',
        'wafw00f': 'wafw00f {target}',
        'whatweb': 'whatweb {target}',
        'dirb': 'dirb {url}',
        'gobuster': 'gobuster dir -u {url} -w {wordlist}',
        'ffuf': 'ffuf -u {url}/FUZZ -w {wordlist}'
    }

    # ====== DATABASE TOOLS ======
    DATABASE = {
        'sqlmate': 'sqlmate --url {url}',
        'dbpwaudit': 'dbpwaudit -s {server} -d {database}',
        'sqlninja': 'sqlninja -m {mode} -t {target}',
        'jsql': 'java -jar jsql-injection.jar',
        'mongoaudit': 'mongoaudit -t {target}',
        'redis': 'redis-cli -h {host}'
    }

    # ====== PASSWORD ATTACKS ======
    PASSWORD = {
        'hydra': 'hydra -l {user} -P {wordlist} {service}://{target}',
        'john': 'john --wordlist={wordlist} {hashfile}',
        'hashcat': 'hashcat -m {mode} -a 0 {hashfile} {wordlist}',
        'medusa': 'medusa -h {target} -u {user} -P {wordlist} -M {module}',
        'crunch': 'crunch {min} {max} {charset} -o {output}',
        'cewl': 'cewl {url} -w {wordlist}',
        'patator': 'patator {module} host={target} user={user} password=FILE0 0={wordlist}',
        'ncrack': 'ncrack -U {userlist} -P {wordlist} {target}',
        'hashid': 'hashid {hash}',
        'rainbowcrack': 'rcrack {rt} -h {hash}'
    }

    # ====== WIRELESS TOOLS ======
    WIRELESS = {
        'aircrack': 'aircrack-ng {capture}',
        'reaver': 'reaver -i {interface} -b {bssid}',
        'wifite': 'wifite',
        'kismet': 'kismet',
        'wifiphisher': 'wifiphisher',
        'bully': 'bully {bssid}',
        'pixiewps': 'pixiewps -e {pke} -r {pkr} -s {e-hash} -z {e-nonce}',
        'hcxdumptool': 'hcxdumptool -i {interface} -o {output}',
        'hcxtools': 'hcxpcaptool -z {output} {input}',
        'wireshark': 'wireshark'
    }

    # ====== EXPLOITATION TOOLS ======
    EXPLOITATION = {
        'metasploit': 'msfconsole',
        'exploitdb': 'searchsploit {term}',
        'beef': 'beef-xss',
        'armitage': 'armitage',
        'routersploit': 'rsf',
        'setoolkit': 'setoolkit',
        'socialfish': 'python SocialFish.py',
        'phishery': 'phishery -u {url}',
        'evilginx': 'evilginx',
        'gophish': 'gophish'
    }

    # ====== POST EXPLOITATION ======
    POST_EXPLOIT = {
        'mimikatz': 'mimikatz',
        'bloodhound': 'bloodhound',
        'empire': 'powershell-empire',
        'crackmapexec': 'crackmapexec {protocol} {target}',
        'responder': 'responder -I {interface}',
        'impacket': 'python3 {script}.py {target}',
        'pupy': 'pupy',
        'powersploit': 'powersploit',
        'weevely': 'weevely generate {password} {output}',
        'shellter': 'shellter'
    }

    # ====== FORENSICS TOOLS ======
    FORENSICS = {
        'autopsy': 'autopsy',
        'volatility': 'volatility -f {image} {plugin}',
        'binwalk': 'binwalk {file}',
        'foremost': 'foremost -i {file}',
        'scalpel': 'scalpel {file}',
        'bulk_extractor': 'bulk_extractor {file}',
        'guymager': 'guymager',
        'dcfldd': 'dcfldd if={input} of={output}',
        'testdisk': 'testdisk',
        'photorec': 'photorec'
    }

    # ====== STRESS TESTING ======
    STRESS_TEST = {
        'slowloris': 'slowloris -dns {target}',
        'goldeneye': 'goldeneye {url}',
        'thc-ssl-dos': 'thc-ssl-dos {target} {port}',
        'hping3': 'hping3 --flood --rand-source {target}',
        'slowhttptest': 'slowhttptest -u {url}',
        'torshammer': 'python torshammer.py -t {target}',
        'rudy': 'python rudy.py {url}',
        'ddosim': 'ddosim',
        'hoic': 'hoic',
        'loic': 'loic'
    }

    # ====== PRIVACY TOOLS ======
    PRIVACY = {
        'tor': 'tor',
        'proxychains': 'proxychains {command}',
        'anonsurf': 'anonsurf start',
        'i2p': 'i2prouter',
        'tails': 'tails',
        'whonix': 'whonix',
        'kali': 'kali',
        'parrot': 'parrot',
        'qubes': 'qubes',
        'vpn': 'openvpn {config}'
    }

    # ====== HARDWARE HACKING ======
    HARDWARE = {
        'arduino': 'arduino',
        'facedancer': 'facedancer',
        'buspirate': 'buspirate',
        'chipsec': 'chipsec_main',
        'flashrom': 'flashrom',
        'sigrok': 'sigrok',
        'uhd': 'uhd',
        'gnuradio': 'gnuradio-companion',
        'sdr': 'rtl-sdr',
        'hackrf': 'hackrf'
    }

    # ====== AI/ML TOOLS ======
    AI_TOOLS = {
        'deepfake': 'python deepfake.py',
        'voiceclone': 'python voice_clone.py',
        'nlp': 'python nlp_phishing.py',
        'facedetect': 'python face_detection.py',
        'gantool': 'python gan_tool.py',
        'stylegan': 'python stylegan.py',
        'deepdream': 'python deepdream.py',
        'textgen': 'python text_generation.py',
        'sentiment': 'python sentiment_analysis.py',
        'objdetect': 'python object_detection.py'
    }

    # ====== MOBILE TOOLS ======
    MOBILE = {
        'apktool': 'apktool d {apk}',
        'dex2jar': 'd2j-dex2jar {dex}',
        'jadx': 'jadx {apk}',
        'frida': 'frida-ps -U',
        'objection': 'objection explore',
        'mobsf': 'mobsf',
        'androbugs': 'python androbugs.py -f {apk}',
        'qark': 'python qark.py',
        'drozer': 'drozer',
        'apkleaks': 'apkleaks -f {apk}'
    }

    # ====== TUNNELING SERVICES ======
    TUNNELS = {
        'ngrok': './ngrok http {port}',
        'cloudflared': 'cloudflared tunnel --url http://localhost:{port}',
        'serveo': 'ssh -R 80:localhost:{port} serveo.net',
        'localhost.run': 'ssh -R 80:localhost:{port} ssh.localhost.run',
        'pagekite': 'pagekite.py {port} yourname.pagekite.me',
        'localtunnel': 'lt --port {port}',
        'inlets': 'inlets client --remote=your-remote --upstream=http://localhost:{port}',
        'zrok': 'zrok share http://localhost:{port}',
        'teleport': 'teleport start --roles=node --token=your-token --auth-server=your-auth-server',
        'chisel': 'chisel server --port 8080 --reverse'
    }

    # ====== SYSTEM TOOLS ======
    SYSTEM = {
        'adb': 'adb devices',
        'fastboot': 'fastboot devices',
        'dd': 'dd if={input} of={output}',
        'gdb': 'gdb {binary}',
        'strace': 'strace {command}',
        'ltrace': 'ltrace {command}',
        'radare2': 'r2 {binary}',
        'ghidra': 'ghidra',
        'ida': 'ida',
        'ollydbg': 'ollydbg'
    }

# ====== [CORE FUNCTIONALITY] ======
class MasterSuite:
    def __init__(self):
        self.version = Brand.VERSION
        self.session_id = f"RSJ-{uuid.uuid4().hex[:8].upper()}"
        self.db_file = "master_suite.db"
        
        self.setup_environment()
        self.initialize_database()
    
    def setup_environment(self):
        """Create required directories"""
        dirs = [
            'tools', 'logs', 'results', 'wordlists', 'payloads',
            'exploits', 'reports', 'captures', 'downloads', 'screenshots',
            'databases', 'backups', 'scripts', 'binaries', 'temp'
        ]
        for d in dirs:
            os.makedirs(d, exist_ok=True)
    
    def initialize_database(self):
        """Setup SQLite database"""
        conn = sqlite3.connect(self.db_file)
        cursor = conn.cursor()
        
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS tools (
            id TEXT PRIMARY KEY,
            name TEXT,
            category TEXT,
            installed INTEGER DEFAULT 0,
            last_used TEXT
        )
        """)
        
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS sessions (
            id TEXT PRIMARY KEY,
            start_time TEXT,
            end_time TEXT,
            tool_used TEXT,
            status TEXT
        )
        """)
        
        conn.commit()
        conn.close()
    
    def show_banner(self):
        """Display awesome banner"""
        os.system('clear' if os.name == 'posix' else 'cls')
        print(Brand.BANNER)
    
    def main_menu(self):
        """Ultimate interactive menu"""
        self.show_banner()
        
        while True:
            print(f"""
\033[1;36mMain Menu:\033[0m
1. Information Gathering Tools
2. Vulnerability Analysis Tools
3. Web Application Tools
4. Database Tools
5. Password Attacks
6. Wireless Tools
7. Exploitation Tools
8. Post Exploitation
9. Forensics Tools
10. Stress Testing
11. Privacy Tools
12. Hardware Hacking
13. AI/ML Tools
14. Mobile Tools
15. Tunneling Services
16. System Tools
17. Exit
            """)
            
            choice = input("\033[1;33m[?] Select category: \033[0m").strip()
            
            if choice == "1":
                self.show_tools("Information Gathering", AllTools.INFO_GATHERING)
            elif choice == "2":
                self.show_tools("Vulnerability Analysis", AllTools.VULN_ANALYSIS)
            elif choice == "3":
                self.show_tools("Web Application", AllTools.WEB_APPS)
            elif choice == "4":
                self.show_tools("Database", AllTools.DATABASE)
            elif choice == "5":
                self.show_tools("Password Attacks", AllTools.PASSWORD)
            elif choice == "6":
                self.show_tools("Wireless", AllTools.WIRELESS)
            elif choice == "7":
                self.show_tools("Exploitation", AllTools.EXPLOITATION)
            elif choice == "8":
                self.show_tools("Post Exploitation", AllTools.POST_EXPLOIT)
            elif choice == "9":
                self.show_tools("Forensics", AllTools.FORENSICS)
            elif choice == "10":
                self.show_tools("Stress Testing", AllTools.STRESS_TEST)
            elif choice == "11":
                self.show_tools("Privacy", AllTools.PRIVACY)
            elif choice == "12":
                self.show_tools("Hardware Hacking", AllTools.HARDWARE)
            elif choice == "13":
                self.show_tools("AI/ML", AllTools.AI_TOOLS)
            elif choice == "14":
                self.show_tools("Mobile", AllTools.MOBILE)
            elif choice == "15":
                self.show_tools("Tunneling", AllTools.TUNNELS)
            elif choice == "16":
                self.show_tools("System", AllTools.SYSTEM)
            elif choice == "17":
                self.exit_tool()
                break
            else:
                print("\033[1;31m[✗] Invalid option\033[0m")
    
    def show_tools(self, category_name, tools_dict):
        """Show tools in a category"""
        while True:
            print(f"\n\033[1;36m{category_name} Tools:\033[0m")
            for i, (name, cmd) in enumerate(tools_dict.items(), 1):
                status = "\033[1;32m[✓]\033[0m" if self.check_tool_installed(cmd) else "\033[1;31m[✗]\033[0m"
                print(f"{i}. {name.title()} {status}")
            
            print("\n0. Back to Main Menu")
            choice = input("\n\033[1;33m[?] Select tool: \033[0m").strip()
            
            if choice == "0":
                break
            elif choice.isdigit() and 0 < int(choice) <= len(tools_dict):
                tool_name = list(tools_dict.keys())[int(choice)-1]
                self.manage_tool(tool_name, tools_dict[tool_name], category_name)
            else:
                print("\033[1;31m[✗] Invalid tool\033[0m")
    
    def manage_tool(self, tool_name, tool_cmd, category):
        """Manage tool installation/execution"""
        while True:
            print(f"\n\033[1;36m{tool_name.title()} Management:\033[0m")
            print("1. Install Tool")
            print("2. Run Tool")
            print("3. View Documentation")
            print("4. Back")
            
            choice = input("\n\033[1;33m[?] Select option: \033[0m").strip()
            
            if choice == "1":
                self.install_tool(tool_name, tool_cmd, category)
            elif choice == "2":
                self.run_tool(tool_name, tool_cmd, category)
            elif choice == "3":
                self.show_documentation(tool_name)
            elif choice == "4":
                break
            else:
                print("\033[1;31m[✗] Invalid option\033[0m")
    
    def install_tool(self, tool_name, tool_cmd, category):
        """Install tool"""
        print(f"\n\033[1;33m[+] Installing {tool_name}...\033[0m")
        
        # Tool-specific installation
        if tool_name == 'metasploit':
            os.system('pkg install metasploit')
        elif tool_name == 'burpsuite':
            os.system('pkg install burpsuite')
        elif tool_name == 'wireshark':
            os.system('pkg install wireshark')
        else:
            # Generic installation for most tools
            os.system(f'pkg install {tool_name} || pip install {tool_name}')
        
        # Update database
        conn = sqlite3.connect(self.db_file)
        cursor = conn.cursor()
        cursor.execute("""
        INSERT OR REPLACE INTO tools VALUES (?, ?, ?, 1, ?)
        """, (tool_name, tool_name, category, datetime.now().isoformat()))
        conn.commit()
        conn.close()
        
        print("\033[1;32m[✓] Installation complete\033[0m")
    
    def run_tool(self, tool_name, tool_cmd, category):
        """Run tool"""
        if not self.check_tool_installed(tool_cmd):
            print("\033[1;31m[✗] Tool not installed\033[0m")
            return
        
        # Record session
        conn = sqlite3.connect(self.db_file)
        cursor = conn.cursor()
        cursor.execute("""
        INSERT INTO sessions VALUES (?, ?, ?, ?, ?)
        """, (
            self.session_id,
            datetime.now().isoformat(),
            "",
            tool_name,
            "running"
        ))
        conn.commit()
        conn.close()
        
        # Execute tool
        print(f"\n\033[1;33m[+] Running {tool_name}...\033[0m")
        os.system(tool_cmd)
    
    def check_tool_installed(self, tool_cmd):
        """Check if tool is installed"""
        tool_name = tool_cmd.split()[0]
        return os.system(f"which {tool_name} > /dev/null") == 0
    
    def show_documentation(self, tool_name):
        """Display tool documentation"""
        docs = {
            'nmap': "Network mapper - https://nmap.org/book/man.html",
            'metasploit': "Exploitation framework - https://www.metasploit.com/help",
            'sqlmap': "SQL injection tool - https://github.com/sqlmapproject/sqlmap/wiki"
        }
        
        print(f"\n\033[1;36m{tool_name.title()} Documentation:\033[0m")
        print(docs.get(tool_name, "Documentation not available. Try 'man {tool_name}' or '--help'"))
    
    def exit_tool(self):
        """Clean exit"""
        # Update session status
        conn = sqlite3.connect(self.db_file)
        cursor = conn.cursor()
        cursor.execute("""
        UPDATE sessions SET end_time = ?, status = ? WHERE id = ?
        """, (datetime.now().isoformat(), "completed", self.session_id))
        conn.commit()
        conn.close()
        
        print(f"\n\033[1;32m[✓] Follow for more tools:")
        print(f"YouTube: {Brand.YOUTUBE}")
        print(f"Instagram: {Brand.INSTAGRAM}\033[0m")
        sys.exit(0)

if __name__ == "__main__":
    try:
        suite = MasterSuite()
        suite.main_menu()
    except KeyboardInterrupt:
        print("\n\033[1;33m[!] Interrupted\033[0m")
        sys.exit(0)
    except Exception as e:
        print(f"\n\033[1;31m[✗] Fatal error: {str(e)}\033[0m")
        sys.exit(1)
