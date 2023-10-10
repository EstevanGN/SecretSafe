
import random
ABC=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
K=[5,7,11,15,17,19,21,23,25]  #¿QUE PASA CUANDO ES 25?     
M=input("Ingresa tu mensaje\n")
M=M.upper()
Mnumber=[]
for i in range(len(M)):
   Mnumber.append(ABC.index(M[i]))
print(K)
k=int(input("Elige la clave que deseas para tu mensaje dada la lista anterior\n")) #k=random.choice(K)
Cnumber=[]
for i in range(len(M)):
   Cnumber.append((Mnumber[i]**k)%26)
print(Mnumber)
print(Cnumber)
C=''
for i in range(len(Cnumber)):
   C=C+ABC[Cnumber[i]]
print(C)   