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

def cifrar_sustPermu(texto, num_bloques):
    texto_cifrado = ""
    claves = []
    
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
        
        bloque_cifrado = [bloque[clave[i] - 1] for i in range(longitud_bloque)]
        texto_cifrado += ''.join(bloque_cifrado)
    
    # Generar una última permutación completa del texto cifrado
    permutacion_final = generar_permutacion_aleatoria(len(texto_cifrado))
    texto_cifrado = ''.join([texto_cifrado[permutacion_final[i] - 1] for i in range(len(texto_cifrado))])
    
    return texto_cifrado, claves, permutacion_final

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

# Solicitar al usuario seleccionar entre cifrar o descifrar
opcion = input("Selecciona 'c' para cifrar o 'd' para descifrar: ")
    
if opcion == "c":
    # Solicitar al usuario ingresar el texto
    texto = input("Ingrese el texto a cifrar: ")

    # Solicitar al usuario el numero de bloques
    num_bloques = int(input("Ingrese el número de bloques mínimo: "))
    
    texto_cifrado, claves, permutacion_final = cifrar_sustPermu(texto, num_bloques)
    print("Texto Cifrado:", texto_cifrado)
    print("Claves usadas:", claves)
    print("Permutación final:", permutacion_final)

elif opcion == "d":
    texto_cifrado = input("Ingrese el texto cifrado: ")
    claves_texto = input("Ingrese las claves separadas por ';', y para cada clave separe los numeros con ',': ").split(";")
    claves = []
    for i in claves_texto:
        clave = i.split(",")
        claves.append( [eval(j) for j in clave] )
    permutacion_final = [int(x) for x in input("Ingrese la permutación final (separada por comas): ").split(',')]
    print(permutacion_final)
    
    texto_descifrado = descifrar_sustPermu(texto_cifrado, claves, permutacion_final)
    print("Texto Descifrado:", texto_descifrado)

else:
    print("Opción no válida. Debes seleccionar 'c' o 'd'.")