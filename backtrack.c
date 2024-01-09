#include <stdio.h>

#define MAX 100

int result[MAX][MAX];
int subset[MAX];
int total_sum;

void backtrack(int nums[], int k, int start, int target, int path[], int path_index) {
    if (target == 0 && path_index == k) {
        for (int i = 0; i < k; i++) {
            result[path_index - 1][i] = path[i];
        }
        return;
    }

    for (int i = start; i < total_sum; i++) {
        if (nums[i] <= target) {
            path[path_index] = nums[i];
            backtrack(nums, k, i + 1, target - nums[i], path, path_index + 1);
        }
    }
}

void k_partition(int nums[], int n, int k) {
    total_sum = 0;
    for (int i = 0; i < n; i++) {
        total_sum += nums[i];
    }

    if (total_sum % k != 0) {
        printf("Não é possível encontrar uma partição válida.\n");
        return;
    }

    int subset_sum = total_sum / k;
    int path[MAX];
    backtrack(nums, k, 0, subset_sum, path, 0);

    printf("Partição de números em %d subconjuntos:\n", k);
    for (int i = 0; i < k; i++) {
        printf("Subset %d: ", i + 1);
        for (int j = 0; j < n; j++) {
            if (result[i][j] != 0) {
                printf("%d ", result[i][j]);
            }
        }
        printf("\n");
    }
}

int main() {
    int nums[] = {1, 2, 3, 4, 5, 6};
    int n = sizeof(nums) / sizeof(nums[0]);
    int k = 3;

    k_partition(nums, n, k);

    return 0;
}
