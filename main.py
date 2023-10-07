from items.text import Text
from classic_encryption.shift.shift import Shift

class Main:

    @staticmethod
    def shift():
        print("\nWelcome to shift encryption")
        shift_choose = int(input("1. Encrypt.\n2. Decrypt.\n"))
        if shift_choose == 1:
            input_text = input("Enter the text to encrypt: ")
            input_key = int(input("Enter the shift key (between 0 and 25): "))
            text_object = Text(input_text)

            # Encrypt the text
            shift_cipher = Shift(input_key)
            encrypted_text = shift_cipher.encrypt(text_object)
            print("Encrypted text: ", encrypted_text)
        elif shift_choose == 2:
            input_text = input("Enter the text to decrypt: ")
            input_key = int(input("Enter the shift key (between 0 and 25): "))
            text_object = Text(input_text)

            # Decrypt the text
            shift_cipher = Shift(input_key)
            encrypted_text = shift_cipher.decrypt(text_object)
            print("Decrypted text: ", encrypted_text)


    @staticmethod
    def execute():
        print("# ####################### #")
        print("# Welcome to SecretSafe #")
        print("# ####################### #\n")

        while True:
            try:
                print("\nThe following are the possible encryption methods:")
                print("1. Shift.")
                print("2. Multiplicative.")
                print("3. Permutation.")
                print("4. Vigenere.")
                # Read an integer input from the user
                choice = int(input("Enter a number (1 to 4) or 0 to exit: "))
                
                # Check the input and execute corresponding method
                if choice == 1:
                    Main.shift()
                elif choice == 2:
                    print("Multiplicative")
                elif choice == 3:
                    print("Permutation")
                elif choice == 4:
                    print("Vigenere")
                elif choice == 0:
                    print("Exiting the program. Goodbye!")
                    break  # Exit the loop and end the program
                else:
                    print("\nInvalid choice. Please enter a number between 0 and 4.")
            
            except ValueError:
                print("\nInvalid input. Please enter a valid integer.")


Main.execute()