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

# -----------------------------------------
# EJEMPLO DE USO
# -----------------------------------------

# FORMATO:
# (nombre, tiempo, prioridad, dependencias)

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

resultado = fuerza_bruta_recursiva(
    tareas,
    num_servidores
)

# -----------------------------------------
# MOSTRAR RESULTADOS
# -----------------------------------------

print("\nMEJOR ASIGNACIÓN:\n")

if resultado["asignacion"] is None:

    print("No se encontró una solución válida.")

else:

    for tarea in resultado["asignacion"]:

        nombre = tarea[0]
        prioridad = tarea[1]
        servidor = tarea[2]

        print(f"{nombre}")
        print(f"  Prioridad: {prioridad}")
        print(f"  Servidor: {servidor + 1}\n")

    print("Tiempo total mínimo:", resultado["tiempo"])


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
