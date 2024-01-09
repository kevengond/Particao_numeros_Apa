#include <stdio.h>

// Função auxiliar para imprimir a k-partição
void printPartition(int set[], int subsetSum[], int n, int k) {
    for (int i = 0; i < k; i++) {
        printf("Subset %d: ", i + 1);
        for (int j = 0; j < n; j++) {
            if (subsetSum[j] == i + 1) {
                printf("%d ", set[j]);
            }
        }
        printf("\n");
    }
}

// Função auxiliar para verificar se uma partição é válida
int isValidPartition(int set[], int n, int subsetSum[], int k) {
    for (int i = 0; i < n; i++) {
        int count = 0;
        for (int j = 0; j < k; j++) {
            if (subsetSum[j] == set[i]) {
                count++;
            }
        }
        if (count == 0) {
            return 0;
        }
    }
    return 1;
}

// Função principal para encontrar a k-partição usando força bruta
int bruteForcePartition(int set[], int n, int k, int subsetSum[]) {
    if (n == 0) {
        // Verifica se a partição atual é válida e imprime se for
        if (isValidPartition(set, n, subsetSum, k)) {
            printPartition(set, subsetSum, n, k);
            return 1;
        }
        return 0;
    }

    // Tenta adicionar o elemento atual a cada subconjunto e recursivamente verifica
    for (int i = 0; i < k; i++) {
        subsetSum[i] += set[n - 1];
        if (bruteForcePartition(set, n - 1, k, subsetSum)) {
            return 1;
        }
        subsetSum[i] -= set[n - 1];
    }

    return 0;
}

// Função principal
int main() {
    int set[] = {1, 2, 3, 4, 5, 6};
    int n = sizeof(set) / sizeof(set[0]);
    int k = 3; // Número de partições desejadas

    // Verifica se é possível fazer a k-partição usando força bruta
    int subsetSum[n];
    if (bruteForcePartition(set, n, k, subsetSum)) {
        printf("K-partição encontrada.\n");
    } else {
        printf("Não é possível fazer a k-partição.\n");
    }

    return 0;
}
