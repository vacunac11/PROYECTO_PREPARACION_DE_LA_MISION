# ============================================================
# Archivo: Ejercicio 7: Actividades de exploración científica
# Curso: SOFT-01 Principios de Programación 1 - Sección SCP0
# Integrantes: Sebastian Miguel Segura Arias, Valeria Acuña Castillo
# Fecha: 09/11/2026 Versión: 2.0
# Descripción: Menú repetitivo de actividades de exploración científica
# ============================================================

# Declaración de constantes
ENERGIA_TERRENO = 8
PUNTOS_TERRENO = 10
ENERGIA_MUESTRA = 12
PROVISIONES_MUESTRA = 2
PUNTOS_MUESTRA = 20
ENERGIA_OBSERVACION = 5
PUNTOS_OBSERVACION = 8

# Entrada de datos
energia_disponible = int(input("Ingrese la energía disponible: "))
provisiones_disponibles = int(input("Ingrese las provisiones disponibles: "))

# Valores iniciales de contadores y acumuladores
puntos_cientificos = 0
actividades_realizadas = 0
muestras_recolectadas = 0
continuar_exploracion = True

# Menú de actividades
while continuar_exploracion:
    print("\n1. Analizar terreno")
    print("2. Recolectar muestra")
    print("3. Realizar observación")
    print("4. Finalizar exploración")
    opcion = int(input("Seleccione una actividad: "))

match opcion:
        case 1:
            if energia_disponible >= ENERGIA_TERRENO:
                energia_disponible = energia_disponible - ENERGIA_TERRENO
                actividades_realizadas = actividades_realizadas + 1
                puntos_cientificos = puntos_cientificos + PUNTOS_TERRENO
                print("Actividad realizada: Analizar terreno. Puntos obtenidos:", PUNTOS_TERRENO)
            else:
                print("Recursos insuficientes para realizar la actividad. La exploración finaliza.")
                continuar_exploracion = False
        case 2:
            if energia_disponible >= ENERGIA_MUESTRA and provisiones_disponibles >= PROVISIONES_MUESTRA:
                energia_disponible = energia_disponible - ENERGIA_MUESTRA
                provisiones_disponibles = provisiones_disponibles - PROVISIONES_MUESTRA
                actividades_realizadas = actividades_realizadas + 1
                muestras_recolectadas = muestras_recolectadas + 1
                puntos_cientificos = puntos_cientificos + PUNTOS_MUESTRA
                print("Actividad realizada: Recolectar muestra. Puntos obtenidos:", PUNTOS_MUESTRA)
            else:
                print("Recursos insuficientes para realizar la actividad. La exploración finaliza.")
                continuar_exploracion = False
        case 3:
            if energia_disponible >= ENERGIA_OBSERVACION:
                energia_disponible = energia_disponible - ENERGIA_OBSERVACION
                actividades_realizadas = actividades_realizadas + 1
                puntos_cientificos = puntos_cientificos + PUNTOS_OBSERVACION
                print("Actividad realizada: Realizar observación. Puntos obtenidos:", PUNTOS_OBSERVACION)
            else:
                print("Recursos insuficientes para realizar la actividad. La exploración finaliza.")
                continuar_exploracion = False
        case 4:
            continuar_exploracion = False
        case _:
            print("Opción no válida.")
# Resumen final
print("\nActividades realizadas:", actividades_realizadas)
print("Muestras recolectadas:", muestras_recolectadas)
print("Puntos científicos:", puntos_cientificos)
print("Energía restante:", energia_disponible, "unidades")
print("Provisiones restantes:", provisiones_disponibles, "unidades")