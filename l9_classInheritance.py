#8. Classes Inheritance
#==================================

#class ChildClassName(ParentClass):
#    --snip--

#Inheritance
#You don’t always have to start from scratch when writing a class. If the class 
#you’re writing is a specialized version of another class you wrote, you can 
#use inheritance. When one class inherits from another, it automatically takes 
#on all the attributes and methods of the first class. 

# parent class
class Bird:
		
	def __init__(self):
		print("Bird is ready")

	def whoisThis(self):
		print("Bird")

	def swim(self):
		print("Swim faster")

# child class
class Penguin(Bird):

	def __init__(self):
		# call super() function
		super().__init__()
		print("Penguin is ready")

	def whoisThis(self):
		print("Penguin")

	def run(self):
		print("Run faster")

peggy = Penguin()
peggy.whoisThis()
peggy.swim()
peggy.run()

