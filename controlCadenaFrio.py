import random 

# Registro de encargados 
def lista_encargados(cantidad = 5):
    encargados = []
    for i in range (cantidad):
        encargado = {}
        encargado ["id"] = i + 1 
        encargado["nombre"]= input(f"Nombre del encargado {i+1}: ")
        encargados.append(encargado)
    return encargados
       
       
# login 
def login_encargados(correoRegistrado,contraseñaRegistrada,numeroIntentos): #Es una función llamada login_lider que recibe 3 parámetros: el correo y contraseña guardado en el sistema y numeros de intentos
    for intento in range (1,numeroIntentos + 1):  #Crea una variable llamada intento. Genera una secuencia de números: empieza en 1 y termina en numero de intentos y el +1 es por que el ultimo numero no se incluye en range 
        correo=input("Digita tu correo: ")
        contraseña=input("Digita tu contraseña: ")
        if correo==correoRegistrado and contraseña==contraseñaRegistrada: #Sirve para validar las credenciales y finalizar el proceso si son correctas.
        
            print("\n✅ Acceso exitoso")
            print(" Bienvenido al sistema \n ")
           
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

# mediciones de temperaturas
def crear_mediciones_aleatorias(cantidad=100):
    mediciones = []
    for _ in range(cantidad):
        valor = random.randint(1, 20)
        mediciones.append(valor)
    return mediciones

def calcular_promedio(mediciones):
    suma=0
    for medicion in mediciones:
        suma+=medicion
        
        
    promedio=suma/len(mediciones)
    return promedio

def clasificar_promedio_cadena_frio(promedioMedicion):
    if promedioMedicion <= 5:
        return "  temperatura segura"
    elif promedioMedicion <= 15:
        return "c temperatura en observación"
    else:
        return "temperatura peligrosa"