import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# Define la ecuación diferencial para la velocidad de un objeto que cae
def falling_object_velocity(v, t, m, g, k):
    return -g + (k / m) * (v**2)

# Parámetros
m = 5      # masa en kg
g = 9.81   # aceleración debido a la gravedad en m/s^2
k = 0.05   # constante en kg/m
v0 = 0     # Velocidad inicial en m/s

# Puntos de tiempo
t_velocity = np.linspace(0, 15, 301)  # 0 a 15 segundos, 301 puntos

# Resuelve la ecuación diferencial
solution_velocity = odeint(falling_object_velocity, v0, t_velocity, args=(m, g, k))
v_t = solution_velocity[:, 0]

# Imprime los resultados en la consola para la Velocidad del Objeto que Cae
print("--- Resultados para la Velocidad de un Objeto que Cae (Ejercicio 40) ---")
print("Tiempo (s) | Velocidad (m/s)")
print("-------------------------")
# Imprime cada 30º punto para brevedad
for i in range(0, len(t_velocity), 30):
    print(f"{t_velocity[i]:<9.2f} | {v_t[i]:<14.4f}")
print("...") # Indica que no todos los puntos se imprimen

# Grafica los resultados para la Velocidad del Objeto que Cae
plt.figure(figsize=(10, 6))
plt.plot(t_velocity, v_t, label='Velocidad $v(t)$')
plt.title('Velocidad de un Objeto que Cae a lo Largo del Tiempo')
plt.xlabel('Tiempo (s)')
plt.ylabel('Velocidad (m/s)')
plt.grid(True)
plt.legend()
plt.show()