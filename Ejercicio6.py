"""Diseñar una función que calcule el área y el perímetro de una circunferencia. 
Utiliza dicha función en un programa principal que lea el radio de una circunferencia y 
muestre su área y perímetro."""
from math import pi

def calculos(radio):
    area=pi*radio*radio
    perimetro=2*pi*radio
    print("El área es:",round(area,2),"\n", "El perímetro es:",round(perimetro,2))
def main():
    print("*Operaciones con Circunferencias*")
    rad=int(input("Por favor ingrese el radio de la circunferencia: "))
    calculos(rad)
main()