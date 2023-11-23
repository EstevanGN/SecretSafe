import numpy as np
from sympy import Matrix

def generar_matriz_clave():
    while True:
        # Genera una matriz aleatoria de 4x4
        matriz = np.random.randint(32, 127, size=(4, 4))
        
        # Verifica que el determinante sea diferente de 0 y primo relativo con 95
        det = int(round(np.linalg.det(matriz)))
        if det != 0 and np.gcd(det, 95) == 1:
            lista = matriz.flatten()
            resultado = ",".join(map(str, lista))
            return resultado
        

def texto_a_matriz(texto, n):
    # Convierte el texto en una matriz de n x n
    matriz = []
    for i in range(0, len(texto), n):
        bloque = [ord(c) - 32 for c in texto[i:i+n]]
        matriz.append(bloque)
    return np.array(matriz)

def matriz_a_texto(matriz):
    # Convierte una matriz de números a texto
    return ''.join([chr(c + 32) for fila in matriz for c in fila])

def cifrar_hill(texto, matriz_clave):
    n = len(matriz_clave)
    texto = texto.ljust((len(texto) + n - 1) // n * n, ' ')  # Rellena con espacios si es necesario
    texto_matriz = texto_a_matriz(texto, n)
    cifrado_matriz = (texto_matriz @ matriz_clave) % 95
    return matriz_a_texto(cifrado_matriz)

def descifrar_hill(texto_cifrado, matriz_clave):
    n = len(matriz_clave)
    texto_cifrado_matriz = texto_a_matriz(texto_cifrado, n)
    clave_inversa = Matrix(matriz_clave).inv_mod(95)
    descifrado_matriz = (texto_cifrado_matriz @ clave_inversa) % 95
    return matriz_a_texto(np.array(descifrado_matriz))

def convert_numbers_to_matrix(vector_clave):
    vector_clave = list(map(int, vector_clave))
    matriz = []
    for i in range(0, len(vector_clave), 4):
        matriz.append(vector_clave[i:i+4])
    return matriz