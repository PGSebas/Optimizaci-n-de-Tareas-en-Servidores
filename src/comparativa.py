import time

from Backtracking import *
from divide_y_venceras import *
from fuerza_bruta import *
from Greedy import *
from recursivo import *

datos = [
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

num_servidores = 2
# -----------------------------------------
# Medir tiempo
# -----------------------------------------
def medir_tiempo(funcion, datos, num_servidores):
    inicio = time.perf_counter()

    try:
        funcion(datos, num_servidores)
    except Exception as e:
        print(f"Error en {funcion.__name__}: {e}")
        return None

    fin = time.perf_counter()
    return fin - inicio

# -----------------------------------------
# Algoritmos
# -----------------------------------------
algoritmos = {
    "Backtracking": backtracking,
    "Divide y Vencerás": divide_y_venceras,
    "Fuerza Bruta": fuerza_bruta,
    "Greedy": greedy,
    "Recursivo": fuerza_bruta_recursiva
}

# -----------------------------------------
# Comparativa
# -----------------------------------------
print("\n--- COMPARATIVA DE TIEMPOS ---\n")

for nombre, funcion in algoritmos.items():
    tiempo = medir_tiempo(funcion, datos, num_servidores)

    if tiempo is not None:
        print(f"{nombre}: {tiempo:.10f} segundos")