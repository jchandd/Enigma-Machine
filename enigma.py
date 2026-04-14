# Ceaser Cipher Program


# PSEUDOCODE
# Ask user to encrypt or decrypt
# Ask for message
# Clean message
# If encrypt → call encrypt function
# If decrypt → call decrypt function
# Show result

print("Caesar Cipher Program")

def main():
    print("Caesar Cipher Program")

    # Get user input
    choice = input("Encrypt or decrypt? ").strip().lower()
    message = input("Enter your message: ").strip()
    shift = int(input("Enter shift value: "))

    # Store in dictionary
    data = {
        "message": message,
        "shift": shift
    }

    print("\nData stored successfully!")
    print("Message:", data["message"])
    print("Shift:", data["shift"])


<<<<<<< HEAD
def format_text(text):
    # Removes extra spaces
    return text.strip()


message = format_text(message)


def encrypt(text):
    shift = 3  # You can change this value to increase or decrease the shift
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


def decrypt(text):
    shift = 3  # You can change this value to increase or decrease the shift
    result = ""

    for char in text:
        if char.islower():
            new_char = chr(
                (ord(char) - 97 - shift) % 26 + 97
            )  # Similar to encrypt, but we subtract the shift instead of adding it
            result += new_char
        elif char.isupper():  # Check if the character is an uppercase letter
            new_char = chr(
                (ord(char) - 65 - shift) % 26 + 65
            )  # Similar to the lowercase case, but we use 65 for uppercase letters
            result += new_char
        else:
            result += char
    return result


if choice == "encrypt":
    encrypted_message = encrypt(message)
    print("Encrypted message:", encrypted_message)

elif choice == "decrypt":
    decrypted_message = decrypt(message)
    print("Decrypted message:", decrypted_message)
else:
    print("Invalid choice. Please choose 'encrypt' or 'decrypt'.")
=======
if __name__ == "__main__":
    main()
>>>>>>> a7178de5b10c1efe13ac5ed86e95572f0aab76c6
