import random
from sympy import nextprime
from sympy import isprime, gcd
from Crypto.Util.number import bytes_to_long, long_to_bytes
from sympy import gcdex

def generar_primo_rabin(bits=1000):
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
    while p == q:
        q = generar_primo_rabin()
    n = p * q
    b = random.randint(0, n - 1)
    b =0
    clave_publica = (n, b)
    clave_privada = (p, q)
    return clave_publica, clave_privada

def cifrar(mensaje, clave):
  n, b = clave
  mensaje_ascii = bytes_to_long(mensaje.encode('ascii'))
  return (pow(mensaje_ascii,2) + b) % n;


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
    if isinstance(r1,str): return r1
    if isinstance(r2,str): return r2
    if isinstance(r3,str): return r3
    if isinstance(r4,str): return r4
    return r1,r2,r3,r4

def descifrar(mensaje, clave, b):
  p,q = clave
  n = p*q
  # inverso de 2 
  two_inv = (int(gcdex(2,n)[0])+n)%n
  # inverso de 4 
  four_inv = (int(gcdex(4,n)[0])+n)%n
  c = (mensaje + (b*b*four_inv)) % n
  h = (b*two_inv) % n
  # Calcular raices de sqrt(*)
  m_p = pow(c, (p + 1) // 4, p)
  m_q = pow(c, (q + 1) // 4, q)
  # Teorema Chino del Residuo
  # b1: inverso de q mod p
  b1 = (int(gcdex(q,p)[0])+p)%p
  # b2: inverso de p mod q
  b2 = (int(gcdex(p,q)[0])+q)%q
  # ambos son positivos  
  r1 = ((q*m_p*b1 + p*m_q*b2)-h) % n
  # mp positivo mq negativo
  r2 = ((q*m_p*b1 - p*m_q*b2)-h) % n
  # mp negativo mq positivo
  r3 = (((-1)*q*m_p*b1 + p*m_q*b2)-h) % n
  # ambos negativos
  r4 = (((-1)*q*m_p*b1 - p*m_q*b2) - h) % n

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
mensaje_descifrado = descifrar(mensaje_cifrado, clave_privada, clave_publica[1])
print("Mensaje descifrado:", mensaje_descifrado)
