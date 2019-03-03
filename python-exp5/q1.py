class Employee:
    empCount = 0

    def __init__(self, id):
        self.id = id

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

    def getId(self):
        return self.id

    @classmethod
    def setEmpCount(cls):
        cls.empCount += 1

    @classmethod
    def getEmpCount(cls):
        return cls.empCount


myEmployeeList = []

num = int(input('\nEnter the number of Employees : '))

for i in range(0, num):
    print('Enter the details of  Employee {} :\n----------------------------------------------'.format(i+1))
    myEmployeeList.append(Employee(int(input('Enter the Id of Employee : '))))
    myEmployeeList[i].setName(input('Enter the name of Employee : '))
    Employee.setEmpCount()

print('Total Number of Employees => {}'.format(Employee.getEmpCount()))

print("EmpId \t\t EmpName")
for i in range(0, num):
    print(myEmployeeList[i].getId(), " \t\t ", myEmployeeList[i].getName())
