from genetic_algo_karen.genetic import genetic_algorithm

# Definir el objetivo y el conjunto de genes posibles
target = "hola"
gene_pool = list("abcdefghijklmnopqrstuvwxyz ")

# Ejecutar el algoritmo genético
best_match = genetic_algorithm(target, gene_pool, population_size=200, generations=1000)

# Imprimir el mejor resultado
print("Mejor coincidencia encontrada:", best_match)
