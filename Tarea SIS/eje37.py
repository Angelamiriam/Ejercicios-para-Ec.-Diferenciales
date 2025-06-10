import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# Define la ecuación diferencial para el crecimiento poblacional
def population_growth(N, t, k, Nm):
    return k * N * (Nm - N)

# Parámetros
k = 0.000095  # constante en 1/yr
Nm = 5000     # Número límite para la población
N0 = 100      # Tamaño inicial de la población

# Puntos de tiempo
t_population = np.linspace(0, 20, 201)  # 0 a 20 años, 201 puntos para un gráfico suave

# Resuelve la ecuación diferencial
solution_population = odeint(population_growth, N0, t_population, args=(k, Nm))
N_t = solution_population[:, 0]

# Imprime los resultados en la consola para el Crecimiento Poblacional
print("--- Resultados para el Crecimiento Poblacional (Ejercicio 37) ---")
print("Tiempo (años) | Tamaño de la Población")
print("------------------------------")
# Imprime cada 20º punto para brevedad
for i in range(0, len(t_population), 20):
    print(f"{t_population[i]:<12.2f} | {N_t[i]:<15.2f}")
print("...") # Indica que no todos los puntos se imprimen

# Grafica los resultados para el Crecimiento Poblacional
plt.figure(figsize=(10, 6))
plt.plot(t_population, N_t, label='Tamaño de la Población $N(t)$')
plt.title('Crecimiento Poblacional a lo Largo del Tiempo')
plt.xlabel('Tiempo (años)')
plt.ylabel('Tamaño de la Población')
plt.grid(True)
plt.legend()
plt.show()