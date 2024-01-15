def heuristic_number_partitioning(V):
    # Inicializa dois subconjuntos vazios
    V1 = []
    V2 = []

    # Ordena os números em ordem decrescente
    sorted_V = sorted(V, reverse=True)

    # Adiciona os números de forma alternada aos subconjuntos
    for i, num in enumerate(sorted_V):
        if i % 2 == 0:
            V1.append(num)  # Adiciona ao V1 se o índice for par
        else:
            V2.append(num)  # Adiciona ao V2 se o índice for ímpar

    return (V1, V2)

# Cria um conjunto de números de 1 a 100
V = [i for i in range(1, 101)]

# Chama a função heurística de partição
(V1, V2) = heuristic_number_partitioning(V)

# Calcula a diferença entre os tamanhos dos subconjuntos
difference = len(V1) - len(V2)

# Imprime os subconjuntos e a diferença absoluta entre seus tamanhos
print(V1, end="\n\n\n")
print(V2, end="\n\n\n")
print("|V1|-|V2| = {}".format(abs(difference)))