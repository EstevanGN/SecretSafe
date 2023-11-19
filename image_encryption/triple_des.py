from PIL import Image
from Crypto.Cipher import DES3
from Crypto.Random import get_random_bytes
from Crypto.Util import Counter
import numpy as np

def imagen_a_bytes(imagen):
    return np.array(imagen).tobytes()

def bytes_a_imagen(datos_bytes, modo_imagen, tamaño_imagen):
    return Image.frombytes(modo_imagen, tamaño_imagen, datos_bytes)

def elegir_modo_cifrado():
    modos = {
        "1": DES3.MODE_ECB,
        "2": DES3.MODE_CBC,
        "3": DES3.MODE_OFB,
        "4": DES3.MODE_CTR,

    }

    print("Elige un modo de cifrado:")
    print("1: ECB")
    print("2: CBC")
    print("3: OFB")
    print("4: CTR")


    eleccion = input("Introduce el número del modo deseado: ")
    return modos.get(eleccion, DES3.MODE_CBC)

def cifrar_imagen(ruta_imagen, clave, modo):
    # Cargar la imagen
    imagen = Image.open(ruta_imagen)
    modo_imagen = imagen.mode
    tamaño_imagen = imagen.size
    datos_imagen = imagen_a_bytes(imagen)

    # Asegurarse de que los datos de la imagen sean múltiplos de 8 para 3DES
    while len(datos_imagen) % 8 != 0:
        datos_imagen += b'\0'

    info = None
    # Crear un objeto DES3 en modo deseado
    if(modo == DES3.MODE_ECB):
      cifrador = DES3.new(clave, DES3.MODE_ECB)
    if(modo == DES3.MODE_CBC or modo == DES3.MODE_OFB):
      cifrador = DES3.new(clave, modo)
      iv = cifrador.iv
      info = iv
    if(modo == DES3.MODE_CTR):
      contador = Counter.new(64)
      cifrador = DES3.new(clave, DES3.MODE_CTR, counter=contador)

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

    # Crear un objeto 3DES en modo deseado
    if(modo == DES3.MODE_ECB):
      cifrador = DES3.new(clave, DES3.MODE_ECB)
    if(modo == DES3.MODE_CBC or modo == DES3.MODE_OFB):
      iv = info
      cifrador = DES3.new(clave, modo, iv)
    if(modo == DES3.MODE_CTR):
      contador = Counter.new(64)
      cifrador = DES3.new(clave, DES3.MODE_CTR, counter=contador)

    # Descifrar los datos de la imagen
    datos_descifrados = cifrador.decrypt(datos_cifrados)

    # Convertir los datos descifrados de nuevo a una imagen
    imagen_descifrada = bytes_a_imagen(datos_descifrados, imagen_cifrada.mode, imagen_cifrada.size)

    # Guardar la imagen descifrada
    ruta_imagen_descifrada = 'img_descifrada.png'
    imagen_descifrada.save(ruta_imagen_descifrada)

    return ruta_imagen_descifrada

# Generar una clave
clave = get_random_bytes(24)  # 3DES requiere una clave de 24 bytes
modo = elegir_modo_cifrado()

# Ruta de la imagen a cifrar
ruta_imagen = '.jpg'

# Cifrar la imagen
ruta_imagen_cifrada, info = cifrar_imagen(ruta_imagen, clave, modo)
print(f"Imagen cifrada guardada en: {ruta_imagen_cifrada}")

# Descifrar la imagen
ruta_imagen_descifrada = descifrar_imagen(ruta_imagen_cifrada, clave, modo, info)
print(f"Imagen descifrada guardada en: {ruta_imagen_descifrada}")
