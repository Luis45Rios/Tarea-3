"""Crear una función que calcule la temperatura media de un día a partir de la temperatura 
máxima y mínima. Crear un programa principal, que utilizando la función anterior, vaya pidiendo 
la temperatura máxima y mínima de cada día y vaya mostrando la media. El programa pedirá 
el número de días que se van a introducir."""
def Temperatura (Tmin,Tmax):
    Tmed=(Tmax+Tmin)/2
    print("La temperatura media es:",Tmed)

def main ():
    print("*Temperatura diaria*")
    n1=int(input("Ingrese el número de días que se desean introducir: "))
    for i in range(0,n1):
        n2=int(input("Ingrese la temperatura mínima: "))
        n3=int(input("Ingrese la temperatura máxima: "))
        Temperatura(n2,n3)
main()