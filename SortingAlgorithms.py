#Implement the bubble sort algorithm
def bubbleSort(arr):
    swap = True
    for i in range(len(arr) - 1):
        for j in range(0, len(arr)-i-1):
            if(arr[j] > arr[j+1]):
                swap = True
                arr[j],arr[j+1] = arr[j+1], arr[j]
        if not swap:
            return arr
    return arr

#Implement the merge sort algorithm
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    # Split the array into two halves
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    # Recursive call to sort each half
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    # Merge the sorted halves
    return merge(left_half, right_half)

def merge(left, right):
    result = []
    left_index = right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1

    # Append the remaining elements from both lists (if any)
    result.extend(left[left_index:])
    result.extend(right[right_index:])

    return result


def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)

if __name__ == "__main__":
    # Test Bubble Sort
    print("Testing Bubble Sort:")
    arr_bubble = [64, 34, 25, 12, 22, 11, 90]
    sorted_arr_bubble = bubbleSort(arr_bubble.copy())
    print(f"Original Array: {arr_bubble}")
    print(f"Sorted Array: {sorted_arr_bubble}")
    print()

    # Test Merge Sort
    print("Testing Merge Sort:")
    arr_merge = [38, 27, 43, 3, 9, 82, 10]
    sorted_arr_merge = merge_sort(arr_merge.copy())
    print(f"Original Array: {arr_merge}")
    print(f"Sorted Array: {sorted_arr_merge}")
    print()

    # Test Quick Sort
    print("Testing Quick Sort:")
    arr_quick = [38, 27, 43, 3, 9, 82, 10]
    sorted_arr_quick = quick_sort(arr_quick.copy())
    print(f"Original Array: {arr_quick}")
    print(f"Sorted Array: {sorted_arr_quick}")
