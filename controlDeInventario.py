import random

#Registro de 5 asesores de tienda
def lista_asesores(cantidad=5):
    asesores =[]
    for i in range(cantidad):
        asesor = {}
        asesor["id"] = i + 1
        asesor["nombre"] = input(f"Nombre del asesor {i+1}: ")
        asesores.append(asesor)
    return asesores

#Validacion de loguin 
def autenticar_usuario(correoRegistrado,contraseñaRegistrada,numeroIntentos):
    for intento in range(1,numeroIntentos + 1):  #“Haz esto varias veces, contando los intentos uno por uno”.
        correo=input("Digita tu correo: ")
        contraseña=input("Digita tu contraseña: ")
        if correo==correoRegistrado and contraseña==contraseñaRegistrada:
        
            print("\n✅ Autenticación exitosa")
            print("   Bienvenido al sistema")
           
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
def crear_mediciones_aleatorias(cantidad=100):
    mediciones = []
    for _ in range(cantidad):
        valor = random.randint(40, 500)
        mediciones.append(valor)
    return mediciones

def calcular_promedio(mediciones):
    suma=0
    for medicion in mediciones:
        suma+=medicion
        
        
    promedio=suma/len(mediciones)
    return promedio

def clasificar_promedio(promedioMedicion):
    if promedioMedicion <= 250:
        return " Baja rotación: revisar estrategia de ventas"
    elif promedioMedicion <= 400:
        return " Rotación normal: operación estable"
    else:
        return " Alta rotación: se requiere reabastecimiento"
