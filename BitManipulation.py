#Write a program to check if a given number is even or odd using bit manipulation.
#add check if the number is positive
def isEvenBit(num):
    if(num & 1 == 1):
        print('number is Odd')
    else:
        print('number is Even')
    return

#Write a program to find the number of set bits in a given integer using bit manipulation.
#calc number of 1 in the bin represintation
def count_set_bits(num):
    count = 0
    while num:
        num &= (num - 1)
        count += 1
    return count

if __name__ == "__main__":
    isEvenBit(5)
    isEvenBit(4)
    number = 25
    result = count_set_bits(number)
    print(f"The number of set bits in {number} is: {result}")