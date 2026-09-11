print('Hello world')
name = "Jordan"
print("Hello there " + name)
#comment - does not execute - comments start with a #
#Comment - python is case sensitive - space doesnt matter in the code
#string data type can use double qoutes or single qoutes 
print("hi")
print('hi') 

#print it's "groovy" day
#causes problems due to qoutes in qoutes 
#we can use esqcape characters to fix this problem
print("it's \"groovy\" day")  #this is how you use escape sequences to fix the problem with quotes in quotes

#variables - a variable is a name that refers to a value
#a name container that holds a value - we can use variables to store data and manipulate it later



final_grade = 97 
print("your final grade: " + str(final_grade)) #we have to convert the integer to a string to concatenate it with the string

final_grade = 99
print("your final grade: " + str(final_grade)) #we have to convert the integer to a string to concatenate it with the string

#concatenate string seen above - we can use the + operator to concatenate strings together

#formatting strings (f string)
name = "Jordan"
print(f"Hello {name}! I see your final grade was {final_grade}!") 

print ("Hello " + name + "! I see your final grade was " + str(final_grade) + "!") #this is the old way of formatting strings - we have to convert the integer to a string to concatenate it with the string