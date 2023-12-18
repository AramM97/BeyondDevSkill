#Implement the linear search algorithm
def linearSearch(arr, find):
    for i in arr:
        if(i == find):
            return arr.index(i)
    return -1


def binarySearch(arr, find):
    low = 0
    high = len(arr) - 1
    mid = 0

    while low <= high:
        mid = (high + low) // 2
        # find is greater,check on right side
        if arr[mid] < find:
            low = mid + 1
        # find is smaller,check on left side
        elif arr[mid] > find:
            high = mid - 1
        else:
            return mid

    return -1

if __name__ == "__main__":
    searchArr = [1, 2, 3, 4, 5, 6, 7, 8]
    print(linearSearch(searchArr, 7))
    print(binarySearch(searchArr, 7))