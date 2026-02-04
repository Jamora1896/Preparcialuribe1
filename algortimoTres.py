#Algoritmo 3: Algoritmo para recorrer una lista y obtener un promedio numerico
import random
#Tarea es generar una lista aleatoria de 20 datos que esten entre dos valores (0,450)
lista = [random.randint(0,450) for _ in range(20)]

#lista=[120,250,340,500,301,310,300,40,87,500]

numeroDeElementosDeLista=len(lista) #Tamaño de lista
suma=0

#Un foreach es un for adaptaddo que permite ir elemento por elemento en una lista
for elemento in lista:3
suma+=elemento #Sumar todos los elementos de una lista de numeros

#Obteniendo el promedio de los datos
promedio=suma/numeroDeElementosDeLista
print(lista)
print(promedio)



#Clasificar el promedio obtenido segun las reglas del negocio
if promedio>0 and promedio<=250:
   print("Operacion detenida por falta de agua")
elif promedio>250 and promedio <=400:
   print("operando con normalidad")
else:
    print("Deben abrirse las compuertas de la represa")
   
