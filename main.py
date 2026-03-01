import socket
from urllib.parse import urlparse
from colorama import Fore, init

init(autoreset=True)

def check_website_status(url, name):
    try:
        parsed = urlparse(url)
        host = parsed.netloc or parsed.path

        socket.create_connection((host, 443), timeout=5).close()

        print(f"[{name:12}] {Fore.GREEN}ONLINE")

    except socket.gaierror:
        print(f"[{name:12}] {Fore.RED}OFFLINE - DNS Fehler")

    except TimeoutError:
        print(f"[{name:12}] {Fore.RED}OFFLINE - Timeout")

    except OSError:
        print(f"[{name:12}] {Fore.RED}OFFLINE - Server nicht erreichbar")


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
