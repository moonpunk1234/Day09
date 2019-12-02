#8. Classes Inheritance
#==================================

#class ChildClassName(ParentClass):
#    --snip--

#Inheritance
#You don’t always have to start from scratch when writing a class. If the class 
#you’re writing is a specialized version of another class you wrote, you can 
#use inheritance. When one class inherits from another, it automatically takes 
#on all the attributes and methods of the first class. 

#p = Employee()
#p.whoisThis()
#p.walk()
#p.run()

# parent class
class Person:
		
	def __init__(self):
		print("Person is ready")
	
	def whoisThis(self):
		print('Person')
		
	def walk(self):
		print('Person can walk')

# child class
class Employee(Person):
	def __init__(self):
		super().__init__()
		print("Employee is ready")
	
	def whoisThis(self):
		print('Employee')
		
	def run(self):
		print('Person can run')

p = Employee()
p.whoisThis()
p.walk()
p.run()

