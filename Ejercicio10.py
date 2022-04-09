"""Escribir dos funciones que permitan calcular:

La cantidad de segundos en un tiempo dado en horas, minutos y segundos.
La cantidad de horas, minutos y segundos de un tiempo dado en segundos.
Escribe un programa principal con un menú donde se pueda elegir la opción de convertir a 
segundos, convertir a horas,minutos y segundos o salir del programa."""

def segundos(h,min,s):
    horas=h*3600
    minutos=min*60
    segundos=horas+minutos+s
    return segundos

def H_MIN_SEC(sec):
    horas=int(sec/3600)
    r=(sec/3600)-horas
    minutos=int(r*60)
    r2=(r*60)-minutos
    segundos=int(r2*60)
    return horas, minutos,segundos
def main():
    print("Segundos:",segundos(2,30,15))
    print("Horas,Minutos, Segundos:",H_MIN_SEC(9015))
main()