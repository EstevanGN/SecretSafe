import random
import math

def primesInRange(x, y):
    prime_list = []
    for n in range(x, y):
        isPrime = True

        for num in range(2, n):
            if n % num == 0:
                isPrime = False
                
        if isPrime:
            prime_list.append(n)
    return prime_list

prime_list = primesInRange(5,30)
p = random.choice(prime_list)
q = random.choice(prime_list)
n=p*q
phin=(p-1)*(q-1)
invertibles=[]
for i in range(2,phin):
    if math.gcd(i,phin)==1:
        invertibles.append(i)
a=random.choice(invertibles)
print(a,p,q)
print(invertibles)
for i in invertibles:
    if (a*i)%phin==1:
        b=i
        break

print("n es:",n,"p es:",p,"q es:",q,"a es:",a,"b es:",b)
ABC=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
M=input("Ingresa tu mensaje\n")
M=M.upper()
Mnumber=[]
for i in range(len(M)):
   Mnumber.append(ABC.index(M[i]))
Cnumber=[]
for i in range(len(M)):
   Cnumber.append((Mnumber[i]**a)%n)
print(Mnumber)
print(Cnumber)
C=''
for i in range(len(Cnumber)):
   C=C+ABC[Cnumber[i]]
print(C)   

