# Merge Sort Algorithm

def merge_sort(arr):



    if len(arr) <= 1:
        return arr

    
    mid = len(arr) // 2

    
    left_half = arr[:mid]
    right_half = arr[mid:]

    
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    
    return merge(left_half, right_half)


def merge(left, right):

    sorted_array = []
    i = 0
    j = 0

    
    while i < len(left) and j < len(right):

        if left[i] <= right[j]:
            sorted_array.append(left[i])
            i += 1
        else:
            sorted_array.append(right[j])
            j += 1

    
    sorted_array.extend(left[i:])

    
    sorted_array.extend(right[j:])

    return sorted_array


numbers = [12, 7, 4, 25, 47, 23, 8]

sorted_numbers = merge_sort(numbers)

print("Original array:", numbers)
print("Sorted array:", sorted_numbers)