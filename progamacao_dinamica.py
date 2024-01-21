def minDiferenca(arr, n, somaTotal):
    # Inicializa a tabela dp
    dp = [[0 for i in range(somaTotal + 1)] for j in range(n + 1)]

    # Preenche a tabela dp de maneira ascendente
    for i in range(n + 1):
        dp[i][0] = True

    for j in range(1, somaTotal + 1):
        dp[0][j] = False

    for i in range(1, n + 1):
        for j in range(1, somaTotal + 1):
            dp[i][j] = dp[i - 1][j]

            if arr[i - 1] <= j:
                dp[i][j] |= dp[i - 1][j - arr[i - 1]]

    # Inicializa a diferença da soma das duas partes
    diff = float('inf')

    # Encontra a maior j tal que dp[n][j] é True
    # onde j varia de somaTotal/2 até 0
    for j in range(somaTotal // 2, -1, -1):
        if dp[n][j] == True:
            diff = somaTotal - 2 * j
            break

    return diff

# Testando o código
arr = [3, 1, 4, 2, 2, 1, 5, 2]
n = len(arr)

somaTotal = 0
for i in range(0, n):
    somaTotal += arr[i]

print("A menor diferença é", minDiferenca(arr, n, somaTotal))

