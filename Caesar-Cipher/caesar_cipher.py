class CaesarCipher:
    def __init__(self):
        # Initialize the alphabet
        self.LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        
    def encrypt(self, message, shift):
        """Encrypt a message using Caesar Cipher"""
        encrypted_text = ''
        
        for char in message:
            if char.isalpha():
                # Determine the case and base alphabet
                is_upper = char.isupper()
                char_idx = self.LETTERS.find(char.upper())
                
                # Calculate new position with shift
                new_idx = (char_idx + shift) % 26
                new_char = self.LETTERS[new_idx]
                
                # Preserve original case
                encrypted_text += new_char if is_upper else new_char.lower()
            else:
                # Preserve non-alphabetic characters
                encrypted_text += char
                
        return encrypted_text
    
    def decrypt(self, message, shift):
        """Decrypt a message using Caesar Cipher"""
        # Decryption is just encryption with negative shift
        return self.encrypt(message, -shift)
    
    def show_all_possibilities(self, message):
        """Show all possible shift combinations"""
        results = []
        for shift in range(26):
            decrypted = self.decrypt(message, shift)
            results.append(f"Shift {shift}: {decrypted}")
        return results

def main():
    cipher = CaesarCipher()
    
    while True:
        print("\n=== Caesar Cipher Encryption/Decryption ===")
        print("1. Encrypt a message")
        print("2. Decrypt a message")
        print("3. Show all possible decryptions")
        print("4. Exit")
        
        choice = input("\nEnter your choice (1-4): ").strip()
        
        if choice == '4':
            print("\nGoodbye!")
            break
            
        if choice not in ['1', '2', '3']:
            print("\nInvalid choice! Please select 1, 2, 3, or 4.")
            continue
            
        # Get the message
        message = input("\nEnter the message: ")
        
        if choice in ['1', '2']:
            # Get and validate shift value
            while True:
                try:
                    shift = int(input("Enter the shift value (1-25): "))
                    if 1 <= shift <= 25:
                        break
                    else:
                        print("Shift must be between 1 and 25!")
                except ValueError:
                    print("Please enter a valid number!")
            
            if choice == '1':
                result = cipher.encrypt(message, shift)
                print(f"\nEncrypted message: {result}")
            else:
                result = cipher.decrypt(message, shift)
                print(f"\nDecrypted message: {result}")
                
        else:  # Show all possibilities
            print("\nAll possible decryptions:")
            results = cipher.show_all_possibilities(message)
            for result in results:
                print(result)
        
        input("\nPress Enter to continue...")

# Run the program
if __name__ == "__main__":
    main()

# Show example usage
print("Example usage:")
cipher = CaesarCipher()
message = "Hello, World!"
shift = 3
encrypted = cipher.encrypt(message, shift)
decrypted = cipher.decrypt(encrypted, shift)

print(f"\nOriginal message: {message}")
print(f"Encrypted (shift={shift}): {encrypted}")
print(f"Decrypted: {decrypted}")