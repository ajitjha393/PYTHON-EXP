class Customer:
    def __init__(self, id, name, mobileNo):
        self.id = id
        self.name = name
        self.mobileNo = mobileNo


myCustomerList = []

num = int(input('Enter the number of Customer : '))
for i in range(num):
    id, name, mobileNo = input(
        'Enter ID,Name,Mobile no of Customer {} : '.format(i+1)).split(',')
    print('----------------------------------------')
    myCustomerList.append(Customer(id, name, mobileNo))

myCustomerFile = open('myCustomerFile.txt', 'a')
myCustomerFile.write('ID,Name,Mobile No. \n')
for i in range(num):
    myCustomerFile.write('{},{},{}\n'.format(
        myCustomerList[i].id, myCustomerList[i].name, myCustomerList[i].mobileNo))

myCustomerFile.close()
# READING FROM THE FILE TO DISPLAY
myCustomerFile = open('myCustomerFile.txt', 'r')
print('Id  Name  Mob \n-------------------------')
customerDetails = myCustomerFile.read().split('\n')
for i in range(1, len(customerDetails) - 1):
    id, name, mob = customerDetails[i].split(',')
    print('{}  {}  {} '.format(id, name, mob))
