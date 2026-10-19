# ============================================================ 
# Archivo: Ejercicio 3: Verificación del soporte para la tripulación 
# Curso: SOFT-01 Principios de Programación 1 - Sección SCP0 
# Integrantes: Sebastian Miguel Segura Arias, Valeria Acuña Castillo 
# Fecha: 18/10/2026 Versión: 1.0 
# Descripción: Verificación del soporte para la tripulación
# ============================================================

# Entrada de datos
oxigeno_disponible = int(input("Ingrese la cantidad de oxígeno disponible: "))
oxigeno_requerido = int(input("Ingrese la cantidad de oxígeno requerido: "))
provisiones_disponibles = int(input("Ingrese la cantidad de provisiones disponibles: "))
provisiones_requeridas = int(input("Ingrese la cantidad de provisiones requeridas: "))

# Regla de decisión (condicional doble)
if oxigeno_disponible >= oxigeno_requerido and provisiones_disponibles >= provisiones_requeridas:
    print("La nave posee recursos suficientes para la tripulación.")
else:
    print("La nave no posee recursos suficientes para la tripulación.")