from itertools import product

def partition_k(X, k):
    n = len(X)
    
    # Gera todas as combinações possíveis dos índices dos elementos
    index_combinations = product(range(k), repeat=n)
    
    unique_partitions = set()
    
    # Verifica se cada combinação atende aos critérios
    for indices in index_combinations:
        subsets = [[] for _ in range(k)]
        
        # Preenche os subsets com os elementos correspondentes
        for i, index in enumerate(indices):
            subsets[index].append(X[i])
        
        # Usa tuplas para representar cada subset
        tuple_subsets = [tuple(subset) for subset in subsets]
        
        # Verifica se as somas são iguais e se não há elementos compartilhados entre os subsets
        sums = [sum(subset) for subset in tuple_subsets]
        if len(set(sums)) == 1 and len(set().union(*tuple_subsets)) == n:
            unique_partitions.add(tuple(tuple_subsets))

    # Imprime as partições únicas
    for i, partition in enumerate(unique_partitions):
        # Ordena os elementos dentro de cada subset
        formatted_partition = [', '.join(map(str, sorted(subset))) for subset in partition]
        output = f"{i}: ({'), ('.join(formatted_partition)})"
        print(output)

# Exemplo de uso
X = [2, 5, 4, 9, 1, 7, 6, 8]
k = 3
partition_k(X, k)
