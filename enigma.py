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


def get_choice():
    while True:
        choice = input("Encrypt or decrypt? (encrypt/decrypt): ").strip().lower()
        if choice == "encrypt" or choice == "decrypt":
            return choice
        else:
            print("Invalid choice. Please type 'encrypt' or 'decrypt'.")


def main():
    while True:
        choice = get_choice()
        message = format_text(input("Enter your message: "))

        if choice == "encrypt":
            print("\nEncrypted message:", encrypt(message))
        else:
            print("\nDecrypted message:", decrypt(message))

        again = input("\nDo you want to run again? (y/n): ").strip().lower()
        if again != "y":
            print("Goodbye!")
            break


if __name__ == "__main__":
    main()
