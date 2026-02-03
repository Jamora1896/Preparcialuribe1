#Crear una lista de 5 ingenieros (in ingeniero es un diccionario)
import random
import string



#así se crea una lista 
lista= []

for _ in range(1,6):
    
    #así se crea un diccionario 
    diccionario ={}
    
    #diccionario ["id"]=int(input("Digite el id del ingeniero: "))
    diccionario["id_entero"] = random.randint(0, 999999) #id entero generado por python de forma aleatoria no negativo
    
    diccionario["id_alfanumerico"] = ''.join(random.choices(string.ascii_uppercase + string.digits, k=8)) # id alfanumerico
    
    diccionario ["nombres"]=input("Digita los nombres del ingeniero: ")
    diccionario ["documento"] = input("Digita el documento del ingeniero: ")
    diccionario ["correo"] = input("Digita el correo del ingeniero: ")
    diccionario ["contraseña"]  = input("Digita la contraseña: ")
    
    print(diccionario)
  
     
  

    
    
    