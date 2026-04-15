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


if choice == "encrypt":
    result = encrypt(message)
    print("\nEncrypted message:", result)
elif choice == "decrypt":
    result = decrypt(message)
    print("\nDecrypted message:", result)
else:
        print("Please choose either 'encrypt' or 'decrypt'.")


if __name__ == "__main__":
    main()


