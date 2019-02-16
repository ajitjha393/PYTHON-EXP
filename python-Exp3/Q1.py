#-------Perfect Number---------#


def isPerfectNumber(num, findDivisor):
    return sum(findDivisor(num)) == num


def findDivisor(num):
    myDivisorList = []
    for i in range(1, num//2 + 1):
        if num % i == 0:
            myDivisorList.append(i)
    return myDivisorList


num = int(input("Enter a number : "))
if isPerfectNumber(num, findDivisor):
    print(f"{num} is a perfect number :)")
else:
    print(f"{num} is not a perfect number :( ")
