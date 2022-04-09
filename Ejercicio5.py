"""Crea una función “calcularMaxMin” que recibe una lista con valores numéricos y devuelve 
el valor máximo y el mínimo. Crea un programa que pida números por teclado y muestre el máximo 
y el mínimo, utilizando la función anterior."""
def calculadoraMaxMin(lista_num):
        maximo=max(lista_num)
        minimo=min(lista_num)
        print("Máximo:",maximo)
        print("Mínimo",minimo)

def main():
    print("*Máximo y mínimo de una lista*")
    n1=int(input("Por favor, ingrese la cantidad de valores que deseas analizar: "))
    lista=[]
    print("Por favor, ingrese los valores: ")
    for i in range(0,n1):
        n2=int(input())
        lista.append(n2)
    calculadoraMaxMin(lista)
main()