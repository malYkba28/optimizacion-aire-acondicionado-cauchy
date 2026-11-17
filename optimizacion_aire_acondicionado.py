import numpy as np
import pandas as pd

# 1. Datos del problema
horas = ["12:00", "13:00", "14:00", "15:00", "16:00", "17:00", "18:00", "19:00"]
temp_ext = np.array([29, 31, 33, 34, 35, 34, 32, 30], dtype=float)
estudiantes = np.array([10, 18, 25, 30, 32, 28, 20, 12], dtype=float)
costo = np.array([1.1, 1.1, 1.2, 1.3, 1.4, 1.4, 1.2, 1.1])

T_CONFORT = 24.0
T_MIN, T_MAX = 22.0, 27.0

# Estrategia inicial: 24 °C todas las horas
x = np.ones(8) * T_CONFORT
x_inicial = x.copy()

# Parametros del metodo de Cauchy (maximo descenso)
alpha = 0.5
tolerancia = 0.001
max_iteraciones = 100
lambda_confort = 0.03

# 2. Funciones
def energia(x):
    # Consumo: crece cuanto mas se enfria respecto a la temperatura exterior
    return np.sum(costo * (temp_ext - x))

def funcion_objetivo(x):
    # Energia + penalizacion de confort ponderada por ocupacion
    penalizacion = lambda_confort * np.sum(estudiantes * (x - T_CONFORT) ** 2)
    return energia(x) + penalizacion

# 3. Metodo de Cauchy
for iteracion in range(1, max_iteraciones + 1):
    gradiente = -costo + 2 * lambda_confort * estudiantes * (x - T_CONFORT)
    if np.linalg.norm(gradiente) < tolerancia:
        break

    x = x - alpha * gradiente

    # Restriccion: entre 22 y 27 °C
    x = np.clip(x, T_MIN, T_MAX)

# 4. Resultados
resultados = pd.DataFrame({
    "Hora": horas,
    "Temperatura exterior": temp_ext,
    "Estudiantes": estudiantes,
    "Costo energia": costo,
    "Temperatura inicial": x_inicial,
    "Temperatura optimizada": np.round(x, 2),
    "Cambio": np.round(x - x_inicial, 2),
})

energia_inicial = energia(x_inicial)
energia_optima = energia(x)
ahorro = energia_inicial - energia_optima
porcentaje_ahorro = ahorro / energia_inicial * 100

print(resultados.to_string(index=False))
print("Iteraciones:", iteracion)
print("Energia inicial:", round(energia_inicial, 2))
print("Energia optimizada:", round(energia_optima, 2))
print("Ahorro:", round(ahorro, 2))
print("Porcentaje de ahorro:", round(porcentaje_ahorro, 2), "%")
print("Funcion objetivo inicial:", round(funcion_objetivo(x_inicial), 4))
print("Funcion objetivo final:", round(funcion_objetivo(x), 4))