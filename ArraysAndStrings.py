# Write a program to reverse a string in place
def reverseString(s):
    return (s[::-1])


# Write a program to find the maximum and minimum elements in an array.
def findMinMax(arr):
    return (min(arr), max(arr))


# Write a program to remove duplicates from a sorted array
def removeDup(arr):
    return set(arr)


if __name__ == '__main__':
    s1 = "string"
    arr = [1, 3, 4, 9, 10, 30, 50]
    arr2 = [1, 3, 4, 9, 10, 30, 50, 50, 1, 1]

    print(reverseString(s1))
    print(findMinMax(arr))
    print(removeDup(arr2))
