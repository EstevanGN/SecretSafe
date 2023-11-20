import numpy as np
from PIL import Image
from scipy import linalg

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

def crear_clave_hill(tamano):
    """ Crea una clave de cifrado de Hill aleatoria y su inversa. """
    while True:
        clave = np.random.randint(0, 256, (tamano, tamano), dtype=np.uint8)
        try:
            clave_inv = np.round(linalg.inv(clave) * np.linalg.det(clave)).astype(np.int64) % 256
            if np.all(np.dot(clave, clave_inv) % 256 == np.eye(tamano, dtype=np.int64)):
                return clave, clave_inv
        except linalg.LinAlgError:
            pass

def aplicar_cifrado_hill(datos, clave):
    """ Aplica el cifrado o descifrado de Hill a la imagen. """
    forma = datos.shape
    datos_planos = datos.reshape(-1, forma[-1])
    transformados = np.dot(datos_planos, clave) % 256
    return transformados.reshape(forma)

# Cargar imagen
ruta_imagen = 'imagen_grayscale.JPG'
datos_imagen = cargar_imagen(ruta_imagen)

# Crear clave de Hill
tamano_clave = 3
clave, clave_inv = crear_clave_hill(tamano_clave)

# Cifrar imagen
imagen_cifrada = aplicar_cifrado_hill(datos_imagen, clave)
guardar_imagen(imagen_cifrada, 'imagen_cifrada.png')

# Descifrar imagen
imagen_descifrada = aplicar_cifrado_hill(imagen_cifrada, clave_inv)
guardar_imagen(imagen_descifrada, 'imagen_descifrada.png')
