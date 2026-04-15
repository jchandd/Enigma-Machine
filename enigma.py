# Ceaser Cipher Program


# PSEUDOCODE
# Ask user to encrypt or decrypt
# Ask for message
# Clean message
# If encrypt → call encrypt function
# If decrypt → call decrypt function
# Show result


print("Caesar Cipher Program")


def format_text(text):
    # Removes extra spaces
    return text.strip()


def encrypt(data): # using dictionnary
    text = data["message"]
    shift = data["shift"]
    result = ""

    for char in text:
        if char.islower():
            new_char = chr(
                (ord(char) - 97 + shift) % 26 + 97
            )  # ord() gives the ASCII value of the character, we shift it, and then convert back to character
            result += new_char
        elif char.isupper():  # Check if the character is an uppercase letter
            new_char = chr(
                (ord(char) - 65 + shift) % 26 + 65
            )  # Similar to the lowercase case, but we use 65 for uppercase letters
            result += new_char
        else:
            result += char
    return result


def decrypt(data): # using dictionnary
    data["shift"] = -data["shift"] # We can simply negate the shift to decrypt, since the Caesar cipher is symmetric. This way, we can reuse the encrypt function for decryption.
    return encrypt(data)





def main():
    choice = input("Do you want to encrypt or decrypt a message? (Type 'encrypt' or 'decrypt'): ").lower()
    message = input("Enter your message: ")
    shift = int(input("Enter the shift value (number of positions to shift): "))

  # Clean Inputs
choice = choice.strip().lower()
message = format_text(message)

print("\nYou entered:", message)

# Code for storing data in a dictionary
data = {
    "message": message,
    "shift": shift
}

if choice == "encrypt":
    result = encrypt(data)
    print("\nEncrypted message:", result)
elif choice == "decrypt":
    result = decrypt(data)
    print("\nDecrypted message:", result)
else:
    print("Please choose either 'encrypt' or 'decrypt'.")



if __name__ == "__main__":
    main()


