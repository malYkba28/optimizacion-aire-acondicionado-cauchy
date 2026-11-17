# Optimización del consumo de aire acondicionado con el método de Cauchy

Proyecto final de la materia de **Sistemas de Optimización Inteligente**.

## Problema

Un aula usa aire acondicionado durante una jornada de 8 horas (12:00 a 19:00). Mantenerlo siempre a 24 °C gasta más energía de la necesaria, pero subir demasiado la temperatura afecta el confort de los estudiantes. La ocupación, la temperatura exterior y el costo de la energía cambian cada hora.

**Objetivo:** encontrar la temperatura de operación para cada hora que reduzca el consumo sin alejarse demasiado del confort.

## Modelo

- **Variables:** temperatura programada para cada una de las 8 horas.
- **Función objetivo:** energía consumida + penalización por alejarse de 24 °C, ponderada por el número de estudiantes en el aula.
- **Restricción:** la temperatura debe estar entre 22 °C y 27 °C.
- **Método:** descenso más pronunciado (Cauchy), con paso fijo α = 0.5 y proyección a los límites en cada iteración.

**Tecnologías:** Python, NumPy y pandas.

## Resultados

| Hora | T. exterior (°C) | Estudiantes | T. optimizada (°C) |
|---|---|---|---|
| 12:00 | 29 | 10 | 25.83 |
| 13:00 | 31 | 18 | 25.02 |
| 14:00 | 33 | 25 | 24.80 |
| 15:00 | 34 | 30 | 24.72 |
| 16:00 | 35 | 32 | 24.73 |
| 17:00 | 34 | 28 | 24.83 |
| 18:00 | 32 | 20 | 25.00 |
| 19:00 | 30 | 12 | 25.53 |

- Convergencia en **21 iteraciones**.
- Consumo de energía: de 82.6 a 72.5 unidades relativas, un **ahorro de 12.23 %** frente a dejarlo fijo en 24 °C.
- En las horas con más estudiantes la temperatura se mantiene más cerca de 24 °C; en las horas con pocos estudiantes se sube más para ahorrar.

## Cómo ejecutarlo

```bash
pip install numpy pandas
python optimizacion_aire_acondicionado.py
```
