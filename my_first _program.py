#part 1: hello world

print ("hello, my name is Catherine: ")

print("I am learning python : ")

print("=" *25)

#part 2: user input 

name = input("enter your name: ")

age = input("enter your age: ")

print("welcome ", name + "you are", age," years old " )

print("=" * 25)

#part3 simple calculator

num1 = float(input("Enter first number: "))

num2 = float(input("Enter second number: "))

sum_result = num1 + num2
difference = num1 - num2
product = num1 * num2

print("Sum =", sum_result)
print("Difference =", difference)
print("Product =", product)

print("=" *25)

#part 4

number = int(input("enter a number: "))

if number % 4 == 0 :
    print("The number is even")
else:
    print("The number is odd")  

print("=" * 25)

#part 5:Simple grade checker

marks = int(input("Enter marks :"))

if marks >= 80 and marks <= 100:
    print("Grade : A")
elif marks >= 70 and marks <= 79:
    print("Grade : B")  
elif marks >= 60 and marks <= 69:    
    print("Grade : C") 
elif marks >= 50 and marks <= 59:   
    print("Grade : D")
elif marks < 50:    
    print("Grade: F")
else:
    print("Invalid marks")    

print("=" *25)