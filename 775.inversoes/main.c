#include <stdio.h>
#include <stdlib.h>

int merge(int arr[], int temp[], int left, int mid, int right) {
    int i, j, k;
    int inversions = 0;

    i = left;
    j = mid;
    k = left;

    while ((i <= mid - 1) && (j <= right)) {
        if (arr[i] <= arr[j]) {
            temp[k++] = arr[i++];
        } else {
            temp[k++] = arr[j++];
            inversions += (mid - i);
        }
    }

    while (i <= mid - 1) {
        temp[k++] = arr[i++];
    }

    while (j <= right) {
        temp[k++] = arr[j++];
    }

    for (i = left; i <= right; i++) {
        arr[i] = temp[i];
    }

    return inversions;
}

int mergeSort(int arr[], int temp[], int left, int right) {
    long int mid, inversions = 0;

    if (right > left) {
        mid = (right + left) / 2;

        inversions += mergeSort(arr, temp, left, mid);
        inversions += mergeSort(arr, temp, mid + 1, right);

        inversions += merge(arr, temp, left, mid + 1, right);
    }

    return inversions;
}

int countInversions(int arr[], int n) {
    int *temp = (int *)malloc(sizeof(int) * n);
    int inversions = mergeSort(arr, temp, 0, n - 1);
    free(temp);
    return inversions;
}

int isIdealPermutation(int *nums, int numsSize) {
    int localInversions = 0;

    for (int i = 0; i < numsSize - 1; i++) {
        if (nums[i] > nums[i + 1]) {
            localInversions++;
        }
    }
    int globalInversions = countInversions(nums, numsSize);

    return globalInversions == localInversions;
}

int main() {
    int nums1[] = {1, 0, 2};
    int nums2[] = {1, 2, 0};

    printf("Exemplo 1: %s\n", isIdealPermutation(nums1, 3) ? "true" : "false");
    printf("Exemplo 2: %s\n", isIdealPermutation(nums2, 3) ? "true" : "false");

    return 0;
}
