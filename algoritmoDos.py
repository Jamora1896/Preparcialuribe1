#Algoritmo 2: Rutina para LOGIN de usuario con correo y contraseña, se permiten hasta 3 intentos

#Variables de datos almacenados en BD
correoBD="correo@gmail.com"
contraseñaBD="admin123"


intentosPermitidos=3
contadorIntentos=0

#ciclo para controlar el numero de intentos
while contadorIntentos<intentosPermitidos:

    #Variables que digita el usuarios
    correoDigitado=input("Digita tu correo: ")
    contraseñaDigita=input("Digita tu contraseña: ")

    #Evaluar si el login es efectivo
    if correoDigitado==correoBD and contraseñaDigita==contraseñaBD:
        print("Login exitoso")

        #Se rompe/termina el ciclo
        break

    else:
        
        contadorIntentos+=1
        intentosRestantes = intentosPermitidos - contadorIntentos
        
        print("Cuidado! Credenciales incorrectas")
        print(f"Intento número: {contadorIntentos}")
        print(f"Intentos restantes: {intentosRestantes}\n")
        
    if contadorIntentos == intentosPermitidos:
        print("Has superado el número máximo de intentos!")
        