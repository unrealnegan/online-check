import requests
from colorama import Fore, init

init(autoreset=True)

def check_website_status(url, name):
    try:
        response = requests.get(url, timeout=10)
        
        if response.status_code == 200:
            print(f"[{name}] {Fore.GREEN}ONLINE")
        else:
            print(f"[{name}] {Fore.RED}OFFLINE - Fehlercode: {response.status_code} ({get_error_description(response.status_code)})")
    
    except requests.exceptions.RequestException as e:
        print(f"[{name}] {Fore.RED}Fehler beim Überprüfen der Website: {e}")

def get_error_description(code):
    error_descriptions = {
        400: "Bad Request",
        401: "Unauthorized",
        403: "Forbidden",
        404: "Not Found",
        408: "Request Timeout",
        429: "Too Many Requests",
        500: "Internal Server Error",
        502: "Bad Gateway",
        503: "Service Unavailable",
        504: "Gateway Timeout"
    }
    return error_descriptions.get(code, "Unbekannter Fehler")

sites = [
    ("DDL-Warez", "https://ddl-warez.cc/"),
    ("Filmfans", "https://filmfans.org/"),
    ("Serienfans", "https://serienfans.org/"),
    ("Byte", "https://byte.to/"),
    ("DDownload", "https://ddownload.com/"),
    ("1fichier", "https://1fichier.com/"),
    ("Rapidgator", "https://rapidgator.net/site/index"),
]

for name, url in sites:
    check_website_status(url, name)
