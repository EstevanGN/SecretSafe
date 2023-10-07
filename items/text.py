class Text:
    def __init__(self, input_string):
        self.input_string = input_string

    def letters_to_numbers(self):
        number_list = []
        for char in self.input_string:
            if char.isalpha():
                char_lower = char.lower()
                number = ord(char_lower) - ord('a')
                number_list.append(number)
        return number_list

    @staticmethod
    def numbers_to_letters(number_list):
        letter_list = []
        for number in number_list:
            if 0 <= number <= 25:
                char = chr(number + ord('a'))
                letter_list.append(char)
        return ''.join(letter_list)