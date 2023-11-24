from PIL import Image
from Crypto.Cipher import AES
from Crypto.Util import Counter
from Crypto.Random import get_random_bytes
import numpy as np

def aes_generate_key():
  return list(get_random_bytes(16))

def imagen_a_bytes(imagen):
    return np.array(imagen).tobytes()

def bytes_a_imagen(datos_bytes, modo_imagen, tamaño_imagen):
    return Image.frombytes(modo_imagen, tamaño_imagen, datos_bytes)

def elegir_modo_cifrado():
    modos = {
        "2": AES.MODE_ECB,
        "0": AES.MODE_CBC,
        "3": AES.MODE_OFB,
        "1": AES.MODE_CTR
    }
    return modos.get("0", AES.MODE_CBC)
  
  
def elegir_modo_cifrado_ecb():
  modos = {
        "2": AES.MODE_ECB,
        "0": AES.MODE_CBC,
        "3": AES.MODE_OFB,
        "1": AES.MODE_CTR
    }
  return modos.get("2", AES.MODE_ECB)

def elegir_modo_cifrado_ctr():
  modos = {
        "2": AES.MODE_ECB,
        "0": AES.MODE_CBC,
        "3": AES.MODE_OFB,
        "1": AES.MODE_CTR
    }
  return modos.get("1", AES.MODE_CTR)

def cifrar_imagen_ecb(ruta_imagen, clave, filename):
    # Cargar la imagen
    modo = elegir_modo_cifrado_ecb()
    imagen = Image.open(ruta_imagen)
    modo_imagen = imagen.mode
    tamaño_imagen = imagen.size
    datos_imagen = imagen_a_bytes(imagen)
    info = None
    cifrador = AES.new(clave, AES.MODE_ECB)

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
    modo = elegir_modo_cifrado()
    imagen = Image.open(ruta_imagen)
    modo_imagen = imagen.mode
    tamaño_imagen = imagen.size
    datos_imagen = imagen_a_bytes(imagen)
    info = None
    contador = Counter.new(128)
    cifrador = AES.new(clave, AES.MODE_CTR, counter=contador)
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
    modo = elegir_modo_cifrado()
    imagen = Image.open(ruta_imagen)
    modo_imagen = imagen.mode
    tamaño_imagen = imagen.size
    datos_imagen = imagen_a_bytes(imagen)
    info = None
    # Crear un objeto AES en modo deseado
    if(modo == AES.MODE_ECB):
      cifrador = AES.new(clave, AES.MODE_ECB)
    if(modo == AES.MODE_CBC or modo == AES.MODE_OFB):
      cifrador = AES.new(clave, modo)
      iv = cifrador.iv
      info = iv
    if(modo == AES.MODE_CTR):
      contador = Counter.new(128)
      cifrador = AES.new(clave, AES.MODE_CTR, counter=contador)

    # Cifrar los datos de la imagen
    datos_cifrados = cifrador.encrypt(datos_imagen)

    # Convertir los datos cifrados de nuevo a una imagen
    imagen_cifrada = bytes_a_imagen(datos_cifrados, modo_imagen, tamaño_imagen)

    # Guardar la imagen cifrada
    ruta_imagen_cifrada = 'testing_images/' + filename + '.png'
    imagen_cifrada.save(ruta_imagen_cifrada)

    if (modo == AES.MODE_CBC or modo == AES.MODE_ECB):
      return ruta_imagen_cifrada, list(info)
    else:
      return ruta_imagen_cifrada

def descifrar_imagen(ruta_imagen_cifrada, clave, filename, info=None):
    # Cargar la imagen cifrada
    modo = elegir_modo_cifrado()
    imagen_cifrada = Image.open(ruta_imagen_cifrada)
    datos_cifrados = imagen_a_bytes(imagen_cifrada)

    # Crear un objeto AES en modo deseado
    if(modo == AES.MODE_ECB):
      cifrador = AES.new(clave, AES.MODE_ECB)
    if(modo == AES.MODE_CBC or modo == AES.MODE_OFB):
      iv = info
      cifrador = AES.new(clave, modo, iv)
    if(modo == AES.MODE_CTR):
      contador = Counter.new(128)
      cifrador = AES.new(clave, AES.MODE_CTR, counter=contador)
    # Descifrar los datos de la imagen
    datos_descifrados = cifrador.decrypt(datos_cifrados)

    # Convertir los datos descifrados de nuevo a una imagen
    imagen_descifrada = bytes_a_imagen(datos_descifrados, imagen_cifrada.mode, imagen_cifrada.size)

    # Guardar la imagen descifrada
    ruta_imagen_descifrada = 'testing_images/' + filename + '.png'
    imagen_descifrada.save(ruta_imagen_descifrada)

    return ruta_imagen_descifrada
  
def descifrar_imagen_ecb(ruta_imagen_cifrada, clave, filename, info=None):
    # Cargar la imagen cifrada
    modo = elegir_modo_cifrado_ecb()
    imagen_cifrada = Image.open(ruta_imagen_cifrada)
    datos_cifrados = imagen_a_bytes(imagen_cifrada)
    cifrador = AES.new(clave, AES.MODE_ECB)
    datos_descifrados = cifrador.decrypt(datos_cifrados)

    # Convertir los datos descifrados de nuevo a una imagen
    imagen_descifrada = bytes_a_imagen(datos_descifrados, imagen_cifrada.mode, imagen_cifrada.size)

    # Guardar la imagen descifrada
    ruta_imagen_descifrada = 'testing_images/' + filename + '.png'
    imagen_descifrada.save(ruta_imagen_descifrada)

    return ruta_imagen_descifrada

def descifrar_imagen_ctr(ruta_imagen_cifrada, clave, filename, info=None):
    # Cargar la imagen cifrada
    modo = elegir_modo_cifrado_ctr()
    imagen_cifrada = Image.open(ruta_imagen_cifrada)
    datos_cifrados = imagen_a_bytes(imagen_cifrada)
    contador = Counter.new(128)
    cifrador = AES.new(clave, AES.MODE_CTR, counter=contador)
    datos_descifrados = cifrador.decrypt(datos_cifrados)

    # Convertir los datos descifrados de nuevo a una imagen
    imagen_descifrada = bytes_a_imagen(datos_descifrados, imagen_cifrada.mode, imagen_cifrada.size)

    # Guardar la imagen descifrada
    ruta_imagen_descifrada = 'testing_images/' + filename + '.png'
    imagen_descifrada.save(ruta_imagen_descifrada)

    return ruta_imagen_descifrada