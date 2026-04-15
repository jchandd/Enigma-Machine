# Ceaser Cipher Program


# PSEUDOCODE
# Ask user to encrypt or decrypt
# Ask for message
# Clean message
# If encrypt → call encrypt function
# If decrypt → call decrypt function
# Show result


print("Caesar Cipher Program")

SHIFT = 3  # fixed Caesar shift


def format_text(text):
    return text.strip()


def encrypt(message):
    result = ""

    for char in message:
        if char.islower():
            result += chr((ord(char) - 97 + SHIFT) % 26 + 97)
        elif char.isupper():
            result += chr((ord(char) - 65 + SHIFT) % 26 + 65)
        else:
            result += char

    return result


def decrypt(message):
    result = ""

    for char in message:
        if char.islower():
            result += chr((ord(char) - 97 - SHIFT) % 26 + 97)
        elif char.isupper():
            result += chr((ord(char) - 65 - SHIFT) % 26 + 65)
        else:
            result += char

    return result


def main():
    choice = input("Encrypt or decrypt? (encrypt/decrypt): ").strip().lower()
    message = format_text(input("Enter your message: "))

    if choice == "encrypt":
        print("\nEncrypted message:", encrypt(message))
    elif choice == "decrypt":
        print("\nDecrypted message:", decrypt(message))
    else:
        print("Invalid choice.")


if __name__ == "__main__":
    main()
