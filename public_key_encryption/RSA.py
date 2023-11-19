import random

# Función para verificar si un número es primo
def es_primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True

# Función para generar un número primo en el rango de caracteres imprimibles ASCII
def generar_primo():
    primo = random.randint(33, 126)
    while not es_primo(primo):
        primo = random.randint(33, 126)
    return primo

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

    return ((n, e), (n, d))

# Función para cifrar un mensaje usando la clave pública
def cifrar(mensaje, clave_publica):
    n, e = clave_publica
    return [pow(ord(char), e, n) for char in mensaje]

# Función para descifrar un mensaje cifrado usando la clave privada
def descifrar(cifrado, clave_privada):
    n, d = clave_privada
    return ''.join([chr(pow(char, d, n)) for char in cifrado])

# Solicitar al usuario que ingrese un mensaje
mensaje_original = input("Ingrese el mensaje que desea cifrar: ")

# Obtener el alfabeto de caracteres imprimibles ASCII
alfabeto = ''.join([chr(i) for i in range(33, 128)])

# Generar claves pública y privada
clave_publica, clave_privada = generar_claves()

# Mostrar claves generadas
print("Clave pública:", clave_publica)
print("Clave privada:", clave_privada)

# Cifrar el mensaje original
mensaje_cifrado = cifrar(mensaje_original, clave_publica)
print("Mensaje cifrado:", mensaje_cifrado)

# Descifrar el mensaje cifrado
mensaje_descifrado = descifrar(mensaje_cifrado, clave_privada)
print("Mensaje descifrado:", mensaje_descifrado)


