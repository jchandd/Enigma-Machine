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
    return text.strip()


def encrypt(data):
    text = data["message"]
    shift = data["shift"] % 26  # keep shift within alphabet range
    result = ""

    for char in text:
        if char.islower():
            result += chr((ord(char) - 97 + shift) % 26 + 97)
        elif char.isupper():
            result += chr((ord(char) - 65 + shift) % 26 + 65)
        else:
            result += char

    return result


def decrypt(data):
    # Do NOT modify original shift permanently
    new_data = {
        "message": data["message"],
        "shift": -data["shift"]
    }
    return encrypt(new_data)


def main():
    choice = input("Encrypt or decrypt? (encrypt/decrypt): ").strip().lower()
    message = input("Enter your message: ")
    
    # Handle invalid shift input safely
    try:
        shift = int(input("Enter shift value: "))
    except ValueError:
        print("Shift must be a number.")
        return

    message = format_text(message)

    data = {  # Use a dictionary to pass data to functions
        "message": message,
        "shift": shift
    }

    if choice == "encrypt":
        print("\nEncrypted message:", encrypt(data))
    elif choice == "decrypt":
        print("\nDecrypted message:", decrypt(data))
    else:
        print("Invalid choice. Please type 'encrypt' or 'decrypt'.")


if __name__ == "__main__":
    main()
