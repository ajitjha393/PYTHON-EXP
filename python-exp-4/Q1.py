from math import floor, ceil


def separateEvenOddList(myList):
    evenList = list(filter(lambda x: x % 2 == 0, myList))
    oddList = list(filter(lambda x: x % 2 != 0, myList))
    return evenList, oddList


def mergeAndSort(myList1, myList2):
    return sorted(myList1 + myList2)


def updateFirstElement(myList, newElement):
    myList[0] = newElement
    return myList


def middleElement(myList):
    if len(myList) % 2 != 0:
        return myList[floor((len(myList) - 1)/2)]
    else:
        return myList[floor((len(myList) - 1)/2)], myList[ceil((len(myList) - 1)/2)]


def main():
    myChoice = 'True'
    while(myChoice != '5'):
        print('''
        1. Put even and odd elements in two different list
        2. Merge and Sort two lists
        3. Update the first Element with a value X
        4. Print middle element of the list
        5. Exit
        ''')
        myChoice = input("Enter a choice : ")
        if myChoice == '1':
            evenList, oddList = separateEvenOddList(
                list(map(int, input("Enter a List of numbers : ").split(','))))
            print(f"Even List => {evenList}\nOdd List => {oddList}")

        elif myChoice == '2':
            print(
                f'''Sorted Array After Merging => {
                        mergeAndSort(list(map(int, input("Enter a List of numbers : ").split(','))),
                        list(map(int, input("Enter a List of numbers : ").split(','))))}''')
        elif myChoice == '3':
            print(
                f'''After Updating the list => {updateFirstElement(list(map(int, input("Enter a List of numbers : ").split(","))),
                 int(input("Enter the new value at first Index")))}'''
            )
        elif myChoice == '4':
            print(
                f'''Middle Element of List  => {middleElement(list(map(int, input("Enter a List of numbers : ").split(","))))}'''
            )


main()
