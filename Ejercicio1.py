"""Crea un función EscribirCentrado, que reciba como parámetro un texto y lo escriba centrado 
en pantalla (suponiendo una anchura de 80 columnas; pista: deberás escribir 40 - longitud/2 
espacios antes del texto). Además subraya el mensaje utilizando el carácter =."""
def EscribirCentrado(column,texto):
    espacio=int(column/2)-(int(len(texto)/2))
    for i in range(0,espacio):
        print(end =" ")
    print(texto)
    for k in range(0,espacio):
        print(end =" ")
    for j in range(0,len(texto)):
        print(end ="=")
EscribirCentrado(80,"Hola mi nombre es Luis Humberto Ríos, tengo 16 años")