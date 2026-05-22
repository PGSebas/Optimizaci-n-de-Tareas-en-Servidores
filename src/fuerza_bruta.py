from itertools import product

# -----------------------------------------
# Verifica dependencias
# -----------------------------------------

def dependencias_cumplidas(tarea, ejecutadas):

    dependencias = tarea[3]

    for dep in dependencias:
        if dep not in ejecutadas:
            return False

    return True


# -----------------------------------------
# Obtiene tareas disponibles
# -----------------------------------------

def obtener_tareas_disponibles(tareas, ejecutadas):

    disponibles = []

    for tarea in tareas:

        nombre = tarea[0]

        # Ignorar tareas ya ejecutadas
        if nombre in ejecutadas:
            continue

        # Verificar dependencias
        if dependencias_cumplidas(tarea, ejecutadas):
            disponibles.append(tarea)

    return disponibles


# -----------------------------------------
# FUERZA BRUTA
# -----------------------------------------

def fuerza_bruta(tareas, num_servidores):

    mejor_tiempo = float('inf')
    mejor_asignacion = None

    # Generar TODAS las asignaciones posibles
    for asignacion in product(range(num_servidores), repeat=len(tareas)):

        cargas = [0] * num_servidores
        ejecutadas = set()

        asignacion_final = []

        solucion_valida = True

        # -----------------------------------------
        # Ejecutar tareas paso a paso
        # -----------------------------------------

        for servidor in asignacion:

            # Obtener tareas disponibles
            disponibles = obtener_tareas_disponibles(
                tareas,
                ejecutadas
            )

            # Si no hay tareas disponibles
            if not disponibles:
                break

            # Ordenar por prioridad
            disponibles.sort(key=lambda x: x[2])

            # Elegir la tarea de mayor prioridad
            tarea = disponibles[0]

            nombre = tarea[0]
            tiempo = tarea[1]
            prioridad = tarea[2]

            # Evitar repetir tareas
            if nombre in ejecutadas:
                solucion_valida = False
                break

            # Ejecutar tarea
            cargas[servidor] += tiempo

            ejecutadas.add(nombre)

            asignacion_final.append(
                (nombre, prioridad, servidor)
            )

        # Verificar si se ejecutaron TODAS las tareas
        if len(ejecutadas) != len(tareas):
            continue

        # Calcular tiempo total
        tiempo_total = max(cargas)

        # Guardar mejor solución
        if tiempo_total < mejor_tiempo:

            mejor_tiempo = tiempo_total
            mejor_asignacion = asignacion_final

    # -----------------------------------------
    # MOSTRAR RESULTADOS
    # -----------------------------------------

    print("\nMEJOR ASIGNACIÓN:\n")

    if mejor_asignacion is None:

        print("No se encontró una solución válida.")
        return

    for tarea in mejor_asignacion:

        nombre = tarea[0]
        prioridad = tarea[1]
        servidor = tarea[2]

        print(f"{nombre}")
        print(f"  Prioridad: {prioridad}")
        print(f"  Servidor: {servidor + 1}\n")

    print("Tiempo total mínimo:", mejor_tiempo)


# -----------------------------------------
# CASO DE PRUEBA GRANDE
# -----------------------------------------

tareas = [
    ("T1", 3, 1, []),
    ("T2", 5, 2, ["T1"]),
    ("T3", 2, 1, ["T1"]),
    ("T4", 4, 3, ["T2"]),
    ("T5", 6, 2, ["T2", "T3"]),
    ("T6", 3, 1, ["T3"]),
    ("T7", 7, 2, ["T4", "T5"])
]

num_servidores = 2

fuerza_bruta(tareas, num_servidores)