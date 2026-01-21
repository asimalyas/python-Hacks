import random
import string
import time

def generate_captcha(length=6):
    chars = string.ascii_letters + string.digits
    return ''.join(random.choice(chars) for _ in range(length))

def tilt_captcha(text):
    lines = ["", "", ""]  # 3 rows for tilt effect

    for ch in text:
        tilt = random.choice([0, 1, 2])
        for i in range(3):
            if i == tilt:
                lines[i] += ch + " "
            else:
                lines[i] += "  "

    return "\n".join(lines)

attempts = 3
expiry = 30
start_time = time.time()

captcha = generate_captcha()

print("\n🔐 CAPTCHA VERIFICATION 🔐")
print("Type the CAPTCHA exactly (ignore tilt)")
print("⏱️ Expires in 30 seconds\n")

while attempts > 0:
    print("CAPTCHA:")
    print(tilt_captcha(captcha))

    user_input = input("\nEnter CAPTCHA: ")

    if time.time() - start_time > expiry:
        print("\n⏰ CAPTCHA expired! Refresh required.")
        break

    if user_input == captcha:
        print("\n✅ Verified! Human detected 😎")
        break
    else:
        attempts -= 1
        print(f"\n❌ Wrong CAPTCHA! Attempts left: {attempts}\n")
        captcha = generate_captcha()

        if attempts == 0:
            print("🚫 Access blocked!")
            print("🤖 Bot activity detected.")
