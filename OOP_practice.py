class Person:
    def __init__(self,name,occupation):
        self.name= name
        self.occupation= occupation
    def info(self):
        print(f"{self.name} is a {self.occupation}")

class Programmer(Person):
    def showSalary(self):
        print("Salary is 50K")

a=Programmer("Marij","Data Scientist")
a.info()
a.showSalary()


"""
Exercise 41. Rectangle class
"""
class Rectangle:
    def __init__(self,width,length):
        self.width= width
        self.length= length

    def Perimeter(self):
        return 2*self.width+self.length
    
    def Area(self):
        return self.width*self.length
    
    def Display(self):
        print(f"The Width of the Rectangle is {self.width}")
        print(f"The Length of the Rectangle is {self.length}")
        print(f"The Perimeter of the Rectangle is {self.Perimeter()}")
        print(f'The Area of the Rectangle is {self.Area()}')
class Parallelepipede(Rectangle):
        def __init__(self,width,length,height):
            Rectangle.__init__(self,width,length)
            self.height= height

        def Volume(self):
            return self.width*self.length*self.height
        
myRectangle=Rectangle(5,7)
print("----------------------------------------------------")
myRectangle.Display()
myParallelpipede= Parallelepipede(5,7,8)
print("The volume of the Parallelepipede is ",myParallelpipede.Volume())


"""
Exercice 42: Person class and child Student class
"""

class Person:
    def __init__(Self,name,age):
        Self.name= name
        Self.age= age
    def Display(Self):
        print(f"The name of the Person is {Self.name} and the age of the Person is {Self.age}")

class Student(Person):
    def __init__(Self, name, age, section):
        Person.__init__(Self,name,age)
        Self.section = section
    def Display(Self):
        print(f"The Name of the student is {Self.name} and the age of the student is {Self.age} and the section is {Self.section}")

record=Person("Marij", 23)
record.Display()
data= Student("Ali",24,"BSCS-7TH-1E")
data.Display()

"""
Exercise 43. Bank Account class
"""
class Bankaccount:
    def __init__(self,accountNumber,name,balance):
        self.accountNumber= int(accountNumber)
        self.name= str(name)
        self.balance = int(balance)

    def Deposit(self,d):
        self.balance = self.balance + d
    
    def Withdrawal(self,w):
        if (self.balance < w):
            print("Insufficient balance ! ")
        else:
            self.balance = self.balance -w
        
    def Bankfees(self):
        self.balance = (95/100)*self.balance
    
    def Display(self):
        print("Account Number : " , self.accountNumber)
        print("Account Name : " , self.name)
        print("Account Balance : " , self.balance , "PKR")

myaccount=Bankaccount(100123,"Marij",5000)
myaccount.Withdrawal(500)
myaccount.Deposit(300)
myaccount.Display()