import sys
import timeit
from collections import defaultdict

dd = defaultdict(list) #Mapa donde se almacenaran los resultados
def main():
    ft = False #Variable para controlar cuando se muestra el tiempo y cuando no
    for i in sys.argv:
        #Opcion para mostrar el tiempo de ejecucion
        if i == '--t':
            ft = True
        else:
            if i != "PDinamica.py":
                f = open(i, "r")
                if f.mode == "r":
                    contents = f.read()  #Se lee el fichero y se guarda su contenido
                f.close()
                pDinamica(contents, ft)
                pDinamica(contents, ft)

def count(a, b, m, n):
    # Si ambas String estan vacias, o si es la segunda string la que lo esta, devuelve 1
    if ((m == 0 and n == 0) or n == 0):
        return 1

    # Si la primera string esta vacia pero la segunda no, devuelve 0.
    if (m == 0):
        return 0

    # Si los ultimos caracteres son iguales, se repetira el siguiente procedimiento
    # para las strings restantes:
    # 1. Se consideran los ultimos caracteres en ambas strings.
    # 2. Se ignoran los ultimos caracteres de la primera string.
    if (a[m - 1] == b[n - 1]):
        return (count(a, b, m - 1, n - 1) +
                count(a, b, m - 1, n))
    else:
        # Si los ultimos caracteres son diferentes, se ignora el ultimo caracter
        # de la primera string y se vuelve a repetir para la string restante.
        return count(a, b, m - 1, n)

#Analizamos si ya se ha recibido el dato. En caso contrario se calcula.
#Si ya se han recibido, se devuelve el valor.
def pDinamica(contents, ft):
    #Caso en que se encuentre ya en el mapa.
    if dd.has_key(contents):
        print("Ya se ha probado")
        #Se calculan los tiempo de inicio y fin para saber cuanto tarda en mostrar el valor.
        if ft == True:
            tiempo_inicio = timeit.default_timer()
        res = dd[contents]  #Se muestra el valor.
        if ft == True:
            tiempo_final = timeit.default_timer() - tiempo_inicio
            tiempo_final = str(tiempo_final * 100)
            print ("El tiempo final es de %s mseg" % repr(tiempo_final))
    #Caso en que no se encuentre en el mapa.
    else:
        #Se divide la String en dos mediante su separador (el guion)
        temp = contents.split('-')
        #Se calculan los tiempo de inicio y fin para saber cuanto tarda en calcular el valor.
        if ft == True:
            tiempo_inicio = timeit.default_timer()
        #Se le pasa al metodo anterior la String dividida para que la trate
        res = count(temp[0], temp[1], len(temp[0]), len(temp[1]))
        dd[contents].append(res) #Se añade el resultado al mapa
        if ft == True:
            tiempo_final = timeit.default_timer() - tiempo_inicio
            tiempo_final = str(tiempo_final * 100)
            print ("El tiempo final es de %s mseg" % repr(tiempo_final))
    print (res)

if __name__ == "__main__":
    main()
