"""Crear una subrutina llamada “Login”, que recibe un nombre de usuario y una contraseña y 
te devuelve Verdadero si el nombre de usuario es “usuario1” y la contraseña es “asdasd”. 
Además recibe el número de intentos que se ha intentado hacer login y si no se ha podido hacer 
login incremente este valor.

Crear un programa principal donde se pida un nombre de usuario y una contraseña y se intente hacer login, solamente tenemos tres oportunidades para intentarlo."""
def Login (nombre_usuario,contraseña,n):
    if nombre_usuario =="usuario1" and contraseña== "asdasd": 
        n=0
        return True
    else:
        n+=1
        return False

def main():
    global n
    n=0
    while n<3:
        usuario=str(input("Por favor ingrese su nombre de usuario: "))
        clave=str(input("Por favor ingrese su clave: "))
        if n<3 and Login(usuario,clave,n)==True:
            print("Acceso correcto")
            pass
        else:
            print("El usuario o la clave son incorrectos")
            n+=1
    if n==3:
        print("Ha superado el número de intentos, vuelva más tarde")
main()