#qt 1] reverse a list in Python without using any built-in functions

def reverse_list(list):
    return list[::-1]

my_list = [10,20,30,40,50]
rev_list = reverse_list(my_list)
print(f"The reverse list is {rev_list}")

#qt 2] sort a list without using any built-in functions.
#      Ex: my_list = [64, 34, 25, 12, 22, 11, 90]


def sort_list(list):
    n = len(list)
    for i in range(n):
        for j in range(0, n-i-1):
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]
    return list

my_list = [64, 34, 25, 12, 22, 11, 90]
sorted_list = sort_list(my_list)
print(f"The sorted list is : {sorted_list}")

#qt 3] find the highest number in a list without using any built-in functions
def largest_number(list):
    largest_num = 0
    for num in list:
        if num > largest_num:
            largest_num = num
    return largest_num

my_list = [64, 34, 25, 120, 22, 11, 90]
largest_num = largest_number(my_list)
print(f"The largest number in the list is: {largest_num}")

#qt 4] extract the letters from the string "a1b2c3" o/p=abbccc

my_string = "a1b2c3"
output_string = ''
for i in range(0,len(my_string),2):
    output_string = output_string + (my_string[i] * int(my_string[i+1]))

print(f"Output string is : {output_string}")


#qt 5] What is the difference between remove() function and del statement?

#The remove() method is a list method that is used to remove the first
#occurrence of a specified element from the list.

my_list = [25,35,45,55,65,75,85,95]

my_list.remove(55)
print(f"Updated list is: {my_list}")

#The del statement is a more general-purpose tool for removing elements from a list.
# It can be used to remove elements by index or to delete the entire list.

del my_list[4]
print(f"Updated list is: {my_list}")

del my_list[3:6]
print(f"Updated list is: {my_list}")

#qt 6] How to remove whitespaces from a string in Python?

my_string = "Python is a high level programming language."
new_string = my_string.replace(' ','')
print(f"The new string after removing all the whitespaces is: {new_string}")

#qt 7] Write a Python script that iterates over two lists simultaneously, list_1 and list_2.
'''            If during iteration, the element in list_1  is equal to 'Y' and the corresponding element in list_2 is equal to 33, 
           the loop should break. Print each pair of elements as they are iterated over. Ensure that the loop terminates when 
           this condition is met.'''

list_1 = ['A', 'B', 'G', 'Y', 'Z', 'S', 'W']
list_2 = [10, 20, 30 ,33, 40, 50, 60]
n = len(list_1)
for i in range(n):
        print(f"The elements pairs of list_1 and list_2 are: {list_1[i]},{list_2[i]}")
        if list_1[i] == 'Y' and list_2[i] == 33:
            break
        else:
            continue
print(f"The given condition is met in this iteration")

#qt 8] What are the different types of operators in Python explain with example
#1.Arithmetic Operators(+,-,/,//,%,*,**): Used for mathematical operations.

a=10
b=2
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b)
print(a%b)
print(a**b)

#2.Comparison Operators(==,!=,<,>,<=,>=):Used to compare values and return Boolean results.

a=10
b=2
print(a == b)
print(a != b)
print(a < b)
print(a > b)
print(a <= b)
print(a >= b)

#3.Logical Operators(and,or,not):Used to perform logical operations on Boolean values.

print(True and False)
print(True or False)
print(not True)

#4. Assignment Operators(+=,-=,*=,/=):Used to assign values to variables.

a = 10
a += 5
print(a)
a -= 2
print(a)
a *= 2
print(a)
a /= 2
print(a)

#5.Bitwise Operators(&,|,^,~):Used for bitwise operations on integers.

a = 5   #0101
b = 4   #0100

print(a & b)
print(a | b)
print(a ^ b)
print(~a)

#6.Membership Operators(in,not in):Used to test whether a value is a member of a sequence

a = 5 in range(0,10)
print(a)

b=5 not in range(0,10)
print(b)

#7.Identity Operators(is):Used to compare the memory addresses of two objects.

a = [10,20,30]
b = [10,20,30]
c = a
print(a == b)
print(a is b)
print(a is c)

#qt 9] How to create a Unicode string in Python?

#In Python 3, all strings are Unicode by default.

unicode_string_escape = "This is a Unicode string: \U0001F31F \U0001F32F \U0001F30F \U00010001"
print(unicode_string_escape)

#qt 10] What are the rules for a local and global variable in Python explain with example

#They will be resolved or accessed acc to the LEGB rule
#(LEGB) Rule: Local-> Enclosed-> Global -> Built-in

from math import e

x = 'GLOBAL:: local and enclosed values were not available'
def func1():
    x = 'LOCAL:: local value was available'
    print(x)

def outer():
    x = 'ENCLOSED:: local value was not available'
    def inner():
        print(x)
    inner()

def func2():
    print(x)

func1()
outer()
func2()
print(f"BUILT IN = {e} :: local,enclosed and global values were not available")



#qt 11] What are functions in Python explain with Example

"""Function is a block of code that performs a specific task.
They are reusable and can be called multiple times within a program.
Functions help in organizing and modularizing code, making it more readable, maintainable, and efficient.

for eg the add function in the following program is defined once and used many times."""

def add(*args):
    sum = 0
    for arg in args:
        sum = sum + arg
    return sum

print(add(4,5,6,7))
print(add(10,20,30,40,50,60))



