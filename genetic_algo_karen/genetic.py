import random

def generate_population(size, gene_pool, gene_length):
    return [
        [random.choice(gene_pool) for _ in range(gene_length)]
        for _ in range(size)
    ]

def fitness(individual, target):
    return sum(1 for i, gene in enumerate(individual) if gene == target[i])

def selection(population, target):
    return sorted(population, key=lambda x: fitness(x, target), reverse=True)

def crossover(parent1, parent2):
    pivot = random.randint(1, len(parent1) - 1)
    return parent1[:pivot] + parent2[pivot:]

def mutate(individual, gene_pool, mutation_rate=0.01):
    return [
        gene if random.random() > mutation_rate else random.choice(gene_pool)
        for gene in individual
    ]

def genetic_algorithm(target, gene_pool, population_size=100, generations=1000):
    gene_length = len(target)
    population = generate_population(population_size, gene_pool, gene_length)

    for generation in range(generations):
        population = selection(population, target)
        if fitness(population[0], target) == gene_length:
            return population[0], generation

        next_generation = population[:2]  # elitismo

        while len(next_generation) < population_size:
            parent1, parent2 = random.sample(population[:10], 2)
            child = crossover(parent1, parent2)
            child = mutate(child, gene_pool)
            next_generation.append(child)

        population = next_generation

    return population[0], generations