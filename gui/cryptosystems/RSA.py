

import random
from sympy import nextprime
from Crypto.Util import number
from Crypto.Util.number import bytes_to_long, long_to_bytes
# Función para verificar si un número es primofrom Crypto.Util import number

# Función para generar un número primo aleatorio grande
def generar_primo(bits=1000):
    lower_bound = 2**(bits - 1)
    upper_bound = 2**bits - 1

    prime_candidate = random.randint(lower_bound, upper_bound)
    random_prime = nextprime(prime_candidate)
    return random_prime

# Función para generar un número primo en el rango de caracteres imprimibles ASCII


# Función para calcular el máximo común divisor (MCD)
def mcd(a, b):
    while b:
        a, b = b, a % b
    return a

# Función para generar claves pública y privada RSA
def generar_claves():
    p = generar_primo()
    q = generar_primo()
    n = p * q   
    phi = (p - 1) * (q - 1)

    e = random.randint(2, phi - 1)
    while mcd(e, phi) != 1:
        e = random.randint(2, phi - 1)

    d = pow(e, -1, phi)

    return ((n, e), (n, d),(p,q,phi))

# Función para cifrar un mensaje usando la clave pública
def cifrar(mensaje, clave_publica):
    mensaje_ascii=bytes_to_long(mensaje.encode('ascii'))
    n, e = clave_publica
    return pow(mensaje_ascii, e, n)

# Función para descifrar un mensaje cifrado usando la clave privada
def descifrar(cifrado, clave_privada):
    n, d = clave_privada
    return ''.join(long_to_bytes(pow(cifrado, d, n)).decode('ascii')) 

