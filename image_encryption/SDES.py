from PIL import Image
from Crypto.Cipher import DES
from Crypto.Random import get_random_bytes
from Crypto.Util import Counter
import numpy as np

def imagen_a_bytes(imagen):
    return np.array(imagen).tobytes()

def bytes_a_imagen(datos_bytes, modo_imagen, tamaño_imagen):
    return Image.frombytes(modo_imagen, tamaño_imagen, datos_bytes)

def cifrar_imagen(ruta_imagen, clave, modo):
    # Cargar la imagen
    imagen = Image.open(ruta_imagen)
    modo_imagen = imagen.mode
    tamaño_imagen = imagen.size
    datos_imagen = imagen_a_bytes(imagen)

    # Asegurarse de que los datos de la imagen sean múltiplos de 8 para DES
    while len(datos_imagen) % 8 != 0:
        datos_imagen += b'\0'

    info = None
    # Crear un objeto DES en modo deseado
    if(modo == DES.MODE_ECB):
      cifrador = DES.new(clave, DES.MODE_ECB)
    if(modo == DES.MODE_CBC or modo == DES.MODE_OFB):
      cifrador = DES.new(clave, modo)
      iv = cifrador.iv
      info = iv
    if(modo == DES.MODE_CTR):
      contador = Counter.new(64)
      cifrador = DES.new(clave, DES.MODE_CTR, counter=contador)

    # Cifrar los datos de la imagen
    datos_cifrados = cifrador.encrypt(datos_imagen)

    # Convertir los datos cifrados de nuevo a una imagen
    imagen_cifrada = bytes_a_imagen(datos_cifrados, modo_imagen, tamaño_imagen)

    # Guardar la imagen cifrada
    ruta_imagen_cifrada = 'img_cifrada.png'
    imagen_cifrada.save(ruta_imagen_cifrada)

    return ruta_imagen_cifrada, info

def descifrar_imagen(ruta_imagen_cifrada, clave, modo, info):
    # Cargar la imagen cifrada
    imagen_cifrada = Image.open(ruta_imagen_cifrada)
    datos_cifrados = imagen_a_bytes(imagen_cifrada)

    # Crear un objeto DES en modo deseado
    if(modo == DES.MODE_ECB):
      cifrador = DES.new(clave, DES.MODE_ECB)
    if(modo == DES.MODE_CBC or modo == DES.MODE_OFB):
      iv = info
      cifrador = DES.new(clave, modo, iv)
    if(modo == DES.MODE_CTR):
      contador = Counter.new(64)
      cifrador = DES.new(clave, DES.MODE_CTR, counter=contador)

    # Descifrar los datos de la imagen
    datos_descifrados = cifrador.decrypt(datos_cifrados)

    # Convertir los datos descifrados de nuevo a una imagen
    imagen_descifrada = bytes_a_imagen(datos_descifrados, imagen_cifrada.mode, imagen_cifrada.size)

    # Guardar la imagen descifrada
    ruta_imagen_descifrada = 'img_descifrada.png'
    imagen_descifrada.save(ruta_imagen_descifrada)

    return ruta_imagen_descifrada


# Obtener el modo de cifrado deseado por el usuario
modo = elegir_modo_cifrado()

# Generar una clave
clave = get_random_bytes(8)  # DES requiere una clave de 8 bytes

# Ruta de la imagen a cifrar
ruta_imagen = 'chess.jpg'

# Cifrar la imagen
ruta_imagen_cifrada, info = cifrar_imagen(ruta_imagen, clave, modo)
print(f"Imagen cifrada guardada en: {ruta_imagen_cifrada}")

# Descifrar la imagen
ruta_imagen_descifrada = descifrar_imagen(ruta_imagen_cifrada, clave, modo, info)
print(f"Imagen descifrada guardada en: {ruta_imagen_descifrada}")
