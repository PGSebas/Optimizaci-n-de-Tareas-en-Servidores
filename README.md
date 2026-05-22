# Optimización de Tareas en Servidores

## Descripción General

Este proyecto desarrolla e implementa diferentes paradigmas algorítmicos para resolver un problema de planificación y distribución de tareas en servidores.

El objetivo principal consiste en asignar tareas a múltiples servidores de manera eficiente, minimizando el tiempo total de ejecución y respetando restricciones importantes del sistema como:

- prioridades de ejecución,
- dependencias entre tareas,
- y balance de carga entre servidores.

Cada tarea posee:
- un identificador,
- un tiempo de ejecución,
- un nivel de prioridad,
- y posibles dependencias con otras tareas.

---

# Objetivo del Proyecto

El proyecto busca comparar distintas técnicas algorítmicas aplicadas al mismo problema para analizar:

- eficiencia,
- complejidad computacional,
- calidad de solución,
- escalabilidad,
- y facilidad de implementación.

Se estudia cómo cada paradigma enfrenta el crecimiento del problema y cuáles son sus ventajas y limitaciones en escenarios reales.

---

# Paradigmas Algorítmicos Implementados

## 1. Fuerza Bruta

Explora todas las posibles asignaciones de tareas a servidores para garantizar encontrar la solución óptima.

Características:
- garantiza la mejor solución,
- alto costo computacional,
- crecimiento exponencial.

---

## 2. Recursividad

Resuelve el problema mediante llamadas recursivas y construcción de un árbol de decisiones.

Características:
- representación natural del problema,
- facilita exploración de soluciones,
- base para técnicas más avanzadas.

---

## 3. Greedy (Voraz)

Toma decisiones locales óptimas en cada paso:
- selecciona tareas de mayor prioridad,
- y las asigna al servidor menos cargado.

Características:
- ejecución rápida,
- bajo costo computacional,
- no siempre garantiza optimalidad.

---

## 4. Backtracking

Mejora la recursividad utilizando poda de ramas innecesarias para evitar explorar soluciones claramente inválidas o peores.

Características:
- mantiene soluciones óptimas,
- reduce el espacio de búsqueda,
- mejora considerablemente el rendimiento práctico.

---

## 5. Divide y Vencerás

Divide el conjunto de tareas en subproblemas más pequeños, resuelve cada uno recursivamente y combina las soluciones parciales.

Características:
- mejor rendimiento en entradas grandes,
- complejidad más eficiente,
- solución aproximada.

---

# Restricciones del Problema

El sistema debe cumplir obligatoriamente las siguientes condiciones:

## Dependencias

Una tarea no puede ejecutarse hasta que todas sus dependencias hayan sido completadas.

Ejemplo:

```text
T5 depende de T2 y T3