def caesar_cipher(text, shift, mode='encrypt'):
    result = ""
    
    # Normalize the shift value to a value between 0-25
    shift = shift % 26
    
    for char in text:
        # Encrypt uppercase letters
        if char.isupper():
            if mode == 'encrypt':
                result += chr((ord(char) + shift - 65) % 26 + 65)
            elif mode == 'decrypt':
                result += chr((ord(char) - shift - 65) % 26 + 65)
        # Encrypt lowercase letters
        elif char.islower():
            if mode == 'encrypt':
                result += chr((ord(char) + shift - 97) % 26 + 97)
            elif mode == 'decrypt':
                result += chr((ord(char) - shift - 97) % 26 + 97)
        else:
            # Non-alphabetical characters are unchanged
            result += char
    
    return result

# User input for the message and shift value
message = input("Enter your message: ")
shift = int(input("Enter shift value (positive integer): "))
mode = input("Type 'encrypt' to encrypt or 'decrypt' to decrypt: ").strip().lower()  # Normalize input

# Validate the mode
if mode not in ['encrypt', 'decrypt']:
    print("Invalid mode selected. Please choose 'encrypt' or 'decrypt'.")
else:
    if mode == 'encrypt':
        encrypted_message = caesar_cipher(message, shift, 'encrypt')
        print("Encrypted Message:", encrypted_message)
    else:
        decrypted_message = caesar_cipher(message, shift, 'decrypt')
        print("Decrypted Message:", decrypted_message)
