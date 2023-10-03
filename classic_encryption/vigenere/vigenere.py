class Vigenere:
  def __init__(self, key):
    self.key_text = key

  def encrypt(self, clear_text):
    idx = 0
    encrypted_text = ""
    for c in clear_text:
      
      new_char = ((ord(c)-97) + (ord(self.key_text[idx])-97)) % 26
      encrypted_text += chr(new_char+97)
      idx +=1
      idx = idx%len(self.key_text)
    return encrypted_text

  def decrypt(self, enc_text):
    idx = 0
    decrypted_text = ""
    for c in enc_text:
      new_char = ((ord(c)-97) - (ord(self.key_text[idx])-97)) % 26
      decrypted_text += chr(new_char+97)
      idx +=1
      idx = idx%len(self.key_text)
    return decrypted_text
vig = Vigenere("hola")

print(vig.encrypt("casa"))
print(vig.decrypt(vig.encrypt("casa")))