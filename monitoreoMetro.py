import random 

#Registro de 5 operadores
def lista_operadores(cantidad=5):
    operadores =[]
    for i in range(cantidad):
        operador = {}
        operador["id"] = i + 1
        operador["nombre"] = input(f"Nombre del operador {i+1}: ")
        operadores.append(operador)
    return operadores

#Validacion de loguin 
def autenticar_operador(correoRegistrado,contraseñaRegistrada,numeroIntentos):
    for intento in range(1,numeroIntentos + 1):  #“Haz esto varias veces, contando los intentos uno por uno”.
        correo=input("Digita tu correo: ")
        contraseña=input("Digita tu contraseña: ")
        if correo==correoRegistrado and contraseña==contraseñaRegistrada:
        
            print("\n✅ Acceso exitoso")
            print(" Bienvenido al sistema Metro ")
           
            return True
        else:
             intentos_restantes = numeroIntentos - intento
        if intentos_restantes > 0:
                print(f"\n❌ Credenciales incorrectas. Intentos restantes: {intentos_restantes}\n")
        else:
                print("\n" + "="*40)
                print("\n⛔ Se agotaron los intentos permitidos\n")
                print("="*40 + "\n")
               
    return False

# mediciones
def crear_mediciones_aleatorias_metro(cantidad=500):
    mediciones = []
    for _ in range(cantidad):
        valor = random.randint(50, 300)
        mediciones.append(valor)
    return mediciones

def calcular_promedio(mediciones):
    suma=0
    for medicion in mediciones:
        suma+=medicion
        
        
    promedio=suma/len(mediciones)
    return promedio

def clasificar_promedio_metro(promedioMedicion):
    if promedioMedicion <= 100:
        return " demora crítica"
    elif promedioMedicion <= 300:
        return "operación normal"
    else:
        return " congestión severa que exige activar plan de contingencia"