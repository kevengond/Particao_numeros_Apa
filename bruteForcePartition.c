#include <stdio.h>

// Função auxiliar para imprimir uma partição
void printPartition(int partition[], int n, int k) {
    for (int i = 0; i < k; i++) {
        printf("Subset %d: ", i + 1);
        for (int j = 0; j < n; j++) {
            if (partition[j] == i)
                printf("%d ", j + 1);
        }
        printf("\n");
    }
}

// Função auxiliar para verificar se todos os subconjuntos têm a mesma soma
int checkEqualSums(int arr[], int partition[], int n, int k) {
    int subsetSum[k];
    
    // Inicializar a soma de cada subconjunto como 0
    for (int i = 0; i < k; i++)
        subsetSum[i] = 0;

    // Calcular a soma de cada subconjunto
    for (int i = 0; i < n; i++)
        subsetSum[partition[i]] += arr[i];

    // Verificar se todas as somas são iguais
    for (int i = 1; i < k; i++) {
        if (subsetSum[i] != subsetSum[0])
            return 0; // Soma não é igual
    }

    return 1; // Todas as somas são iguais
}

// Função principal para encontrar todas as partições com a mesma soma
void kPartitionEqualSums(int arr[], int n, int k, int partition[], int index) {
    // Se todas as partições foram formadas
    if (index == n) {
        if (checkEqualSums(arr, partition, n, k))
            printPartition(partition, n, k);
        return;
    }

    // Tentar adicionar o elemento atual a todas as partições possíveis
    for (int i = 0; i < k; i++) {
        partition[index] = i;
        kPartitionEqualSums(arr, n, k, partition, index + 1);
    }
}

int main() {
    int n, k;

    printf("Digite o número de elementos (n): ");
    scanf("%d", &n);

    int arr[n];

    printf("Digite os elementos:\n");
    for (int i = 0; i < n; i++) {
        scanf("%d", &arr[i]);
    }

    printf("Digite o número de partições (k): ");
    scanf("%d", &k);

    if (n < k) {
        printf("Não é possível dividir em %d partições.\n", k);
    } else {
        int partition[n];
        kPartitionEqualSums(arr, n, k, partition, 0);
    }

    return 0;
}
