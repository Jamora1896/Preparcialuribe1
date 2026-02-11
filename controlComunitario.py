import random


# Registro de lideres 
def lista_lideres(cantidad= 5):  
    lideres = []
    for i in range(cantidad): #Crea un bucle que se repite cantidad veces.
        lider = {} # Crea un diccionario vacío.
        lider["id"] = i + 1 #Agrega la clave "id" al diccionario.
        lider["nombre"] = input(f"Nombre del lider {i+1}: ") # Pide al usuario el nombre del operador. y f"..." es un f-string para mostrar el número correcto.
        lideres.append(lider) #Agrega el diccionario lider  a la lista lideres.
    return lideres # Devuelve la lista completa de operadores.

# login de lideres 
def login_lider(correoRegistrado,contraseñaRegistrada,numeroIntentos): #Es una función llamada login_lider que recibe 3 parámetros: el correo y contraseña guardado en el sistema y numeros de intentos
    for intento in range (1,numeroIntentos + 1):  #Crea una variable llamada intento. Genera una secuencia de números: empieza en 1 y termina en numero de intentos y el +1 es por que el ultimo numero no se incluye en range 
        correo=input("Digita tu correo: ")
        contraseña=input("Digita tu contraseña: ")
        if correo==correoRegistrado and contraseña==contraseñaRegistrada: #Sirve para validar las credenciales y finalizar el proceso si son correctas.
        
            print("\n✅ Acceso exitoso")
            print(" Bienvenido al sistema EPM ")
           
            return True #Sale inmediatamente de la función.
        else: 
            intentos_restantes = numeroIntentos - intento # operación aritmética que sirve para calcular cuántos intentos de login quedan
        if intentos_restantes > 0: #sirve para verificar si todavía quedan intentos disponibles.
            print(f"\n❌ Credenciales incorrectas. Intentos restantes: {intentos_restantes}\n") #me diga cuantos intentos restantes quedan 
        else:
                print("\n" + "="*40)
                print("\n⛔ Se agotaron los intentos permitidos\n")
                print("="*40 + "\n")
               
    return False #Termina la función.


# mediciones de lecturas
def crear_lecturas_aleatorias(cantidad=20):
    lecturas = []
    for _ in range(cantidad):
        valor = random.randint(1, 20)
        lecturas.append(valor)
    return lecturas

def calcular_promedio(lecturas):
    suma=0
    for lectura in lecturas:
        suma+=lectura
        
        
    promedio=suma/len(lecturas)
    return promedio

def clasificar_promedio_epm(promedioMedicion):
    if promedioMedicion <= 5:
        return " alerta por bajo nivel"
    elif promedioMedicion <= 15:
        return "consumo estable"
    else:
        return "consumo alto que exige abrir compuertas o redistribuir"
            












