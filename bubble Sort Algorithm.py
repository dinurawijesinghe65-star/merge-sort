# Bubble Sort Algorithm

def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        for j in range(0, n - i - 1):

            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


numbers = [13, 21, 19, 11]

bubble_sort(numbers)

print("Sorted array:", numbers)