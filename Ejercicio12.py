"""Queremos crear un programa que trabaje con fracciones a/b. Para representar una fracción 
vamos a utilizar dos enteros: numerador y denominador.

Vamos a crear las siguientes funciones para trabajar con funciones:

Leer_fracción: La tarea de esta función es leer por teclado el numerador y el denominador. 
Cuando leas una fracción debes simplificarla.
Escribir_fracción: Esta función escribe en pantalla la fracción. Si el dominador es 1, se 
muestra sólo el numerador.
Calcular_mcd: Esta función recibe dos número y devuelve el máximo común divisor.
Simplificar_fracción: Esta función simplifica la fracción, para ello hay que dividir 
numerador y dominador por el MCD del numerador y denominador.
Sumar_fracciones: Función que recibe dos funciones n1/d1 y n2/d2, y calcula la suma de las 
dos fracciones. La suma de dos fracciones es otra fracción cuyo numerador=n1*d2+d1*n2 y 
denominador=d1*d2. Se debe simplificar la fracción resultado.
Restar_fracciones: Función que resta dos fracciones: numerador=n1*d2-d1*n2 y 
denominador=d1*d2. Se debe simplificar la fracción resultado.
Multiplicar_fracciones: Función que recibe dos fracciones y calcula el producto, para 
ello numerador=n1*n2 y denominador=d1*d2. Se debe simplificar la fracción resultado.
Dividir_fracciones: Función que recibe dos fracciones y calcula el cociente, para ello 
numerador=n1*d2 y denominador=d1*n2. Se debe simplificar la fracción resultado."""

def Leer_fraccion(a,b):
    return Simplificar_fraccion(a,b)
def Escribir_fraccion(a,b):
    if b!=0:
        return a,b
    if b==1:
        return a
def Calcular_mcd(a,b):
        if a%b==0:
            return b
        elif a%b!=0:
            return Calcular_mcd(b,a%b)
        elif a<b:
            Calcular_mcd(b,a)
        elif b==0:
            return a
def Simplificar_fraccion(a,b):
    simp_a=int(a/Calcular_mcd(a,b))
    simp_b=int(b/Calcular_mcd(a,b))
    return simp_a,simp_b
def Sumar_fracciones(a,b,c,d):
    den=b*d
    num=(a*d)+(b*c)
    return Simplificar_fraccion(num,den)
def Restar_fracciones(a,b,c,d):
    den=b*d
    num=(a*d)-(b*c)
    return Simplificar_fraccion(num,den)
def Multiplicar_fracciones(a,b,c,d):
    num=a*c
    den=b*d
    return Simplificar_fraccion(num,den)
def Dividir_fracciones(a,b,c,d):
    num=a*d
    den=b*c
    return Simplificar_fraccion(num,den)
def main():
    print("*Operaciones con Fracciones*\n Por favor ingresa las fracciones que deseas operar:")
    n1=int(input("Numerador 1: ")); d1=int(input("Denominador 1: "))
    n2=int(input("Numerador 2: ")); d2=int(input("Denominador 2: "))
    a,b=(Escribir_fraccion(n1,d1))
    c,d=(Escribir_fraccion(n2,d2))
    print("Fraccion 1:",Leer_fraccion(a,b))
    print("Fraccion 2:",Leer_fraccion(c,d))
    n1=0
    while n1!=5:
        print("Seleccione el número según la operación que desea realizar:")
        print("1. Suma\n2. Resta\n3. Multiplicación\n4. División\n5. Salir")
        n1=int(input())
        if n1==1:print("Suma:",Sumar_fracciones(a,b,c,d))
        elif n1==2:print("Resta",Restar_fracciones(a,b,c,d))
        elif n1==3:print("Multiplicacion",Multiplicar_fracciones(a,b,c,d))
        elif n1==4:print("Division",Dividir_fracciones(a,b,c,d))
        elif n1==5:print("Salir")
        else: print("El número que ingresó no está en el menú")
    print("Fin de las operaciones")
    #print(Simplificar_fraccion(1,39))
    #print(Sumar_fracciones(4,3,2,5))
    #print(Restar_fracciones(4,3,2,5))
    #print(Multiplicar_fracciones(4,3,2,5))
    #print(Dividir_fracciones(4,3,2,5))
main()