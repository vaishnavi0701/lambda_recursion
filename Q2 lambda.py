

# Write a Python program to sort a list of tuples using Lambda.


subject_marks = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
print(subject_marks)

subject_marks.sort(key = lambda x: x[1])
print(subject_marks)


# x=input("enter name")
# y=int(input("enter age"))
# if x=="shreshta":
#     print("my name is shreshta")
# if y==20:
#     print("my age is 20")

