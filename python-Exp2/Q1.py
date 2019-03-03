import numpy as np


def readArray():
    myArray = np.array([], dtype='int32')
    num = int(input("Enter the number of elements of the array"))
    for i in range(0, num):
        myArray = np.append(myArray, int(input(f"Enter the Array{i} = ")))
    return myArray


def displayArray(myArray):
    print(f"Elements are => {myArray}")


def addItem(myArray):
    return np.append(myArray, int(input("Enter the number to be appended : ")))


def reverseOrder(myArray):
    return myArray[-1::-1]


def getItemSize(myArray):
    return myArray.itemsize


def appendFromAnotherArray(array1, array2):
    return np.append(array1, array2)


def removeElementAtIndex(myArray, index):
    return np.append(myArray[:index], myArray[index+1:])


myArray = readArray()
displayArray(myArray)
myArray = addItem(myArray)
print(f"After appending => {myArray}")
print(f"Reverse of the Array => {reverseOrder(myArray)}")
print(f"Item-Size = {getItemSize(myArray)}")
print("Enter the array to be appended")
myNewArray = readArray()
print(f"Appended array => {appendFromAnotherArray(myArray,myNewArray)}")
index = int(input("Enter the index"))
print(f"After Deletion  New Array => {removeElementAtIndex(myArray,index)}")
