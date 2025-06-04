import requests
from colorama import Fore, init

init(autoreset=True)

def check_website_status(url, name):
    try:
        response = requests.get(url)
        
        if response.status_code == 200:
            print(f"[{name}] {Fore.GREEN}ONLINE")
        else:
            print(f"[{name}] {Fore.RED}OFFLINE")
    
    except requests.exceptions.RequestException as e:
        print(f"[{name}] {Fore.RED}Fehler beim Überprüfen der Website: {e}")

sites = [
    ("DDL-Warez", "https://ddl-warez.cc/"),
    ("Filmfans", "https://filmfans.org/"),
    ("Serienfans", "https://serienfans.org/"),
    ("Byte", "https://byte.to/"),
    ("DDownload", "https://ddownload.com/"),
]

for name, url in sites:
    check_website_status(url, name)
