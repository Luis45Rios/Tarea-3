"""Crea un programa que pida dos número enteros al usuario y diga si alguno de ellos es 
múltiplo del otro. Crea una función EsMultiplo que reciba los dos números, y devuelve si el 
primero es múltiplo del segundo."""
def EsMultiplo(num1,num2):
    try:
        if num1%num2==0:
            print(f"El numero {num1} es multiplo de {num2}")
        else: 
            print(f"El numero {num1} no es multiplo de {num2}")
    except Exception as e:
        print("¡Error!Los valores ingresados no son enteros")
EsMultiplo(3,21)
EsMultiplo(20,5)