# ============================================================
# Archivo: ejercicio_seis.py
# Curso: SOFT-01 Principios de Programación 1 - Sección SCP0
# Integrantes: Sebastian Miguel Segura Arias, Valeria Acuña Castillo
# Fecha: 09/11/2026 Versión: 2.0
# Descripción: Simulación del viaje hacia el destino
# ============================================================

# Declaración de constantes
CONSUMO_COMBUSTIBLE_DIA = 8
CONSUMO_OXIGENO_TRIPULANTE = 2
CONSUMO_ENERGIA_DIA = 5
CONSUMO_PROVISIONES_TRIPULANTE = 1

# Entrada de datos
dias_viaje = int(input("Ingrese la cantidad de días del viaje: "))
cant_tripulantes = int(input("Ingrese la cantidad de tripulantes: "))
combustible_disponible = int(input("Ingrese el combustible disponible: "))
oxigeno_disponible = int(input("Ingrese el oxígeno disponible: "))
energia_disponible = int(input("Ingrese la energía disponible: "))
provisiones_disponibles = int(input("Ingrese las provisiones disponibles: "))

# Consumo diario según tripulación
consumo_oxigeno_dia = cant_tripulantes * CONSUMO_OXIGENO_TRIPULANTE
consumo_provisiones_dia = cant_tripulantes * CONSUMO_PROVISIONES_TRIPULANTE

# Variables de control
dia_actual = 1
dias_completados = 0
puede_continuar = True

# Ciclo de simulación del viaje
while dia_actual <= dias_viaje and puede_continuar:
    if (combustible_disponible >= CONSUMO_COMBUSTIBLE_DIA and
        oxigeno_disponible >= consumo_oxigeno_dia and
        energia_disponible >= CONSUMO_ENERGIA_DIA and
        provisiones_disponibles >= consumo_provisiones_dia):
        
        combustible_disponible = combustible_disponible - CONSUMO_COMBUSTIBLE_DIA
        oxigeno_disponible = oxigeno_disponible - consumo_oxigeno_dia
        energia_disponible = energia_disponible - CONSUMO_ENERGIA_DIA
        provisiones_disponibles = provisiones_disponibles - consumo_provisiones_dia
        dias_completados = dias_completados + 1
        
        print("Día", dia_actual, "| Combustible:", combustible_disponible, "| Oxígeno:", oxigeno_disponible, "| Energía:", energia_disponible, "| Provisiones:", provisiones_disponibles)
        dia_actual = dia_actual + 1
    else:
        puede_continuar = False

# salidas finales
if puede_continuar:
    print("La nave llegó al destino en", dias_completados, "días.")
    print("Recursos restantes -> Combustible:", combustible_disponible, "| Oxígeno:", oxigeno_disponible, "| Energía:", energia_disponible, "| Provisiones:", provisiones_disponibles)
else:
    recursos_insuficientes = ""
    if combustible_disponible < CONSUMO_COMBUSTIBLE_DIA:
        recursos_insuficientes = recursos_insuficientes + "Combustible "
    if oxigeno_disponible < consumo_oxigeno_dia:
        recursos_insuficientes = recursos_insuficientes + "Oxígeno "
    if energia_disponible < CONSUMO_ENERGIA_DIA:
        recursos_insuficientes = recursos_insuficientes + "Energía "
    if provisiones_disponibles < consumo_provisiones_dia:
        recursos_insuficientes = recursos_insuficientes + "Provisiones "
        
    print("Viaje interrumpido en el día", str(dia_actual) + ".")
    print("Recurso(s) insuficiente(s):", recursos_insuficientes)
    print("Días completados:", dias_completados)