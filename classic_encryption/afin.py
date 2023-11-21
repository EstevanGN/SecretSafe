import random
import math

# Test

def cifrar_afin(texto, a, b):
    texto_cifrado = ""
    for caracter in texto:
        if ' ' <= caracter <= '~':
            # Asegurarse de que el caracter esté en el rango ASCII imprimible (32-126)
            codigo = ord(caracter)
            codigo_cifrado = ((a * (codigo - 32) + b) % 95) + 32  # 95 caracteres imprimibles
            texto_cifrado += chr(codigo_cifrado)
        else:
            texto_cifrado += caracter  # Mantener caracteres no imprimibles sin cambios

    return texto_cifrado

def descifrar_afin(texto_cifrado, a, b):
    texto_descifrado = ""
    a_inverso = pow(a, -1, 95)  # Calcular el inverso de 'a' módulo 95

    for caracter in texto_cifrado:
        if ' ' <= caracter <= '~':
            # Asegurarse de que el caracter esté en el rango ASCII imprimible (32-126)
            codigo = ord(caracter)
            codigo_descifrado = ((a_inverso * (codigo - 32 - b)) % 95) + 32  # 95 caracteres imprimibles
            texto_descifrado += chr(codigo_descifrado)
        else:
            texto_descifrado += caracter  # Mantener caracteres no imprimibles sin cambios

    return texto_descifrado

def generar_claves_afin():
    # Generar una clave "a" coprima con 95
    coprimos = [i for i in range(2, 95) if math.gcd(i, 95) == 1]
    a = random.choice(coprimos)

    # Generar una clave "b" aleatoria
    b = random.randint(1, 94)  # Rango de 1 a 94

    return a, b

# Solicitar al usuario seleccionar entre cifrar o descifrar
opcion = input("Selecciona 'c' para cifrar o 'd' para descifrar: ")

if opcion == 'c':
    # Solicitar al usuario ingresar el texto
    texto_original = input("Ingrese el texto a cifrar: ")

    # Generar claves aleatorias
    a, b = generar_claves_afin()

    texto_cifrado = cifrar_afin(texto_original, a, b)
    print("Texto Cifrado:", texto_cifrado)
    print("Claves utilizadas (a, b):", a, b)

elif opcion == 'd':
    texto_cifrado = input("Ingrese el texto cifrado: ")
    a = int(input("Ingrese el valor de 'a' utilizado: "))
    b = int(input("Ingrese el valor de 'b' utilizado: "))

    texto_descifrado = descifrar_afin(texto_cifrado, a, b)
    print("Texto Descifrado:", texto_descifrado)
else:
    print("Opción no válida. Debes seleccionar 'c' o 'd'.")