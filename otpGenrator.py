import random
import time

# For Windows terminal color support
try:
    from colorama import init, Fore, Style
    init()
except ImportError:
    # colorama not installed, fallback to plain colors
    class Fore:
        GREEN = '\033[92m'
        RED = '\033[91m'
        YELLOW = '\033[93m'
        BLUE = '\033[94m'
        CYAN = '\033[96m'
        RESET = '\033[0m'
    class Style:
        BRIGHT = '\033[1m'
        RESET_ALL = '\033[0m'

# Welcome message
print(Fore.CYAN + Style.BRIGHT + "\n🔐 Welcome to Secure Login System\n" + Style.RESET_ALL)

email = input(Fore.YELLOW + "📧 Enter your email: " + Fore.RESET)

otp = random.randint(1000, 9999)
expiry_time = time.time() + 60
attempts = 3

print(Fore.BLUE + f"\n📩 OTP has been sent to your email (Practice OTP: {otp})\n" + Fore.RESET)

while attempts > 0:
    user_otp = input(Fore.YELLOW + "🔢 Enter OTP: " + Fore.RESET)

    if time.time() > expiry_time:
        print(Fore.RED + "⏰ OTP expired. Please try again later." + Fore.RESET)
        break

    if user_otp == str(otp):
        print(Fore.GREEN + "\n🎉 Login Successful!" + Fore.RESET)
        print(Fore.CYAN + "✨ Welcome, you did it!" + Fore.RESET)
        break
    else:
        attempts -= 1
        print(Fore.RED + f"❌ Wrong OTP. Attempts left: {attempts}" + Fore.RESET)

if attempts == 0:
    print(Fore.RED + "\n🔒 Too many wrong attempts. Account temporarily locked." + Fore.RESET)
