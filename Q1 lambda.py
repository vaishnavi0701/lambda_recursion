# Write a Python program to create a function that takes one argument, and that argument will be multiplied with an unknown given number.



def num(n):
 return lambda x : x * n
var=num(2)
print("2 times :", var(15))
var=num(3)
print("3 times :", var(15))
var=num(4)
print("4 times :",var(15))
var=num(5)
print("5 times :", var(15))
