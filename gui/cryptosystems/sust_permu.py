import random

def generar_permutacion_aleatoria(longitud):
    permutacion = list(range(1, longitud + 1))
    random.shuffle(permutacion)
    return permutacion

def generar_permutacion_inversa(permutacion):
    inversa = [0] * len(permutacion)
    for i, pos in enumerate(permutacion):
        inversa[pos - 1] = i + 1
    return inversa

def generar_claves(texto):
    claves = []
    num_bloques = random.randint(1, int(len(texto)/2))
    
    # Limitar la cantidad de bloques
    num_bloques = max(1, min(num_bloques, len(texto)))
    
    # Dividir el texto en bloques
    bloque_longitud = len(texto) // num_bloques
    bloques = [texto[i:i+bloque_longitud] for i in range(0, len(texto), bloque_longitud)]
    
    # Generar una clave aleatoria para cada bloque
    for bloque in bloques:
        longitud_bloque = len(bloque)
        clave = generar_permutacion_aleatoria(longitud_bloque)
        claves.append(clave)
    
    # Generar una última permutación completa del texto cifrado
    permutacion_final = generar_permutacion_aleatoria(len(texto))
    return claves, permutacion_final, bloque_longitud

def cifrar_sustPermu(texto, bloque_longitud, claves, permutacion_final):
    texto_cifrado = ""
    bloques = [texto[i:i+bloque_longitud] for i in range(0, len(texto), bloque_longitud)]
    
    # Generar una clave aleatoria para cada bloque
    for indice, bloque in enumerate(bloques):
        longitud_bloque = len(bloque)
        clave = claves[indice]
        bloque_cifrado = [bloque[clave[i] - 1] for i in range(longitud_bloque)]
        texto_cifrado += ''.join(bloque_cifrado)
    
    texto_cifrado = ''.join([texto_cifrado[permutacion_final[i] - 1] for i in range(len(texto_cifrado))])
    
    return texto_cifrado

def descifrar_sustPermu(texto_cifrado, claves, permutacion_final):
    # Aplicar la permutación inversa al texto cifrado
    inversa_permutacion_final = generar_permutacion_inversa(permutacion_final)
    texto_cifrado = ''.join([texto_cifrado[inversa_permutacion_final[i] - 1] for i in range(len(texto_cifrado))])

    texto_descifrado = ""
    
    # Determinar la longitud de cada bloque
    bloque_longitudes = [len(clave) for clave in claves]
    
    # Descifrar cada bloque con su clave correspondiente
    inicio = 0
    for longitud in bloque_longitudes:
        bloque_cifrado = texto_cifrado[inicio:inicio + longitud]
        
        # Generar la clave inversa
        clave_inversa = generar_permutacion_inversa(claves.pop(0))
        
        bloque_descifrado = [bloque_cifrado[clave_inversa[i] - 1] for i in range(longitud)]
        texto_descifrado += ''.join(bloque_descifrado)
        
        inicio += longitud
    
    return texto_descifrado
