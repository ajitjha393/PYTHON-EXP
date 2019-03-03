class Employee:
 
    
    def __init__(self,id):
        self.id = id

    def setName(self,name):
        self.name = name

    def getName(self):
        return self.name

    def getId(self):
        return self.id    

class Student:
    def __init__(self,college):
        self.college = college

    def getCollege(self):
        return self.college

class Intern(Employee,Student):
    def __init__(self,id,college,period):
        Employee.__init__(self,id)
        Student.__init__(self,college)
        self.period = period

    def setDetails(self,name):
        self.setName(name)
    
    def getDetails(self):
        return 'ID = {} \n Name = {} \n College = {} \n Period = {} months'.format(self.getId(),self.getName(),self.getCollege(),self.period)



myIntern = Intern(input('Enter the Id : '),input('Enter the college Name : '),input('Enter the period')) 
myIntern.setDetails(input('Enter the Name'))       
print(myIntern.getDetails())