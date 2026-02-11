
from controlDeInventario import lista_asesores, autenticar_usuario,calcular_promedio,clasificar_promedio,crear_mediciones_aleatorias
from monitoreoMetro import lista_operadores,autenticar_operador,crear_mediciones_aleatorias_metro,clasificar_promedio_metro,calcular_promedio
from controlComunitario import lista_lideres,login_lider,crear_lecturas_aleatorias,calcular_promedio,clasificar_promedio_epm
from controlCadenaFrio import lista_encargados, login_encargados, crear_mediciones_aleatorias, calcular_promedio,clasificar_promedio_cadena_frio






#1 GRUPO URIBE
# CREACION DE ASESORES
'''print("\n" + "="*40)
print("👥 Inicio del proceso de creación de asesores")
print("="*40 + "\n")


asesores_registrados = lista_asesores()

# MOSTRAR ASESORES
print("\n✅ Asesores creados correctamente\n")

print("👥 Asesores registrados:")
for asesor in asesores_registrados:
    print(f"ID: {asesor['id']} - Nombre: {asesor['nombre']}")
    

#2 AUTENTICACION DE USUARIOS

print("\n" + "="*40)
print("➡️  Iniciando autenticación del usuario")
print("="*40 + "\n")
correoBD = "correo@gmail.com"
contraseñaBD = "admin123"

todoSalioBien = autenticar_usuario(correoBD, contraseñaBD, 3)

#3 Promedio 

mediciones = crear_mediciones_aleatorias()
promedio = calcular_promedio(mediciones)
estado = clasificar_promedio(promedio)

print("\n" + "="*40)
print("➡️  Iniciando calculo de promedio")
print("="*40 + "\n")
print(f"📊 Promedio de rotación: {promedio:.2f}")
print("\n" + "="*40)
print("➡️  Clasificación de la operación")
print("="*40 + "\n")
print(f"📌 Estado de la operación: {estado}\n")'''



#2 METRO MEDELLIN 
# REGISTRO DE OPERADORES
'''print("\n" + "="*40)
print("👥 Inicio del registro de operadores")
print("="*40 + "\n")


operadores_registrados = lista_operadores()

# MOSTRAR ASESORES
print("\n✅ Operadores creados correctamente\n")

print("👥 Operadores registrados:")
for operador in operadores_registrados:
    print(f"ID: {operador['id']} - Nombre: {operador['nombre']}")

#2 ACCESO DE OPERADORES 

print("\n" + "="*40)
print("➡️  Iniciando acceso del operador")
print("="*40 + "\n")

correoBD = "operador@gmail.com"
contraseñaBD = "operador123"

todoSalioBien = autenticar_operador(correoBD, contraseñaBD, 5)

#3 Promedio 

mediciones = crear_mediciones_aleatorias_metro()
promedio = calcular_promedio(mediciones)
estado = clasificar_promedio_metro(promedio)

print("\n" + "="*40)
print("➡️  Iniciando calculo de promedio")
print("="*40 + "\n")
print(f"📊 Promedio de mediciones: {promedio:.2f}")
print("\n" + "="*40)
print("🏷️ Clasificación del servicio")
print("="*40 + "\n")
print(f"⚙️ Estado del servicio: {estado}\n")'''

#EPM

'''# REGISTRO DE LIDERES
print("\n" + "="*40)
print("👥 Inicio del registro de lideres")
print("="*40 + "\n")


lideres_registrados = lista_lideres()

# MOSTRAR LIDERES
print("\n✅ Lideres creados correctamente\n")

print("👥 Lideres registrados:")
for lider in lideres_registrados:
    print(f"ID: {lider['id']} - Nombre: {lider['nombre']}")

#2 ACCESO DE LIDERES

print("\n" + "="*40)
print("➡️  Iniciando acceso del lider")
print("="*40 + "\n")

correoBD = "lider@gmail.com"
contraseñaBD = "lider123"

todoSalioBien = login_lider(correoBD, contraseñaBD, 2)

#3 Promedio 

lecturas = crear_lecturas_aleatorias()
promedio = calcular_promedio(lecturas)
estado = clasificar_promedio_epm(promedio)

print("\n" + "="*40)
print("➡️  Iniciando calculo de promedio")
print("="*40 + "\n")
print(f"📊 Promedio de mediciones: {promedio:.2f}")
print("\n" + "="*40)
print("🏷️ Clasificación del servicio")
print("="*40 + "\n")
print(f"⚙️ Estado del servicio: {estado}\n")'''


#PLAZA MINORISTA 

# REGISTRO DE ENCARGADOS
print("\n" + "="*40)
print("👥 Inicio del registro de los encargados")
print("="*40 + "\n")


encargados_registrados = lista_encargados()

# MOSTRAR encargados
print("\n✅ Encargados creados correctamente\n")
print("👥 Encargados registrados:")
for encargado in encargados_registrados:
    print(f"ID: {encargado['id']} - Nombre: {encargado['nombre']}")

#2 ACCESO DE encargados 

print("\n" + "="*40)
print("➡️  Iniciando acceso del operador")
print("="*40 + "\n")

correoBD = "encargado@gmail.com"
contraseñaBD = "encargado123"

todoSalioBien = login_encargados (correoBD, contraseñaBD, 3)

#3 Promedio 

mediciones = crear_mediciones_aleatorias()
print("Cantidad inicial:", len(mediciones))
mediciones.pop()
print("Después de pop():", len(mediciones))

buscar = 10
if buscar in mediciones:
    posicion = mediciones.index(buscar)
    mediciones.pop(posicion)
    print("Después de eliminar por posición:", len(mediciones))
promedio = calcular_promedio(mediciones)
estado = clasificar_promedio_cadena_frio(promedio)

print("\n" + "="*40)
print("➡️  Iniciando calculo de promedio")
print("\n" + "="*40)
print(f"📊 Promedio de mediciones: {promedio:.2f}")
print("🏷️ Clasificación del servicio")
print(f"⚙️ Estado del servicio: {estado}")
