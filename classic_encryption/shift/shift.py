from items.text import Text

class Shift:
    def __init__(self, key):
        self.key = key

    def encrypt(self, text_object):
        numbers_list = text_object.letters_to_numbers()
        encrypted_numbers = [(number + self.key) % 26 for number in numbers_list]
        encrypted_text = Text.numbers_to_letters(encrypted_numbers)
        return encrypted_text

    def decrypt(self, encrypted_text):
        numbers_list = encrypted_text.letters_to_numbers()
        decrypted_numbers = [(number - self.key) % 26 for number in numbers_list]
        decrypted_text = Text.numbers_to_letters(decrypted_numbers)
        return decrypted_text