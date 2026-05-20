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
