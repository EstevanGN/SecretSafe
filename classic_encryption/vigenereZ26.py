import random
from pycipher import Vigenere
from util.transforms import Masker

def generar_clave_vigenere(longitud):
    alfabeto = 'abcdefghijklmnopqrstuvwxyz'  # Alfabeto en minúsculas
    return ''.join(random.choice(alfabeto) for _ in range(longitud))

text = input("De el texto para cifrar: ")
plaintext, masker = Masker.from_text(text)
long_clave = int(input("De qué longitud quiere la clave: "))
clave = generar_clave_vigenere(long_clave)
ciphertext = Vigenere(clave).encipher(plaintext)

print("Clave:", clave)
print("Texto cifrado: ", ciphertext)