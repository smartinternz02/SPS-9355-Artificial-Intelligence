def productDesign():
    print("THE REFERNCES ARE:")
    print("https://learntocodewith.me/posts/product-design-guide/")
    print("https://cityos.io/tutorial/2023/Product-design-basics")
	
def pythonProgramming():
    print("THE REFERNCES ARE:")
    print("https://www.w3schools.com/python/")
    print("https://www.tutorialspoint.com/python/index.htm")
	
def Django():
    print("THE REFERNCES ARE:")
    print("https://www.geeksforgeeks.org/django-tutorial/")
    print("https://www.tutorialspoint.com/django/index.htm")
	
def softwareLifecycles():
    print("THE REFERNCES ARE:")
    print("https://www.tutorialspoint.com/sdlc/index.htm")
    print("https://www.javatpoint.com/software-development-life-cycle")
	
def javaprogramming():
    print("THE REFERNCES ARE:")
    print("https://www.w3schools.com/java/")
    print("https://www.javatpoint.com/java-tutorial")
    
def flask():
    print("THE REFERNCES ARE:")
    print("https://www.tutorialspoint.com/flask/index.htm")
    print("https://www.fullstackpython.com/flask.html")
	
def inputRole(x):
    List=[]
    
    if(x==1):
        skillslacking = list(int(input("Enter skill lacking  :").split("")))
        List=List.append(skillslacking)
        length = len(List)
        while(length>0):
            for k in skillslacking:
                if(k == 1):
                    productDesign()
                elif(k == 2):
                    pythonProgramming()
                elif(k==3):
                    Django()
				    
                else:
                    print("I think your inputs are wrong")
		
        print("you are suitable for this job")
        print("application process")
					
    if(x == 2):

        skillslacking = list(int(input("Enter skills lacking  space").split("")))
        length = len(skillslacking)

        while(length>0):
            for k in skillslacking:

                if(k == 1):

                    softwareLifecycles()

                elif(k == 2):

                    pythonProgramming()
                elif(k==3):
                    flask()
                else:
                    print("I think your inputs are wrong")
                    
        print("you are suitable for this job")
        print("application process")
	
    if(x == 3):

        skillslacking = list(int(input("Enter skills lacking  space").split("")))
        length = len(skillslacking)

        while(length>0):
            for k in skillslacking:

                if(k == 1):

                    javaprogramming()
                elif(k == 2):
                    pythonProgramming()
                elif(k == 3):
                    flask()

                else:

                    print("I think your inputs are wrong")
        print("you are suitable for this job")
        print("application process")
		
		

print("HELLO!!!!!")
print("We are here to help you for finding a role...... ")
print("The vacancies are:")
print("     1. Product Manager")
print("     2. Software Engineer")
print("     3. Java Developer")


input_role = int(input("Enter the Role you are looking for : "))

if(input_role == 1):

	print("SKILLS REQUIRED FOR PRODUCT MANAGER ARE:")
	print("      1. Product Design") 
	print("      2. Python Programming ")
	print("      3. Django")

	inputRole(1)

elif(input_role == 2):

	print("SKILLS REQUIRED FOR SOFTWARE ENGINEER ARE:")
	print("      1. Software LifeCycle") 
	print("      2. Python Programming ")
	print("      3. Flask")

	inputRole(2)
elif(input_role == 3):

	print("SKILLS REQUIRED FOR JAVA DEVELOPER ARE:")
	print("      1. Java Programming	")
	print("      2. Python Programming ")
	print("      3. Flask")

	inputRole(3)
else:

	print("Sorry please enter the right input")
