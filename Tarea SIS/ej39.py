import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# Define la ecuación diferencial para el crecimiento del tumor
def tumor_growth(A, t, alpha, k, nu):
    return alpha * A * (1 - (A / k)**nu)

# Parámetros
alpha = 0.8
k = 60
nu = 0.25
A0 = 1  # Área inicial en mm^2

# Puntos de tiempo
t_tumor = np.linspace(0, 30, 301)  # 0 a 30 días, 301 puntos para un gráfico suave

# Resuelve la ecuación diferencial
solution_tumor = odeint(tumor_growth, A0, t_tumor, args=(alpha, k, nu))
A_t = solution_tumor[:, 0]

# Imprime los resultados en la consola para el Crecimiento del Tumor
print("--- Resultados para el Crecimiento del Tumor (Ejercicio 39) ---")
print("Tiempo (días) | Área del Tumor (mm^2)")
print("---------------------------------")
# Imprime cada 30º punto para brevedad
for i in range(0, len(t_tumor), 30):
    print(f"{t_tumor[i]:<11.2f} | {A_t[i]:<15.4f}")
print("...") # Indica que no todos los puntos se imprimen

# Grafica los resultados para el Crecimiento del Tumor
plt.figure(figsize=(10, 6))
plt.plot(t_tumor, A_t, label='Área del Tumor $A(t)$')
plt.title('Crecimiento del Tumor a lo Largo del Tiempo')
plt.xlabel('Tiempo (días)')
plt.ylabel('Área del Tumor ($mm^2$)')
plt.grid(True)
plt.legend()
plt.show()