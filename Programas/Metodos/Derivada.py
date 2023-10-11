import sympy as sp

# Definir la variable simbólica
x = sp.symbols('x')

# Definir una función simbólica
f = x**2 + 3*x + 2

# Calcular la derivada de la función con respecto a x
f_prime = sp.diff(f, x)

# Mostrar la derivada
print(f_prime)

# Definir la variable simbólica
x = sp.symbols('x')

# Definir la función seno
f = sp.sin(x)

# Calcular la derivada
f_prime = sp.diff(f, x)

# Imprimir la derivada
print(f_prime)

x = sp.symbols('x')
f = sp.sin(x) + 2*x**3 - 5*x**2 + 2
f_prime = sp.diff(f,x)
print(f_prime)