from PIL import Image
from Crypto.Cipher import AES
from Crypto.Util import Counter
from Crypto.Random import get_random_bytes
import numpy as np

def imagen_a_bytes(imagen):
    return np.array(imagen).tobytes()

def bytes_a_imagen(datos_bytes, modo_imagen, tamaño_imagen):
    return Image.frombytes(modo_imagen, tamaño_imagen, datos_bytes)

def elegir_modo_cifrado():
    modos = {
        "1": AES.MODE_ECB,
        "2": AES.MODE_CBC,
        "3": AES.MODE_OFB,
        "4": AES.MODE_CTR,
        
    }

    print("Elige un modo de cifrado:")
    print("1: ECB")
    print("2: CBC")
    print("3: OFB")
    print("4: CTR")
    

    eleccion = input("Introduce el número del modo deseado: ")
    return modos.get(eleccion, AES.MODE_CBC)

def cifrar_imagen(ruta_imagen, clave, modo):
    # Cargar la imagen
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
    ruta_imagen_cifrada = 'img_cifrada.png'
    imagen_cifrada.save(ruta_imagen_cifrada)

    return ruta_imagen_cifrada, info

def descifrar_imagen(ruta_imagen_cifrada, clave, modo, info):
    # Cargar la imagen cifrada
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
    ruta_imagen_descifrada = 'img_descifrada.png'
    imagen_descifrada.save(ruta_imagen_descifrada)

    return ruta_imagen_descifrada


# Obtener el modo de cifrado deseado por el usuario
modo = elegir_modo_cifrado()

# Generar una clave y un vector de inicialización (IV)
clave = get_random_bytes(16)  # AES requiere una clave de 16 (AES-128), 24 (AES-192) o 32 (AES-256) bytes


# Ruta de la imagen a cifrar
# TODO: CAMBIAR ESTA RUTA
ruta_imagen = '.jpg'

# Cifrar la imagen
ruta_imagen_cifrada, info = cifrar_imagen(ruta_imagen, clave, modo)
print(f"Imagen cifrada guardada en: {ruta_imagen_cifrada}")

# Descifrar la imagen
ruta_imagen_descifrada = descifrar_imagen(ruta_imagen_cifrada, clave, modo, info)
print(f"Imagen descifrada guardada en: {ruta_imagen_descifrada}")
