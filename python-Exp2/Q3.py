
import numpy as np

myCase = '0'
myArray = np.array([], dtype='int64')

while(myCase != '5'):
    print('''*************MENU DRIVEN*************
        1. Create array
        2. Sum of Array
        3. Sort Array
        4. Compare two arrays
        5. Exit
        ''')

    myCase = input("\nEnter a choice : ")

    if myCase == '1':

        print('''*************MENU DRIVEN*************
            1. Using array()
            2. Using arange()
        ''')
        mySubCase = input("\nEnter a choice : ")

        if mySubCase == '1':
            n = int(input("Enter the number of elements of array : "))
            for i in range(0, n):
                myArray = np.append(
                    myArray, [int(input(f"Enter array[{i}] = "))])

        else:
            start, end, step = input(
                "Enter the starting point ,ending point and steps for the arange() : ").split(",")
            start = int(start)
            end = int(end)
            step = int(step)
            myArray = np.arange(start, end, step)
        print(f"Array is => {myArray}")

    elif myCase == '2':
        if len(myArray) == 0:
            print("Please Create an Array")
        else:
            print(f"Sum of array = {sum(myArray)}")

    elif myCase == '3':
        if len(myArray) == 0:
            print("Please Create an Array")
        else:
            print(f"Sorted array => {np.sort(myArray)}")

    elif myCase == '4':
        # print(np.array(
        #     input("Enter another array to compare : ").split(",")))

        myNewArray = np.array(
            list(map(int, input("Enter another array to compare : ").split(","))))

        print(myNewArray)

        if np.array_equal(myArray, myNewArray):
            print("Both Arrays are Equal")
        else:
            print("Both Arrays are Not Equal")
