#include <stdio.h>

void implementFirstFit(int blockSize[], int blocks, int processSize[], int processes) {
    // This will store the block id of the allocated block to a process
    int allocate[processes];

    // Initially assigning -1 to all allocation indexes (nothing is allocated)
    for (int i = 0; i < processes; i++) {
        allocate[i] = -1;
    }

    // Take each process one by one and find the first block that can accommodate it
    for (int i = 0; i < processes; i++) {
        for (int j = 0; j < blocks; j++) {
            if (blockSize[j] >= processSize[i]) {
                // Allocate block j to process i
                allocate[i] = j;

                // Reduce size of block j as it has accommodated process i
                blockSize[j] -= processSize[i];
                break;
            }
        }
    }

    // Output the allocation result
    printf("\nProcess No.\tProcess Size\tBlock No.\n");
    for (int i = 0; i < processes; i++) {
        printf("%d\t\t%d\t\t", i + 1, processSize[i]);
        if (allocate[i] != -1)
            printf("%d\n", allocate[i] + 1);
        else
            printf("Not Allocated\n");
    }
}

int main() {
    int blockSize[] = {100, 500, 200, 300, 600};
    int processSize[] = {212, 417, 112, 426};
    int m = sizeof(blockSize) / sizeof(blockSize[0]);
    int n = sizeof(processSize) / sizeof(processSize[0]);

    implementFirstFit(blockSize, m, processSize, n);
    return 0;
}
