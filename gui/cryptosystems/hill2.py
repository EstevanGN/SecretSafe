import numpy as np
from PIL import Image
from sympy import Matrix
import ast

def cargar_imagen(ruta):
    """ Carga una imagen y la convierte en una matriz numpy. """
    img = Image.open(ruta)
    img = img.convert("RGB")
    datos = np.array(img)
    return datos

def guardar_imagen(datos, ruta):
    """ Guarda una matriz numpy como imagen. """
    img = Image.fromarray(np.uint8(datos), 'RGB')
    img.save(ruta)

def crear_clave_hill():
    while True:
        # Genera una matriz aleatoria de 3x3 con números en el rango [1, 256)
        matriz = np.random.randint(1, 256, size=(3, 3), dtype=np.uint8)
        
        # Verifica que el determinante sea diferente de 0 y primo relativo con 256
        det = int(round(np.linalg.det(matriz)))
        if det != 0 and np.gcd(det, 256) == 1:
            return matriz

def clave_inversa(matriz_clave):
    inversa = Matrix(matriz_clave).inv_mod(256)
    return inversa

def aplicar_cifrado_hill(datos, clave):
    """ Aplica el cifrado o descifrado de Hill a la imagen. """
    forma = datos.shape
    datos_planos = datos.reshape(-1, forma[-1])
    transformados = np.dot(datos_planos, clave) % 256
    return transformados.reshape(forma)

# Cargar imagen
#ruta_imagen = 'imagen_grayscale.jpg'
#datos_imagen = cargar_imagen(ruta_imagen)
# Crear clave de Hill
#clave = crear_clave_hill()
# Cifrar imagen
#print(clave.tolist())
#imagen_cifrada = aplicar_cifrado_hill(datos_imagen, clave)
#guardar_imagen(imagen_cifrada, 'imagen_cifrada.png')

# Descifrar imagen
#ruta_imagen_cifrada = 'imagen_cifrada.png'
#datos_imagen_cifrada = cargar_imagen(ruta_imagen_cifrada)
#cadena_matriz = input("Cargue la clave en de matriz, por ejemplo: [[2, 3, 4], [5, 6, 7], [8, 9, 10]]")
#matriz_resultante = ast.literal_eval(cadena_matriz)
#matriz = [[int(elemento) for elemento in fila] for fila in matriz_resultante]
#clave_inv = clave_inversa(matriz)
#imagen_descifrada = aplicar_cifrado_hill(datos_imagen_cifrada, clave_inv)
#guardar_imagen(imagen_descifrada, 'imagen_descifrada.png')