# ============================================================ 
# Archivo: Ejercicio 2: Verificación de combustible 
# Curso: SOFT-01 Principios de Programación 1 - Sección SCP0 
# Integrantes: Sebastian Miguel Segura Arias, Valeria Acuña Castillo 
# Fecha: xx/xx/2026 Versión: 1.0 
# Descripción: Verificación de combustible para realizar el viaje
# ============================================================

# Declaración de constantes
RESERVA_COMBUSTIBLE = 10

# Entrada de datos
combustible_disponible = int(input("Ingrese la cantidad de combustible disponible: "))
combustible_ida = int(input("Ingrese el combustible requerido para llegar: "))
combustible_regreso = int(input("Ingrese el combustible requerido para regresar: "))

# Procesamiento / Cálculos
combustible_total_requerido = combustible_ida + combustible_regreso + RESERVA_COMBUSTIBLE
combustible_adicional = combustible_disponible - combustible_total_requerido

# Salidas obligatorias
print("Combustible disponible:", combustible_disponible, "unidades")
print("Combustible requerido para llegar:", combustible_ida, "unidades")
print("Combustible requerido para regresar:", combustible_regreso, "unidades")
print("Reserva de emergencia:", RESERVA_COMBUSTIBLE, "unidades")
print("Combustible total requerido:", combustible_total_requerido, "unidades")
print("Combustible adicional disponible:", combustible_adicional, "unidades")

# Regla de advertencia (condicional simple)
if combustible_adicional < 10:
    print("Advertencia: el margen adicional de combustible es bajo.")