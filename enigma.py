# Caesar Cipher Program


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
            )  # Similar to the encrypt function, but we subtract the shift instead of adding it
            result += new_char
        elif char.isupper():  # Check if the character is an uppercase letter
            new_char = chr(
                (ord(char) - 65 - shift) % 26 + 65
            )  # Similar to the lowercase case, but we use 65 for uppercase letters
            result += new_char
        else:
            result += char
    return result


def get_choice():
    return input("Would you like to encrypt or decrypt? ").strip().lower()


while True:
    choice = get_choice()
    if choice not in ["encrypt", "decrypt"]:
        print("Invalid choice. Please choose 'encrypt' or 'decrypt'.")
        continue
    message = format_text(
        input("Enter your message: ")
    )  # Clean the message by removing extra spaces
    if choice == "encrypt":
        print("\nEncrypted message:", encrypt(message))
    else:
        print("\nDecrypted message:", decrypt(message))

    again = (
        input("\nDo you want to encrypt/decrypt another message? (yes/no) ")
        .strip()
        .lower()
    )
    if again != "yes":
        print("Goodbye!")
        break
