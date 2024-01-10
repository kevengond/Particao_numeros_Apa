def is_valid_partition(partitions):
    all_elements = set()
    for subset in partitions:
        for num in subset:
            if num in all_elements:
                return False
            all_elements.add(num)
    return True

def k_partition_backtrack(X, k, target_sum, current_partition, result, index):
    if index == len(X):
        if all(sum(subset) == target_sum for subset in current_partition):
            sorted_partitions = [tuple(sorted(subset)) for subset in current_partition]
            result.add(tuple(sorted(sorted_partitions)))
        return

    for i in range(k):
        current_partition[i].append(X[index])
        k_partition_backtrack(X, k, target_sum, current_partition, result, index + 1)
        current_partition[i].remove(X[index])

def k_partition(X, k):
    total_sum = sum(X)
    if total_sum % k != 0:
        return None  # Não é possível encontrar partições com soma igual

    target_sum = total_sum // k
    result = set()
    current_partition = [[] for _ in range(k)]

    k_partition_backtrack(X, k, target_sum, current_partition, result, 0)

    return list(result) if result else None

# Exemplo de uso
X = [2, 5, 4, 9, 1, 7, 6, 8]
k = 3
partitions = k_partition(X, k)

if partitions:
    for i, subset in enumerate(partitions):
        print(f"Subset {i + 1}: {subset}")
else:
    print(f"Não é possível encontrar {k} partições com soma igual.")
