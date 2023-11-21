import random
from Crypto.Util import number

# Función para generar un número primo aleatorio grande
def generate_prime():
    p=number.getPrime(8)
    while(p<126):
        p=number.getPrime(8)
    return p


def suma_elip(p,q,a,P):
    if (p!=q and q[0]!=p[0]):
        s=(q[1]-p[1])%P*pow(q[0]-p[0],-1,P)
    elif (p!=q and q[0]==p[0]):
        return (0,0)
    else:
        s=((3*p[0]*p[0])+a)%P*pow(2*p[1],-1,P)   
    s=s%P
    r=((s*s-p[0]-q[0])%P,(s*(p[0]-((s*s-p[0]-q[0])%P))-p[1])%P)
    return r

def puntos_elipse(a,b,P):
    x=[i for i in range(P)]
    cuad=[(c*c*c+a*c+b)%P for c in x]
    j=int((P-1)/2)
    RC=[(pow(cuad[i],j,P)==1) for i in range(P)]
    y=[(P,P) for i in range(P)]
    for i in range(P):
        if RC[i]:   
            if P%4==3:
                j=int((P+1)/4)
                k1=pow(cuad[i],j,P)
                k2=-k1%P
                y[i]=(k1,k2)
            elif P%8==5:
                j1=int((P-1)/4)
                if pow(cuad[i],j1,P)==1:
                    j=int((P+3)/8)
                    k1=pow(cuad[i],j,P)
                    k2=-k1%P
                    y[i]=(k1,k2)
                elif pow(cuad[i],j1,P)==P-1:
                    j=int((P-5)/8)
                    k1=(2*cuad[i]*(pow(4*cuad[i],j,P)))%P
                    k2=-k1%P
                    y[i]=(k1,k2) 
    puntos=[]
    for i in range(P):
        if(y[i]!=(P,P)):
            puntos.append((x[i],y[i][0]))
            puntos.append((x[i],y[i][1]))
    return puntos


def encontrar_gen(conjunto,a,P):
    random.shuffle(conjunto)
    for elemento in conjunto:
        generado = {elemento}
        s=elemento
        for i in range(len(conjunto)):
            s=suma_elip(s, elemento,a,P)
            if s==(0,0) and generado != set(conjunto):
                break
            generado.add(s)
            if generado == set(conjunto):
                return elemento
    return None


def Encriptar(mensaje):
    chars=[char for char in mensaje]
    alpha=None
    while(alpha==None):
            P=generate_prime()
            a=random.randint(1,P-1)
            b=random.randint(1,P-1)
            d=random.randint(0,P-1)
            k=random.randint(0,P-1)
            alpha=encontrar_gen(puntos_elipse(a,b,P),a,P)
    beta=alpha
    for i in range(d-1):
        beta=suma_elip(beta,alpha,a,P)
    y0=alpha
    for i in range(k-1):
        y0=suma_elip(y0,alpha,a,P)
    y=beta
    for i in range(k-1):
        y=suma_elip(y,beta,a,P)
    encrypt=[]
    for i in chars:
        x=(ord(i),ord(i))
        y1=y[0]*x[0]%P
        y2=y[1]*x[1]%P
        #e[0] es el encriptado, e[1] es el a de la eliptica, P,alpha y beta son la clave publica, d es la privada
        encrypt.append((y1,y2))
    e=(a,P,d,y0,encrypt,alpha,beta)
    return e

def Desncriptar(a,P,d,y,encrypt):
    c=y
    for i in range(d-1):
        c=suma_elip(c,y,a,P)
    c1=pow(c[0],-1,P)
    c2=pow(c[1],-1,P)
    x=""
    for i in encrypt:
        x1=i[0]*c1%P
        x2=i[1]*c2%P
        ch=chr(x1)
        x=x+ch
    return x

            

x1=str(input("Ingresa el mensaje"))

e=Encriptar(x1)
y=Desncriptar(e[0],e[1],e[2],e[3],e[4])
print("----------------------------------------------------------------------------------------------------------")
print("La clave publica es: (P=",e[1],", alpha=",e[4],", beta=",e[5],")")
print("La clave privada es:",e[2])
print("El texto claro es ",x1)
print("El mensaje cifrado es ",e[3],e[4])
print("El mensaje descifrado es ",y)
