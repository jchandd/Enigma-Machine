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


if __name__ == "__main__":
    main()