import sympy as sp

# Definir la variable simbólica
x = sp.symbols('x')

# Definir una función simbólica
f = x**2 + 3*x + 2

# Calcular la derivada de la función con respecto a x
f_prime = sp.diff(f, x)

# Mostrar la derivada
print(f_prime)