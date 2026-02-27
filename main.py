import cloudscraper
from colorama import Fore, init

init(autoreset=True)

def check_website_status(url, name):
    scraper = cloudscraper.create_scraper(
        browser={
            'browser': 'chrome',
            'platform': 'windows',
            'desktop': True
        }
    )
    
    try:
        response = scraper.get(url, timeout=15)
        
        if response.status_code == 200:
            print(f"[{name:12}] {Fore.GREEN}ONLINE")
        else:
            desc = get_error_description(response.status_code)
            print(f"[{name:12}] {Fore.RED}OFFLINE - Status: {response.status_code} ({desc})")
    
    except Exception as e:
        print(f"[{name:12}] {Fore.RED}Fehler: Verbindung fehlgeschlagen")

def get_error_description(code):
    error_descriptions = {
        400: "Bad Request",
        401: "Unauthorized",
        403: "Forbidden (Cloudflare Block?)",
        404: "Not Found",
        429: "Too Many Requests",
        500: "Internal Server Error",
        503: "Service Unavailable (Wartungsmodus)",
        520: "Web server is returning an unknown error (Cloudflare)",
        521: "Web server is down (Cloudflare)",
    }
    return error_descriptions.get(code, "Unbekannter Fehler")

sites = [
    ("DDL-Warez", "https://ddl-warez.cc/"),
    ("Filmfans", "https://filmfans.org/"),
    ("Serienfans", "https://serienfans.org/"),
    ("Byte", "https://byte.to/"),
    ("DDownload", "https://ddownload.com/"),
    ("1fichier", "https://1fichier.com/"),
    ("Rapidgator", "https://rapidgator.net/"),
    ("NOX.TV", "https://nox.to/"),
    ("DLPSGAME", "https://dlpsgame.com/"),
    ("IGG-GAMES", "https://igg-games.com/"),
]

print(f"{'SITE':<14} | STATUS")
print("-" * 25)

for name, url in sites:
    check_website_status(url, name)
