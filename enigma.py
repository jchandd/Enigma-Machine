# Ceaser Cipher Program


# PSEUDOCODE
# Ask user to encrypt or decrypt
# Ask for message
# Clean message
# If encrypt → call encrypt function
# If decrypt → call decrypt function
# Show result

print("Caesar Cipher Program")

choice = input("Would you like to encrypt or decrypt? ")
message = input("Enter your message: ")

# Clean inputs
choice = choice.strip().lower()
message = message.strip()

print("\nYou entered:", message)