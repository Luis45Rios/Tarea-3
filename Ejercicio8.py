"""Crear una función recursiva que permita calcular el factorial de un número. Realiza un 
programa principal donde se lea un entero y se muestre el resultado del factorial."""
def Metodo_Euclides(n1,n2):
    if n1>n2:
        while n1%n2!=0:
            r=n1%n2
            n1=n2
            n2=r
        return n2
    elif n1<n2:
        while n2%n1!=0:
            r=n2%n1
            n2=n1
            n1=r
        return n1
    else:
        return n2

def main():
    print("*MCD*\n Por favor ingrese dos números enteros para calcular su MCD:")
    n1=int(input());n2=int(input())
    print("MCD:",Metodo_Euclides(n1,n2))
    #print("MCD:",Metodo_Euclides(60,48))
    #print("MCD:",Metodo_Euclides(24,16))
    #print("MCD:",Metodo_Euclides(30,78))
    #print("MCD:",Metodo_Euclides(75,120))
    
main()