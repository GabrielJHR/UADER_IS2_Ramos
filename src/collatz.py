import matplotlib.pyplot as plt

def collatz_iterations(n):
    count = 0
    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
        count += 1
    return count

# Listas para almacenar los valores
n_values = []
iterations = []

# Calcular el número de iteraciones para cada número entre 1 y 10000
for i in range(1, 10001):
    n_values.append(i)
    iterations.append(collatz_iterations(i))

# Crear el gráfico
plt.figure(figsize=(12, 6))
plt.scatter(iterations, n_values, s=10, color='blue', alpha=0.5)
plt.title('Número de Collatz (Conjetura 2n + 1)')
plt.xlabel('Número de Iteraciones')
plt.ylabel('Número Inicial (n)')
plt.grid(True)
plt.xlim(0, max(iterations) + 10)
plt.ylim(0, 10000)
plt.show()
