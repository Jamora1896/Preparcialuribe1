#Algoritmo 3: Algoritmo para recorrer una lista y obtener un promedio numerico

def calcular_promedio(mediciones):
    suma=0
    for medicion in mediciones:
        suma+=medicion
    promedio=suma/len(mediciones)
    return promedio

def clasificar_promedio(promedioMedicion):
    if promedioMedicion>0 and promedioMedicion<=250:
        return("Operacion detenida por falta de agua")
    elif promedioMedicion>250 and promedioMedicion <=400:
        return("operando con normalidad")
    else:
        return("Deben abrirse las compuertas de la represa")