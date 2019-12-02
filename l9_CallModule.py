from os import system
from Calculator import Calc

c=Calc()

while True: 
	print("====== Main Menu ========")
	print("1. Addition")
	print("2. Subtraction")
	print("3. Multiplication")
	print("4. Division")
	print("5. Exit")
	print("Enter your selection :",end="")
	choice =int( input())


	if choice ==1:
		x= int(input("Enter your frist value:"))
		y= int(input("Enter your second value:"))
		print(c.add(x,y))
	elif choice == 2:
		x= int(input("Enter your frist value:"))
		y= int(input("Enter your second value:"))
		
		print(c.sub(x,y))
	elif choice ==3:
		x= int(input("Enter your frist value:"))
		y= int(input("Enter your second value:"))
		print(c.mul(x,y))
		
	elif choice == 4:
		x= int(input("Enter your frist value:"))
		y= int(input("Enter your second value:"))
		print(c.div(x,y))
		
	elif choice==5:

		break    
	else:
		print('Invalid Selection')  

	print("Press Enter to continue ...") 
	input()
	system('cls')

