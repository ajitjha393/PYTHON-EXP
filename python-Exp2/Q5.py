
myString = input("Enter a string : ")
charToReplace = myString[0]
replacedString = charToReplace + myString.replace(charToReplace, '@')[1:]
print(replacedString)
