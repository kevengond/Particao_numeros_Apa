def minDiferenca(arr, l, r, soma1=0, soma2=0):
    # Caso base: se não houver mais elementos para incluir em subconjuntos
    if l > r:
        return abs(soma1 - soma2)

    # Inclui o elemento atual no subconjunto 1 e recursivamente calcula a diferença mínima
    inclui_soma1 = minDiferenca(arr, l + 1, r, soma1 + arr[l], soma2)

    # Inclui o elemento atual no subconjunto 2 e recursivamente calcula a diferença mínima
    inclui_soma2 = minDiferenca(arr, l + 1, r, soma1, soma2 + arr[l])

    # Retorna a diferença mínima
    return min(inclui_soma1, inclui_soma2)

# Testando o código
arr = [3, 1, 4, 2, 2, 1, 5, 2]
n = len(arr)

print("A menor diferença é", minDiferenca(arr, 0, n - 1))