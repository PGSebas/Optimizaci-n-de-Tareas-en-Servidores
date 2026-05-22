# -----------------------------------------
# DIVIDE Y VENCERÁS
# Optimización de tareas en servidores
# -----------------------------------------

# Verifica dependencias
def dependencias_cumplidas(tarea, ejecutadas):

    dependencias = tarea[3]

    for dep in dependencias:

        if dep not in ejecutadas:
            return False

    return True


# -----------------------------------------
# FUNCIÓN PRINCIPAL
# -----------------------------------------

def divide_y_venceras(
    tareas,
    num_servidores,
    ejecutadas=None
):

    # -----------------------------------------
    # INICIALIZACIÓN
    # -----------------------------------------

    if ejecutadas is None:
        ejecutadas = set()

    # -----------------------------------------
    # CASO BASE
    # -----------------------------------------
    # Si solo queda una tarea
    # -----------------------------------------

    if len(tareas) == 1:

        tarea = tareas[0]

        nombre = tarea[0]
        tiempo = tarea[1]
        prioridad = tarea[2]

        # Verificar dependencias
        if not dependencias_cumplidas(tarea, ejecutadas):

            return {
                "cargas": [0] * num_servidores,
                "asignaciones": []
            }

        # Buscar servidor menos cargado
        cargas = [0] * num_servidores

        servidor = cargas.index(min(cargas))

        cargas[servidor] += tiempo

        ejecutadas.add(nombre)

        return {
            "cargas": cargas,
            "asignaciones": [
                (nombre, prioridad, servidor)
            ]
        }

    # -----------------------------------------
    # DIVIDIR
    # -----------------------------------------

    mitad = len(tareas) // 2

    izquierda = tareas[:mitad]
    derecha = tareas[mitad:]

    # -----------------------------------------
    # VENCER
    # -----------------------------------------

    resultado_izq = divide_y_venceras(
        izquierda,
        num_servidores,
        ejecutadas
    )

    resultado_der = divide_y_venceras(
        derecha,
        num_servidores,
        ejecutadas
    )

    # -----------------------------------------
    # COMBINAR
    # -----------------------------------------

    cargas_finales = [0] * num_servidores

    for i in range(num_servidores):

        cargas_finales[i] = (
            resultado_izq["cargas"][i]
            +
            resultado_der["cargas"][i]
        )

    asignaciones_finales = (
        resultado_izq["asignaciones"]
        +
        resultado_der["asignaciones"]
    )

    return {
        "cargas": cargas_finales,
        "asignaciones": asignaciones_finales
    }

