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