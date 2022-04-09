"""El día juliano correspondiente a una fecha es un número entero que indica los días que han 
transcurrido desde el 1 de enero del año indicado. Queremos crear un programa principal que 
al introducir una fecha nos diga el día juliano que corresponde. Para ello podemos hacer las 
siguientes subrutinas:

LeerFecha: Nos permite leer por teclado una fecha (día, mes y año).
DiasDelMes: Recibe un mes y un año y nos dice los días de ese mes en ese año.
EsBisiesto: Recibe un año y nos dice si es bisiesto.
Calcular_Dia_Juliano: recibe una fecha y nos devuelve el día juliano."""

def DiasDelMes(mes,anio,dic_month):
    if EsBisiesto(anio)==True:
        dic_month.update({2:29})
    return dic_month[mes]

def EsBisiesto(anio):
    if anio%4==0 and (anio%100!=0 or anio%400==0):
        print("Año bisiesto")
        return True
    else:
        print("Año no bisiesto")
        return False

def LeerFecha(dia,mes,anio,dic_nombre):
    print(" ")
    print(dia,"de",dic_nombre[mes],"de",anio)

def Calcular_Dia_Juliano(dia,mes,anio):
    dic_month={1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
    dic_nombre={1:"Enero",2:"Febrero",3:"Marzo",4:"Abril",5:"Mayo",6:"Junio",7:"Julio",8:"Agosto",9:"Septiembre",10:"Octubre",11:"Noviembre",12:"Diciembre"}
    LeerFecha(dia,mes,anio,dic_nombre)
    DiasDelMes(mes,anio,dic_month)
    suma=0
    for d in range(1,mes):
        suma=suma+dic_month[d]
    suma+=dia
    return suma
def main():
    print("*Dia Juliano*\n Por favor ingrese la fecha en forma de números (dia/mes/año)")
    dia=int(input());mes=int(input());anio=int(input())
    print("Dia Juliano:",Calcular_Dia_Juliano(dia,mes,anio))
    #print("Dia Juliano:",Calcular_Dia_Juliano(3,3,1996))
    #print("Dia Juliano:",Calcular_Dia_Juliano(1,1,2000))
main()