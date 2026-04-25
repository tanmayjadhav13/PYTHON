# enter three number and find the greater number

num1 = int(input("Enter first number : "))
num2 = int(input("Enter secound number : "))
num3 = int(input("Enter third number : ")) 

if(num1> num2 and num3):
    print("greater number is",num1)
elif(num2> num3 and num1):
    print("greater number is",num2)
else: 
    print("greater number is" ,num3)
    