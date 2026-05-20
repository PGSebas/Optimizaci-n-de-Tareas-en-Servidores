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