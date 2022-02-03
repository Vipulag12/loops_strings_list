#Python script to remove duplicate from a list of strings
#  
num1 = int(input("Enter your number : "))
num2 = int(input("Enter your number : "))
num3 = int(input("Enter your number : "))
num4 = int(input("Enter your number : "))
num5 = int(input("Enter your number : "))

list1 =[num1, num2, num3, num4, num5]
list2= set(list1)
print(list2)