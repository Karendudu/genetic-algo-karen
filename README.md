# genetic-algo-karen

Una librería simple de algoritmos genéticos en Python creada por Karen Dayana.

## Ejemplo de uso

```python
from genetic_algo_karen.genetic import genetic_algorithm

target = list("KAREN")
gene_pool = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

result, generations = genetic_algorithm(target, gene_pool)
print("Resultado:", "".join(result), "en", generations, "generaciones")
```