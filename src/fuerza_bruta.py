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


