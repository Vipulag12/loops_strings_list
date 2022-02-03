# Python script to find next prime number of a given number

num = int(input("Enter your number : "))
prime = True

for i in range (2,num):
    if num%i==0:
        prime = False

if prime:
    print("this no. is prime")
else:
    print("This no. is not prime") 