import pygetwindow as gw
import time
from colorama import init, Fore, Style

init(autoreset=True)

last_window = ""
count = 0

# Keywords to ignore (your own dev window)
IGNORE_KEYWORDS = [
    "visual studio code",
    "activewindow.py",
    "whatsappmessage"
]

print(Fore.CYAN + Style.BRIGHT + "\n👁️  PYTHON SCREEN WATCHER STARTED\n")

while True:
    window = gw.getActiveWindow()

    if window:
        title = window.title
        title_lower = title.lower()

        # Ignore your own VS Code window
        if any(keyword in title_lower for keyword in IGNORE_KEYWORDS):
            time.sleep(1)
            continue

        if title != last_window:
            count += 1
            print(
                Fore.YELLOW + Style.BRIGHT + f"#{count}\n"
                + Fore.GREEN + "👀 Active Window Detected\n"
                + Fore.WHITE + Style.BRIGHT + f"➡️  {title}\n"
                + Fore.CYAN + "-" * 50
            )
            last_window = title

    time.sleep(1)
