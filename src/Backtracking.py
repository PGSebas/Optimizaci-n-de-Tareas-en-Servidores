# -----------------------------------------
# SOLUCIÓN BACKTRACKING
# -----------------------------------------


#dependencias_cumplidas verifica si una tarea puede ser ejecutada, es decir, si todas sus dependencias han sido cumplidas.
def dependencias_cumplidas(tarea, ejecutadas):

    dependencias = tarea[3]

    for dep in dependencias:
        if dep not in ejecutadas:
            return False

    return True

#obtener_tareas_disponibles, las agregamos a una lista que retornaremos al final 
def obtener_tareas_disponibles(tareas, ejecutadas):

    disponibles = []

    for tarea in tareas:

        nombre = tarea[0]

        if nombre in ejecutadas:
            continue

        if dependencias_cumplidas(tarea, ejecutadas):
            disponibles.append(tarea)

    return disponibles

#backtracking es la función principal que implementa el algoritmo de backtracking para encontrar la mejor asignación de tareas a servidores.
def backtracking(tareas,num_servidores,cargas=None,ejecutadas=None,asignacion=None,mejor=None):

    # Inicialización
    if cargas is None:
        cargas = [0] * num_servidores

    if ejecutadas is None:
        ejecutadas = set()

    if asignacion is None:
        asignacion = []

    if mejor is None:
        mejor = {"tiempo": float('inf'), "asignacion": None}

    # Caso base
    if len(ejecutadas) == len(tareas):

        tiempo_total = max(cargas)

        if tiempo_total < mejor["tiempo"]:

            mejor["tiempo"] = tiempo_total
            mejor["asignacion"] = asignacion.copy()

        return mejor

    # Obtener tareas disponibles
    disponibles = obtener_tareas_disponibles(tareas,ejecutadas)

    # Ordenar por prioridad
    disponibles.sort(key=lambda x: x[2])

    # Explorar soluciones
    for tarea in disponibles:

        nombre = tarea[0]
        tiempo = tarea[1]
        prioridad = tarea[2]

        for servidor in range(num_servidores):

            # HACER CAMBIOS
            cargas[servidor] += tiempo

            # PODA
            if max(cargas) >= mejor["tiempo"]:

                cargas[servidor] -= tiempo
                continue

            ejecutadas.add(nombre)

            asignacion.append((nombre, tiempo ,prioridad, servidor))

            # LLAMADA RECURSIVA
            backtracking(tareas,num_servidores,cargas,ejecutadas,asignacion,mejor)

            # DESHACER CAMBIOS
            cargas[servidor] -= tiempo
            ejecutadas.remove(nombre)
            asignacion.pop()

    return mejor

tareas_grande = [
    ("T1", 3, 1, []),
    ("T2", 5, 2, ["T1"]),
    ("T3", 2, 1, ["T1"]),
    ("T4", 4, 3, ["T2"]),
    ("T5", 6, 2, ["T2", "T3"]),
    ("T6", 3, 1, ["T3"]),
    ("T7", 7, 2, ["T4", "T5"]),
    ("T8", 2, 3, ["T6"]),
    ("T9", 5, 1, ["T6"]),
    ("T10", 4, 2, ["T7", "T8"]),
    ("T11", 6, 3, ["T9"]),
    ("T12", 3, 2, ["T10", "T11"])
]

print(backtracking(tareas_grande,2))