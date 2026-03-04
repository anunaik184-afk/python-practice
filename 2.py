 #1. this is the program to perform basic airthmatic operation like adition,subtraction,multiplication,division

#Airthmatic Operations
a=int(input("Enter the value of a:"))
b=int(input("Enter the value of b:"))
print(f"sum of the numbers : {a+b}")
print(f"subtraction  of the numbers : {a-b}")
print(f"multiplication of the numbers : {a*b}")
print(f"division of the numbers : {a/b}")


#2. Swap Two Variables:
# Write a Python program that swaps the values of two variables with and without using a third variable.
# without using third element
a=10
b=3
a,b=b,a
print(f"value of a:{a}")
print(f"value of b:{b}")

#with using third element
a=10
b=3
c=a
a=b
b=c
print(f"value of a:{a}")
print(f"value of b:{b}")

