#include <stdio.h>

int main() {
    int i, j, n, a[50], frame[10], no, k, avail, count = 0;

    printf("ENTER THE NUMBER OF PAGES:\n");
    scanf("%d", &n);

    printf("ENTER THE PAGE NUMBERS:\n");
    for (i = 0; i < n; i++) {
        scanf("%d", &a[i]);
    }

    printf("ENTER THE NUMBER OF FRAMES:\n");
    scanf("%d", &no);

    for (i = 0; i < no; i++) {
        frame[i] = -1;
    }

    j = 0;

    printf("\nRef string\tPage frames\n");
    for (i = 0; i < n; i++) {
        printf("%d\t\t", a[i]);
        avail = 0;

        // Check if page is already in a frame
        for (k = 0; k < no; k++) {
            if (frame[k] == a[i]) {
                avail = 1;
                break;
            }
        }

        // If not available, replace using FIFO
        if (avail == 0) {
            frame[j] = a[i];
            j = (j + 1) % no;
            count++;
        }

        for (k = 0; k < no; k++) {
            if (frame[k] != -1)
                printf("%d\t", frame[k]);
            else
                printf("-\t");
        }
        printf("\n");
    }

    printf("\nTotal Page Faults = %d\n", count);

    return 0;
}
