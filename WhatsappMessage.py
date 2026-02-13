import pywhatkit as kit

# Phone number with country code 
phone_number = "+91 9257864310"  # Replace with the recipient's phone number
message = "Hello! This message is sent using Python � By code_with_asim"

# Send instantly (opens WhatsApp Web)
kit.sendwhatmsg_instantly(phone_number, message)

print("Message sent successfully!")
