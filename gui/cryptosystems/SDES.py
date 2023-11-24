from PIL import Image
from Crypto.Cipher import DES
from Crypto.Random import get_random_bytes
from Crypto.Util import Counter
import numpy as np

def imagen_a_bytes(imagen):
    return np.array(imagen).tobytes()

def bytes_a_imagen(datos_bytes, modo_imagen, tamaño_imagen):
    return Image.frombytes(modo_imagen, tamaño_imagen, datos_bytes)
  
def sdes_generate_key():
    return list(get_random_bytes(8))
  
def cifrar_imagen_ecb(ruta_imagen, clave, filename):
    # Cargar la imagen
    imagen = Image.open(ruta_imagen)
    modo_imagen = imagen.mode
    tamaño_imagen = imagen.size
    datos_imagen = imagen_a_bytes(imagen)

    # Asegurarse de que los datos de la imagen sean múltiplos de 8 para DES
    while len(datos_imagen) % 8 != 0:
        datos_imagen += b'\0'

    info = None
    cifrador = DES.new(clave, DES.MODE_ECB)

    # Cifrar los datos de la imagen
    datos_cifrados = cifrador.encrypt(datos_imagen)

    # Convertir los datos cifrados de nuevo a una imagen
    imagen_cifrada = bytes_a_imagen(datos_cifrados, modo_imagen, tamaño_imagen)

    # Guardar la imagen cifrada
    ruta_imagen_cifrada = 'testing_images/' + filename + '.png'
    imagen_cifrada.save(ruta_imagen_cifrada)

    return ruta_imagen_cifrada
  
def cifrar_imagen_ctr(ruta_imagen, clave, filename):
    # Cargar la imagen
    imagen = Image.open(ruta_imagen)
    modo_imagen = imagen.mode
    tamaño_imagen = imagen.size
    datos_imagen = imagen_a_bytes(imagen)

    # Asegurarse de que los datos de la imagen sean múltiplos de 8 para DES
    while len(datos_imagen) % 8 != 0:
        datos_imagen += b'\0'

    info = None
    contador = Counter.new(64)
    cifrador = DES.new(clave, DES.MODE_CTR, counter=contador)

    # Cifrar los datos de la imagen
    datos_cifrados = cifrador.encrypt(datos_imagen)

    # Convertir los datos cifrados de nuevo a una imagen
    imagen_cifrada = bytes_a_imagen(datos_cifrados, modo_imagen, tamaño_imagen)

    # Guardar la imagen cifrada
    ruta_imagen_cifrada = 'testing_images/' + filename + '.png'
    imagen_cifrada.save(ruta_imagen_cifrada)

    return ruta_imagen_cifrada

def cifrar_imagen(ruta_imagen, clave, filename):
    # Cargar la imagen
    imagen = Image.open(ruta_imagen)
    modo_imagen = imagen.mode
    tamaño_imagen = imagen.size
    datos_imagen = imagen_a_bytes(imagen)

    # Asegurarse de que los datos de la imagen sean múltiplos de 8 para DES
    while len(datos_imagen) % 8 != 0:
        datos_imagen += b'\0'

    info = None
    cifrador = DES.new(clave, DES.MODE_CBC)
    iv = cifrador.iv
    info = iv

    # Cifrar los datos de la imagen
    datos_cifrados = cifrador.encrypt(datos_imagen)

    # Convertir los datos cifrados de nuevo a una imagen
    imagen_cifrada = bytes_a_imagen(datos_cifrados, modo_imagen, tamaño_imagen)

    # Guardar la imagen cifrada
    ruta_imagen_cifrada = 'testing_images/' + filename + '.png'
    imagen_cifrada.save(ruta_imagen_cifrada)

    return ruta_imagen_cifrada, list(info)

def descifrar_imagen(ruta_imagen_cifrada, clave, filename, info):
    # Cargar la imagen cifrada
    imagen_cifrada = Image.open(ruta_imagen_cifrada)
    datos_cifrados = imagen_a_bytes(imagen_cifrada)
    iv = info
    cifrador = DES.new(clave, DES.MODE_CBC, iv)

    # Descifrar los datos de la imagen
    datos_descifrados = cifrador.decrypt(datos_cifrados)

    # Convertir los datos descifrados de nuevo a una imagen
    imagen_descifrada = bytes_a_imagen(datos_descifrados, imagen_cifrada.mode, imagen_cifrada.size)

    # Guardar la imagen descifrada
    ruta_imagen_descifrada = 'testing_images/' + filename + '.png'
    imagen_descifrada.save(ruta_imagen_descifrada)

    return ruta_imagen_descifrada
  
def descifrar_imagen_ecb(ruta_imagen_cifrada, clave, filename):
    # Cargar la imagen cifrada
    imagen_cifrada = Image.open(ruta_imagen_cifrada)
    datos_cifrados = imagen_a_bytes(imagen_cifrada)
    cifrador = DES.new(clave, DES.MODE_ECB)

    # Descifrar los datos de la imagen
    datos_descifrados = cifrador.decrypt(datos_cifrados)

    # Convertir los datos descifrados de nuevo a una imagen
    imagen_descifrada = bytes_a_imagen(datos_descifrados, imagen_cifrada.mode, imagen_cifrada.size)

    # Guardar la imagen descifrada
    ruta_imagen_descifrada = 'testing_images/' + filename + '.png'
    imagen_descifrada.save(ruta_imagen_descifrada)

    return ruta_imagen_descifrada
  
def descifrar_imagen_ctr(ruta_imagen_cifrada, clave, filename):
    # Cargar la imagen cifrada
    imagen_cifrada = Image.open(ruta_imagen_cifrada)
    datos_cifrados = imagen_a_bytes(imagen_cifrada)
    contador = Counter.new(64)
    cifrador = DES.new(clave, DES.MODE_CTR, counter=contador)

    # Descifrar los datos de la imagen
    datos_descifrados = cifrador.decrypt(datos_cifrados)

    # Convertir los datos descifrados de nuevo a una imagen
    imagen_descifrada = bytes_a_imagen(datos_descifrados, imagen_cifrada.mode, imagen_cifrada.size)

    # Guardar la imagen descifrada
    ruta_imagen_descifrada = 'testing_images/' + filename + '.png'
    imagen_descifrada.save(ruta_imagen_descifrada)

    return ruta_imagen_descifrada


