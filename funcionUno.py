#Algoritmo 1: Crea una lista de 5 ingenieros (1 ingeniero es un diccionario)
import random


# estructura basica de una funcion:
def crear_lista_ingenieros(cantidadIngenieros):
    ingenieros=[]
    for _ in range(cantidadIngenieros):
        nuevoIngeniero={}
        nuevoIngeniero["id"]=int(input("id: "))
        nuevoIngeniero["nombres"]=input("nombres: ")
        ingenieros.append(nuevoIngeniero)
    return ingenieros 


#Funcion para crear una lista de 20 o N mediciones forma aleatoria


def crear_lista_mediciones(cantidad):
    mediciones = []              # Lista vacía
    for _ in range(cantidad):    # Repite N veces
        valor = random.randint(1, 100)  # Número aleatorio
        mediciones.append(valor) # Agrega a la lista
    return mediciones

lista = crear_lista_mediciones(20)
print(lista)




