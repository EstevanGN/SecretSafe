from Crypto.Util import number

# Función para generar un número primo aleatorio grande
def generate_prime():
    return number.getPrime(2048)

# Función para generar un número aleatorio entre 0 y p-1
def generate_k(p):
    return number.getRandomRange(0, p-1)

# Función para generar un generador alpha en el grupo aditivo de los enteros modulo p
def generate_alpha(p):
    while True:
        alpha = number.getRandomRange(2, p-1)
        if pow(alpha, (p-1)//2, p) != 1 and pow(alpha, (p-1)//3, p) != 1:
            return alpha

# Función para generar una clave privada d
def generate_d(p):
    return number.getRandomRange(1, p-2)

# Función para calcular beta = alpha^d mod p
def calculate_beta(alpha, d, p):
    return pow(alpha, d, p)

# Función para encriptar un mensaje
def encrypt_message(message,clavPub):
    alpha, beta, p, k=clavPub
    # Convertir el mensaje a un número entero
    m = int.from_bytes(message.encode(), 'big')
    # Calcular el primer componente del texto cifrado
    c1 = pow(alpha, k, p)
    # Calcular el segundo componente del texto cifrado
    c2 = (m * pow(beta, k, p)) % p
    # Devolver el texto cifrado como una tupla
    return (c1, c2)

# Función para desencriptar un mensaje
def decrypt_message(ciphertext, p, d):
    # Obtener los componentes del texto cifrado
    c1, c2 = ciphertext
    # Calcular el inverso de c1^d mod p
    inv_c1_d = pow(c1, d, p)
    inv_c1_d = number.inverse(inv_c1_d, p)
    # Calcular el mensaje original
    m = (c2 * inv_c1_d) % p
    # Convertir el mensaje a una cadena de caracteres
    message = m.to_bytes((m.bit_length() + 7) // 8, 'big').decode()
    # Devolver el mensaje original
    return message

def generar_clave():
    p = generate_prime()
    k = generate_k(p)
    alpha = generate_alpha(p)
    d = generate_d(p)
    beta = calculate_beta(alpha, d, p)
    pub=(alpha,beta,p,k)
    priv=d
    return (pub,priv)