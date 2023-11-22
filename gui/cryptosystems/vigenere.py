import random

def generar_clave_vigenere(texto):
    longitud = random.randint(2, int(len(texto)/2))
    caracteres = ''.join([chr(i) for i in range(32, 127)])  # Caracteres ASCII imprimibles (32-126)
    return ''.join(random.choice(caracteres) for _ in range(longitud))

def cifrar_vigenere(texto, clave):
    texto_cifrado = ""
    clave_expandida = clave * (len(texto) // len(clave)) + clave[:len(texto) % len(clave)]

    for i in range(len(texto)):
        if ' ' <= texto[i] <= '~':
            codigo_texto = ord(texto[i])
            codigo_clave = ord(clave_expandida[i])
            codigo_cifrado = ((codigo_texto - 32 + codigo_clave - 32) % 95) + 32  # 95 caracteres imprimibles
            texto_cifrado += chr(codigo_cifrado)
        else:
            texto_cifrado += texto[i]  # Mantener caracteres no imprimibles sin cambios

    return texto_cifrado

def descifrar_vigenere(texto_cifrado, clave):
    texto_descifrado = ""
    clave_expandida = clave * (len(texto_cifrado) // len(clave)) + clave[:len(texto_cifrado) % len(clave)]

    for i in range(len(texto_cifrado)):
        if ' ' <= texto_cifrado[i] <= '~':
            codigo_cifrado = ord(texto_cifrado[i])
            codigo_clave = ord(clave_expandida[i])
            codigo_descifrado = ((codigo_cifrado - 32 - codigo_clave + 32) % 95) + 32  # 95 caracteres imprimibles
            texto_descifrado += chr(codigo_descifrado)
        else:
            texto_descifrado += texto_cifrado[i]  # Mantener caracteres no imprimibles sin cambios

    return texto_descifrado
