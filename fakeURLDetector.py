import re
from urllib.parse import urlparse
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

# Known URL shorteners
SHORTENERS = [
    "bit.ly", "tinyurl.com", "goo.gl", "t.co", "is.gd",
    "buff.ly", "adf.ly", "ow.ly", "cutt.ly", "shorturl.at"
]

# Trusted domains
TRUSTED_DOMAINS = [
    "google.com", "facebook.com", "github.com",
    "linkedin.com", "youtube.com", "openai.com"
]

def is_shortened(domain):
    return domain in SHORTENERS

def has_too_many_subdomains(domain):
    return len(domain.split(".")) > 3

def looks_fake(domain):
    return bool(re.search(r"[0-9]", domain))

def check_url(url):
    score = 0
    reasons = []

    parsed = urlparse(url)
    domain = parsed.netloc.lower()

    if not domain:
        return None, ["Invalid URL format"]

    if is_shortened(domain):
        score += 2
        reasons.append("Uses URL shortener")

    if has_too_many_subdomains(domain):
        score += 2
        reasons.append("Too many subdomains")

    if looks_fake(domain):
        score += 1
        reasons.append("Suspicious characters (numbers in domain)")

    if domain not in TRUSTED_DOMAINS:
        score += 1
        reasons.append("Untrusted domain")

    status = "PHISHING RISK" if score >= 3 else "LIKELY SAFE"
    return status, reasons


# --------- UI ---------
if __name__ == "__main__":
    print(Fore.CYAN + Style.BRIGHT + "\n🔗 Suspicious URL Detector")
    print(Fore.YELLOW + "⚠️ This link can steal your data in seconds 😳\n")

    url = input(Fore.WHITE + "👉 Paste URL here: ").strip()

    status, reasons = check_url(url)

    if not status:
        print(Fore.RED + "❌ Invalid URL")
        exit()

    print("\n" + Fore.MAGENTA + "🔍 Scan Result:\n")

    if status == "PHISHING RISK":
        print(Fore.RED + Style.BRIGHT + "🚨 PHISHING RISK DETECTED!")
    else:
        print(Fore.GREEN + Style.BRIGHT + "✅ LINK APPEARS SAFE")

    print(Fore.BLUE + "\n📌 Analysis:")

    for r in reasons:
        print(Fore.WHITE + " • " + r)

    print(Fore.CYAN + "\n🛡 Stay alert. Never trust links blindly.\n")


