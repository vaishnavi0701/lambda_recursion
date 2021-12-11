# Write a Python program to calculate the sum of a list of numbers.


def list(num):
    if len(num)==1:
        return num[0]
    else:
        return num[0] + list(num[0:])
        
print(list([1,2,3,4,5]))


