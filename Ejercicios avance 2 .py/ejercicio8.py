# ============================================================
# Archivo: Ejercicio 8: Evaluación del regreso y supervivencia de la tripulación
# Curso: SOFT-01 Principios de Programación 1 - Sección SCP0
# Integrantes: Sebastian Miguel Segura Arias, Valeria Acuña Castillo
# Fecha: 09/11/2026 Versión: 2.0
# Descripción: Evalúa si la nave puede regresar a la Tierra o calcula los días de supervivencia si queda varada.
# ============================================================

# Declaración de constantes
CONSUMO_COMBUSTIBLE_DIA = 8
CONSUMO_OXIGENO_TRIPULANTE = 2
CONSUMO_ENERGIA_DIA = 5
CONSUMO_PROVISIONES_TRIPULANTE = 1

# Entrada de datos
tripulantes = int(input("Ingrese la cantidad de tripulantes: "))
dias_viaje = int(input("Ingrese la cantidad de días del viaje de ida: "))
combustible = int(input("Ingrese el combustible disponible: "))
oxigeno = int(input("Ingrese el oxígeno disponible: "))
energia = int(input("Ingrese la energía disponible: "))
provisiones = int(input("Ingrese las provisiones disponibles: "))

# Cálculos base
consumo_oxigeno_dia = tripulantes * CONSUMO_OXIGENO_TRIPULANTE
consumo_provisiones_dia = tripulantes * CONSUMO_PROVISIONES_TRIPULANTE
combustible_requerido = dias_viaje * CONSUMO_COMBUSTIBLE_DIA

# Regla de decisión: Caso A (puede regresar) vs Caso B (queda varada)
if combustible >= combustible_requerido:
    dia_actual = 1
    puede_regresar = True

    while dia_actual <= dias_viaje and puede_regresar:
        if (combustible >= CONSUMO_COMBUSTIBLE_DIA and
                oxigeno >= consumo_oxigeno_dia and
                energia >= CONSUMO_ENERGIA_DIA and
                provisiones >= consumo_provisiones_dia):

            combustible = combustible - CONSUMO_COMBUSTIBLE_DIA
            oxigeno = oxigeno - consumo_oxigeno_dia
            energia = energia - CONSUMO_ENERGIA_DIA
            provisiones = provisiones - consumo_provisiones_dia

            print("Día", dia_actual, "| Combustible:", combustible, "| Oxígeno:", oxigeno, "| Energía:", energia, "| Provisiones:", provisiones)
            dia_actual = dia_actual + 1
        else:
            puede_regresar = False

    if puede_regresar:
        print("La tripulación regresó exitosamente a la Tierra.")
        print("Recursos restantes -> Combustible:", combustible, "| Oxígeno:", oxigeno, "| Energía:", energia, "| Provisiones:", provisiones)
    else:
        insuficientes = ""
        if combustible < CONSUMO_COMBUSTIBLE_DIA:
            insuficientes = "combustible"
        if oxigeno < consumo_oxigeno_dia:
            if insuficientes != "":
                insuficientes = insuficientes + ", "
            insuficientes = insuficientes + "oxígeno"
        if energia < CONSUMO_ENERGIA_DIA:
            if insuficientes != "":
                insuficientes = insuficientes + ", "
            insuficientes = insuficientes + "energía"
        if provisiones < consumo_provisiones_dia:
            if insuficientes != "":
                insuficientes = insuficientes + ", "
            insuficientes = insuficientes + "provisiones"

        print("El regreso se interrumpió en el día", str(dia_actual) + ".")
        print("Recurso(s) insuficiente(s):", insuficientes)
        print("La tripulación no completó el regreso.")
else:
    dias_oxigeno = oxigeno // consumo_oxigeno_dia
    dias_energia = energia // CONSUMO_ENERGIA_DIA
    dias_provisiones = provisiones // consumo_provisiones_dia

    min_dias = dias_oxigeno
    if dias_energia < min_dias:
        min_dias = dias_energia
    if dias_provisiones < min_dias:
        min_dias = dias_provisiones

    limitantes = ""
    if dias_oxigeno == min_dias:
        limitantes = "oxígeno"
    if dias_energia == min_dias:
        if limitantes != "":
            limitantes = limitantes + ", "
        limitantes = limitantes + "energía"
    if dias_provisiones == min_dias:
        if limitantes != "":
            limitantes = limitantes + ", "
        limitantes = limitantes + "provisiones"

    print("La tripulación quedó varada en el destino.")
    print("Días por oxígeno:", dias_oxigeno)
    print("Días por energía:", dias_energia)
    print("Días por provisiones:", dias_provisiones)
    print("Supervivencia estimada:", min_dias, "días")
    print("Recurso(s) limitante(s):", limitantes)