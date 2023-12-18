#Write a program to calculate the factorial of a number using recursion
def factorial(num):
    if(num < 0):
        print('please choose a positive number')
    elif(num == 1 or num == 0):
        return 1
    else:
        return num * factorial(num-1)

def toString(List):
    return ''.join(List)

def permute(string, start, end):
    if start == end:
        print(toString(string))
    else:
        for i in range(start, end):
            string[start], string[i] = string[i], string[start]
            permute(string, start+1, end)
            string[start], string[i] = string[i], string[start]  # backtrack

if __name__ == "__main__":
    print(factorial(4))
    testArr = 'ABC'
    permute(list(testArr), 0, len(testArr))