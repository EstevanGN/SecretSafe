import random

def cifrar_desplazamiento(texto, clave):
    texto_cifrado = ""
    for caracter in texto:
        if ' ' <= caracter <= '~':
            # Asegurarse de que el caracter esté en el rango ASCII imprimible (32-126)
            codigo = ord(caracter)
            codigo_cifrado = ((codigo - 32 + clave) % 95) + 32  # 95 caracteres imprimibles
            texto_cifrado += chr(codigo_cifrado)
        else:
            texto_cifrado += caracter  # Mantener caracteres no imprimibles sin cambios

    return texto_cifrado, clave

def descifrar_desplazamiento(texto_cifrado, clave):
    texto_descifrado = ""
    clave_inversa = 95 - clave  # Clave inversa para descifrar

    for caracter in texto_cifrado:
        if ' ' <= caracter <= '~':
            # Asegurarse de que el caracter esté en el rango ASCII imprimible (32-126)
            codigo = ord(caracter)
            codigo_descifrado = ((codigo - 32 + clave_inversa) % 95) + 32  # 95 caracteres imprimibles
            texto_descifrado += chr(codigo_descifrado)
        else:
            texto_descifrado += caracter  # Mantener caracteres no imprimibles sin cambios

    return texto_descifrado

def generar_clave_desplazamiento():
    return random.randint(1, 94)  # Genera una clave aleatoria entre 1 y 94

# Solicitar al usuario seleccionar entre cifrar o descifrar
opcion = input("Selecciona 'c' para cifrar o 'd' para descifrar: ")

if opcion == 'c':
    # Solicitar al usuario ingresar el texto
    texto_original = input("Ingrese el texto a cifrar: ")

    # Generar una clave aleatoria
    clave = generar_clave_desplazamiento()

    texto_cifrado, clave_utilizada = cifrar_desplazamiento(texto_original, clave)
    print("Texto Cifrado:", texto_cifrado)
    print("Clave utilizada:", clave_utilizada)

elif opcion == 'd':
    texto_cifrado = input("Ingrese el texto cifrado: ")
    clave = int(input("Ingrese la clave utilizada: "))

    texto_descifrado = descifrar_desplazamiento(texto_cifrado, clave)
    print("Texto Descifrado:", texto_descifrado)
else:
    print("Opción no válida. Debes seleccionar 'c' o 'd'.")