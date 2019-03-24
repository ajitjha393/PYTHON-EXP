import os
import time
# Create Directory using mkdir() and makedirs()

os.mkdir('./newDir')  # Create new directory in your working folder
os.makedirs('./makeDirDirectory/newDir')  # creates multiple directory

# remove directory

time.sleep(2)  # This is for delaying the deletion so that we can observe

os.rmdir('./newDir')
os.removedirs('./makeDirDirectory/newDir')

# current directory

print(os.getcwd())

os.chdir('./python-Exp-5/')

print(os.getcwd())
