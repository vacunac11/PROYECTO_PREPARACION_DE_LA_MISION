# ============================================================ 
# Archivo: Ejercicio 1 Cálculo de recursos necesarios para una misión 
# Curso: SOFT-01 Principios de Programación 1 - Sección SCP0 
# Integrantes: Sebastian Miguel Segura Arias, Valeria Acuña Castillo 
# Fecha: xx/xx/xxxx Versión: 1.0 
# Descripción: Analiza los recursos necesarios para una misión espacial y calcula los requerimientos de combustible, oxígeno, energía y provisiones.
# ============================================================

# Declaración de constantes
RESERVA_COMBUSTIBLE = 10

# Entrada de datos
nombre_mision = input("Ingrese el nombre de la misión: ")
cant_tripulantes = int(input("Ingrese la cantidad de tripulantes: "))
dias_viaje = int(input("Ingrese los días de viaje estimados: "))

# Procesamiento / Cálculos
combustible_ida = dias_viaje * 8
combustible_regreso = dias_viaje * 8
combustible_total_requerido = combustible_ida + combustible_regreso + RESERVA_COMBUSTIBLE

oxigeno_requerido = dias_viaje * cant_tripulantes * 2 + 5
energia_requerida = dias_viaje * 5 + 10
provisiones_requeridas = dias_viaje * cant_tripulantes + 3

# Salida esperada
print("Misión:", nombre_mision)
print("Tripulantes:", cant_tripulantes)
print("Duración estimada hasta el destino:", dias_viaje, "días")
print("Combustible para llegar:", combustible_ida, "unidades")
print("Combustible para regresar:", combustible_regreso, "unidades")
print("Reserva de combustible:", RESERVA_COMBUSTIBLE, "unidades")
print("Combustible total requerido:", combustible_total_requerido, "unidades")
print("Oxígeno requerido:", oxigeno_requerido, "unidades")
print("Energía requerida:", energia_requerida, "unidades")
print("Provisiones requeridas:", provisiones_requeridas, "unidades")