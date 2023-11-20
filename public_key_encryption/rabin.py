import random
from sympy import nextprime
from sympy import isprime, gcd
from Crypto.Util.number import bytes_to_long, long_to_bytes
from sympy import gcdex

def generar_primo_rabin(bits=30):
    lower_bound = 2**(bits - 1)
    upper_bound = 2**bits - 1

    prime_candidate = random.randint(lower_bound, upper_bound)
    random_prime = nextprime(prime_candidate)
    while random_prime % 4 != 3:
        prime_candidate = random.randint(lower_bound, upper_bound)
        random_prime = nextprime(prime_candidate)
    return random_prime

def generar_claves():
  p = generar_primo_rabin()
  q = generar_primo_rabin()
  while(p == q):
    q = generar_primo_rabin()
  clave_publica = p*q
  clave_privada = (p,q)
  return clave_publica, clave_privada

def cifrar(mensaje, clave):
  mensaje_ascii = bytes_to_long(mensaje.encode('ascii'))
  return pow(mensaje_ascii,2, clave)

def decodificar_utf(r1,r2,r3,r4):
    try:
        r1 = long_to_bytes(r1).decode('ascii')
    except Exception as e:
      pass

    try:
        r2 = long_to_bytes(r2).decode('ascii')
    except Exception as e:
      pass

    try:
        r3 = long_to_bytes(r3).decode('ascii')
    except Exception as e:
      pass

    try:
        r4 = long_to_bytes(r4).decode('ascii')
    except Exception as e:
      pass
    return r1,r2,r3,r4

def descifrar(mensaje, clave):
  p,q = clave
  n = p*q
  c = mensaje
  # Calcular raices de p
  m_p = pow(c, (p + 1) // 4, p)
  m_q = pow(c, (q + 1) // 4, q)
  # Algoritmo Extendido de Euclides
  yp, yq, gcd = gcdex(p, q)
  y_p = int(yp)
  y_q = int(yq)
  # Teorema Chino del Residuo
  # Cuatro posibles mensajes
  r1 = (y_p * p * m_q + y_q * q * m_p) % n
  r2 = n - r1
  r3 = (y_p * p * m_q - y_q * q * m_p) % n
  r4 = n - r3
  return decodificar_utf(r1,r2,r3,r4)

# Solicitar al usuario que ingrese un mensaje
mensaje_original = input("Ingrese el mensaje que desea cifrar: ")


# Obtener el alfabeto de caracteres imprimibles ASCII
alfabeto = ''.join([chr(i) for i in range(33, 128)])

# Generar claves pública y privada
clave_publica, clave_privada = generar_claves()

# Mostrar claves generadas
print("Clave pública:", clave_publica)
print("Clave privada:", clave_privada)

# Cifrar el mensaje original
mensaje_cifrado = cifrar(mensaje_original, clave_publica)
print("Mensaje cifrado:", mensaje_cifrado)

# Descifrar el mensaje cifrado
mensaje_descifrado = descifrar(mensaje_cifrado, clave_privada)
print("Mensaje descifrado:", mensaje_descifrado)

