#Algoritmo 2: Rutina para LOGIN de usuario con correo y contraseña, se permiten hasta 3 intentos

def autenticar_usuario(correoRegistrado,contraseñaRegistrada,numeroIntentos):
    for intento in range(1,numeroIntentos):
        correo=input("Digita tu correo: ")
        contraseña=input("Digita tu contraseña: ")
        if correo==correoRegistrado and contraseña==contraseñaRegistrada:
            print("✅ Login OK")
            return True
        else:
            #Calcular el numero de intentos restantes OJO
            print("✖️  Fallaste en el Login")
    return False