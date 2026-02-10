
from controlDeInventario import lista_asesores, autenticar_usuario,calcular_promedio,clasificar_promedio,crear_mediciones_aleatorias



#1
# CREACION DE ASESORES
print("\n" + "="*40)
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
print(f"📌 Estado de la operación: {estado}\n")
















