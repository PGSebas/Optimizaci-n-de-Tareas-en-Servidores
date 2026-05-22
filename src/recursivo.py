# Verifica si las dependencias de una tarea ya fueron ejecutadas
def dependencias_cumplidas(tarea, ejecutadas):

    dependencias = tarea[3]

    for dep in dependencias:
        if dep not in ejecutadas:
            return False

    return True

# Obtiene las tareas disponibles:
# - que no hayan sido ejecutadas
# - y que cumplan dependencias
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

def fuerza_bruta_recursiva(
    tareas,
    num_servidores,
    cargas=None,
    ejecutadas=None,
    asignacion_actual=None,
    mejor_resultado=None
):

    # -----------------------------------------
    # INICIALIZACIÓN
    # -----------------------------------------

    if cargas is None:
        cargas = [0] * num_servidores

    if ejecutadas is None:
        ejecutadas = set()

    if asignacion_actual is None:
        asignacion_actual = []

    if mejor_resultado is None:
        mejor_resultado = {
            "tiempo": float('inf'),
            "asignacion": None
        }

    # -----------------------------------------
    # CASO BASE
    # -----------------------------------------
    # Si todas las tareas fueron ejecutadas
    if len(ejecutadas) == len(tareas):

        tiempo_total = max(cargas)

        # Guardar mejor solución
        if tiempo_total < mejor_resultado["tiempo"]:

            mejor_resultado["tiempo"] = tiempo_total
            mejor_resultado["asignacion"] = asignacion_actual.copy()

        return mejor_resultado

    # -----------------------------------------
    # OBTENER TAREAS DISPONIBLES
    # -----------------------------------------

    tareas_disponibles = obtener_tareas_disponibles(
        tareas,
        ejecutadas
    )

    # -----------------------------------------
    # RESPETAR PRIORIDADES
    # -----------------------------------------
    # prioridad menor = más importante
    tareas_disponibles.sort(key=lambda x: x[2])

    # -----------------------------------------
    # PROBAR CADA TAREA DISPONIBLE
    # -----------------------------------------

    for tarea in tareas_disponibles:

        nombre = tarea[0]
        tiempo = tarea[1]
        prioridad = tarea[2]

        # Probar la tarea en cada servidor
        for servidor in range(num_servidores):

            # HACER CAMBIOS
            cargas[servidor] += tiempo
            ejecutadas.add(nombre)

            asignacion_actual.append(
                (nombre, prioridad, servidor)
            )

            # LLAMADA RECURSIVA
            fuerza_bruta_recursiva(
                tareas,
                num_servidores,
                cargas,
                ejecutadas,
                asignacion_actual,
                mejor_resultado
            )

            # DESHACER CAMBIOS
            cargas[servidor] -= tiempo
            ejecutadas.remove(nombre)
            asignacion_actual.pop()

    return mejor_resultado