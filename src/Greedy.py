# -----------------------------------------
# SOLUCIÓN GREEDY
# -----------------------------------------

# Verifica dependencias
def dependencias_cumplidas(tarea, ejecutadas):

    dependencias = tarea[3]

    for dep in dependencias:
        if dep not in ejecutadas:
            return False

    return True

# Obtiene tareas disponibles
def obtener_tareas_disponibles(tareas, ejecutadas):

    disponibles = []

    for tarea in tareas:

        nombre = tarea[0]

        if nombre in ejecutadas:
            continue

        if dependencias_cumplidas(tarea, ejecutadas):
            disponibles.append(tarea)

    return disponibles


def greedy(tareas, num_servidores):

    cargas = [0] * num_servidores

    ejecutadas = set()

    asignacion = []

    # Mientras falten tareas
    while len(ejecutadas) < len(tareas):

        # Obtener tareas disponibles
        disponibles = obtener_tareas_disponibles(tareas,ejecutadas)

        # Ordenar por prioridad
        disponibles.sort(key=lambda x: x[2])

        # Elegir tarea más importante
        tarea = disponibles[0]

        nombre = tarea[0]
        tiempo = tarea[1]
        prioridad = tarea[2]

        # Elegir servidor menos cargado
        servidor = cargas.index(min(cargas))

        # Asignar tarea
        cargas[servidor] += tiempo

        ejecutadas.add(nombre)

        asignacion.append((nombre,tiempo , prioridad, servidor))

    return "tiempo:" + str(max(cargas)), asignacion


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

print(greedy(tareas_grande,2))