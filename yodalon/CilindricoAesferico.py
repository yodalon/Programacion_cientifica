import math

# Valores de las coordenadas cilíndricas
x = 25.0
y = 30.0  
z = 3.0

# Calcula las coordenadas esféricas
r_esferico = math.sqrt(x**2 + y**2 + z**2)
rc= math.sqrt(x**2 + y**2)
theta = math.atan2(rc,z)
theta_final = math.degrees(theta)
# Imprime las coordenadas esféricas
print(f"Coordenadas Esféricas:")
print(f"r_e = {r_esferico}")
print(f"θ = {theta_final}")
print(f"φ = {y}")
