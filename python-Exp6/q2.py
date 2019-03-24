# Create a file named foo.txt
# Since our job is to read from a file then we have to first write into it
from functools import reduce

myFile = open('foo.txt', 'w')
myText = ''

# This small maneuver i have done for taking multi line input
for i in range(int(input('Enter the number of lines to be written into the file : '))):
    myText += input() + '\n'

myFile.write(myText)


myFile.close()

myFile = open('foo.txt', 'r')

myContent = myFile.read()

print(myContent.split('\n'))

numOfLines = len(myContent.split('\n')) - 1
numOfWords = len(' '.join(myContent.split('\n')).split(' ')) - 1
numOfChar = reduce(
    lambda x, y: x+y, list(map(lambda x: len(x), myContent.split('\n'))))

print('No of lines = > {} \n No of  Words = {} \n No of Char = {}'.format(
    numOfLines, numOfWords, numOfChar))

myFile.close()
# Creating a new file and copy the content of old file to it
myNewFile = open('foo2.txt', 'w')


myNewFile.write(myContent)

myNewFile.close()

myNewFile = open('foo2.txt', 'r')
print('Content of new File => \n', myNewFile.read())
