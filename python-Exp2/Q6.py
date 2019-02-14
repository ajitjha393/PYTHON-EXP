# A------------->

myListOfStrings = []
num = int(input("Enter the number of strings"))
for i in range(0, num):
    myListOfStrings.append(input("Enter a string : "))

print("Entered List => ", myListOfStrings)
myListOfStrings.sort()
print("Sorted List => ", myListOfStrings)


# Q6 ------------->
# B-------->


myString = input("Enter a String : ")
if myString == myString[::-1]:
    print("The Entered String is a Palindrome")
else:
    print("The Entered String is not a Palindrome")
