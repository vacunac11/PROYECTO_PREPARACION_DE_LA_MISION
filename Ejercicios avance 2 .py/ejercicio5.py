# ==============================================================================
# Archivo: ejercicio_cinco.py
# Curso: SOFT-01 Principios de Programación 1 - Sección SCPO
# Integrantes: Sebastian Miguel Segura Arias, Valeria Acuña Castillo
# Fecha: 09/11/2026
# Versión: 2.0
# Descripción: Selección del destino 
# ==============================================================================

# DECLARACIÓN DE CONSTANTES
CONSUMO_COMBUSTIBLE_DIA = 8
RESERVA_COMBUSTIBLE = 10
CONSUMO_OXIGENO_TRIPULANTE = 2
RESERVA_OXIGENO = 5
CONSUMO_ENERGIA_DIA = 5
ENERGIA_EXPLORACION = 10
CONSUMO_PROVISIONES_TRIPULANTE = 1
RESERVA_PROVISIONES = 3

# ENTRADA DE DATOS INICIALES
print(" SELECCIÓN DEL DESTINO Y AUTORIZACIÓN DE LA MISIÓN ")
nombre_mision = input("Ingrese el nombre de la misión: ")
cant_tripulantes = int(input("Ingrese la cantidad de tripulantes: "))

print("\n DESTINOS DISPONIBLES ")
print("1. Luna (3 días de viaje)")
print("2. Marte (5 días de viaje)")
print("3. Europa (7 días de viaje)")
opcion_destino = int(input("Seleccione la opción de destino (1-3): "))

# EVALUACIÓN DEL DESTINO 
opcion_valida = True
dias_viaje = 0
nombre_destino = ""

match opcion_destino:
    case 1:
        nombre_destino = "Luna"
        dias_viaje = 3
    case 2:
        nombre_destino = "Marte"
        dias_viaje = 5
    case 3:
        nombre_destino = "Europa"
        dias_viaje = 7
    case _:
        opcion_valida = False

# EVALUACIÓN Y PROCESAMIENTO
if not opcion_valida:
    print("Opción de destino no válida. La misión no puede planificarse.")
else:
    print("\nIngrese los recursos disponibles para la misión:")
    combustible_disponible = int(input("Ingrese el combustible disponible: "))
    oxigeno_disponible = int(input("Ingrese el oxígeno disponible: "))
    energia_disponible = int(input("Ingrese la energía disponible: "))
    provisiones_disponibles = int(input("Ingrese las provisiones disponibles: "))

    # Cálculos de requerimientos 
    combustible_ida = dias_viaje * CONSUMO_COMBUSTIBLE_DIA
    combustible_regreso = dias_viaje * CONSUMO_COMBUSTIBLE_DIA
    combustible_total_requerido = combustible_ida + combustible_regreso + RESERVA_COMBUSTIBLE
    oxigeno_requerido = (dias_viaje * cant_tripulantes * CONSUMO_OXIGENO_TRIPULANTE) + RESERVA_OXIGENO
    energia_requerida = (dias_viaje * CONSUMO_ENERGIA_DIA) + ENERGIA_EXPLORACION
    provisiones_requeridas = (dias_viaje * cant_tripulantes * CONSUMO_PROVISIONES_TRIPULANTE) + RESERVA_PROVISIONES

    # Verificación de recursos 
    lanzamiento_autorizado = (
        combustible_disponible >= combustible_total_requerido and
        oxigeno_disponible >= oxigeno_requerido and
        energia_disponible >= energia_requerida and
        provisiones_disponibles >= provisiones_requeridas
    )

    # SALIDA ESPERADA 
    print("Misión:", nombre_mision)
    print("Destino:", nombre_destino)
    print("Tripulantes:", cant_tripulantes)
    print("Duración del viaje de ida:", dias_viaje, "días")
    print("\nREQUISITOS DE RECURSOS")
    print("Combustible para llegar:", combustible_ida, "unidades")
    print("Combustible para regresar:", combustible_regreso, "unidades")
    print("Reserva de combustible:", RESERVA_COMBUSTIBLE, "unidades")
    print("Combustible total requerido:", combustible_total_requerido, "unidades")
    print("Oxígeno requerido:", oxigeno_requerido, "unidades")
    print("Energía requerida:", energia_requerida, "unidades")
    print("Provisiones requeridas:", provisiones_requeridas, "unidades")


    if lanzamiento_autorizado:
        print("Lanzamiento autorizado.")
    else:
        print("Lanzamiento no autorizado. La misión debe ser revisada.")