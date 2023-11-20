import numpy as np
from PIL import Image

def generar_matriz_clave():
    while True:
        # Genera una matriz aleatoria de 3x3 con números en el rango [1, 256)
        matriz = np.random.randint(1, 256, size=(3, 3), dtype=np.uint8)
        
        # Verifica que el determinante sea diferente de 0 y primo relativo con 256
        det = int(round(np.linalg.det(matriz)))
        if det != 0 and np.gcd(det, 256) == 1:
            return matriz

def cifrar_hill_grayscale(imagen, matriz_clave):
    # Convierte la imagen en una matriz de porcentajes de tinta negra
    matriz_imagen = np.array(imagen.convert("L"), dtype=np.float32) / 255.0

    # Ajusta las dimensiones para que sean múltiplos de 3
    filas, columnas = matriz_imagen.shape
    filas_pad = (filas // 3 + 1) * 3 - filas
    columnas_pad = (columnas // 3 + 1) * 3 - columnas
    matriz_imagen = np.pad(matriz_imagen, ((0, filas_pad), (0, columnas_pad)), mode='constant', constant_values=1.0)

    # Aplica la matriz clave a cada bloque 3x3 de porcentajes de tinta negra
    for i in range(0, matriz_imagen.shape[0], 3):
        for j in range(0, matriz_imagen.shape[1], 3):
            bloque = matriz_imagen[i:i+3, j:j+3]
            bloque_cifrado = (bloque @ matriz_clave) % 1.0
            matriz_imagen[i:i+3, j:j+3] = bloque_cifrado

    # Convierte la matriz resultante de porcentajes de tinta negra a una imagen
    imagen_cifrada = Image.fromarray((matriz_imagen * 255).astype(np.uint8))
    return imagen_cifrada

def descifrar_hill_grayscale(imagen_cifrada, matriz_clave):
    # Convierte la imagen cifrada en una matriz de porcentajes de tinta negra
    matriz_imagen_cifrada = np.array(imagen_cifrada.convert("L"), dtype=np.float32) / 255.0

    # Ajusta las dimensiones para que sean múltiplos de 3
    filas, columnas = matriz_imagen_cifrada.shape
    filas_pad = (filas // 3 + 1) * 3 - filas
    columnas_pad = (columnas // 3 + 1) * 3 - columnas
    matriz_imagen_cifrada = np.pad(matriz_imagen_cifrada, ((0, filas_pad), (0, columnas_pad)), mode='constant', constant_values=1.0)

    # Aplica la matriz clave inversa a cada bloque 3x3 de porcentajes de tinta negra
    clave_inversa = np.array(np.linalg.inv(matriz_clave), dtype=np.float32)

    for i in range(0, matriz_imagen_cifrada.shape[0], 3):
        for j in range(0, matriz_imagen_cifrada.shape[1], 3):
            bloque = matriz_imagen_cifrada[i:i+3, j:j+3]
            bloque_descifrado = (bloque @ clave_inversa) % 1.0
            matriz_imagen_cifrada[i:i+3, j:j+3] = bloque_descifrado

    # Convierte la matriz resultante de porcentajes de tinta negra a una imagen
    imagen_descifrada = Image.fromarray((matriz_imagen_cifrada * 255).astype(np.uint8))
    return imagen_descifrada

# Ejemplo de uso
opcion = input("Selecciona 'c' para cifrar o 'd' para descifrar: ")

if opcion == 'c':
    # Cargar la imagen original en escala de grises
    imagen_original = Image.open("imagen_grayscale.jpeg")

    # Generar una matriz clave aleatoria
    matriz_clave = generar_matriz_clave()
    print("Matriz clave:")
    print(matriz_clave)

    # Cifrar la imagen
    print("Cifrar:")
    imagen_cifrada = cifrar_hill_grayscale(imagen_original, matriz_clave)
    imagen_cifrada.save("imagen_cifrada_grayscale.jpeg")
    imagen_cifrada.show()

else:
    # Descifrar la imagen
    print("Descifrar:")
    imagen_cifrada = Image.open("imagen_cifrada_grayscale.jpeg")
    entries = list(map(int, input("Matriz clave. Ingrese los números separados por ',': ").split(',')))
    matriz_clave = np.array(entries).reshape(3, 3)
    imagen_descifrada = descifrar_hill_grayscale(imagen_cifrada, matriz_clave)
    imagen_descifrada.save("imagen_descifrada_grayscale.jpeg")
    imagen_descifrada.show()
