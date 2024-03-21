#qt 1] my_list = ['apple', 'banana', 'orange']
#      o/p=apple, banana, orange

my_list = ['apple', 'banana', 'orange']
output = ', '.join(my_list)
print(f"o/p= {output}")

#qt 2] How would you convert a string to all lowercase?

string = 'Hello World!!'
lower_string = string.lower()
print(lower_string)

#qt 3] Show what len() does

string = "I love Python"
length = len(string)
print(f"Length of string is: {length}")

#qt 4] How do you copy an object in Python?

"""There are two ways to copy object in Python.
1.Shallow copy: It creates a copy of the object but references each element of the object.
2.Deep copy: It creates a copy of the object and the elements of the object"""

import copy
old_list = ['A','B',100,{1,2,3},[4,5,6]]
print(f"old_list before shallow copy: {old_list}")
#Shallow copy
shallow_copied_list = copy.copy(old_list)
shallow_copied_list[1] = 'Z'
shallow_copied_list[2] = 200
shallow_copied_list[4][0] = 10
shallow_copied_list[3].add(20)
print(f"old_list after changes in shallow copy: {old_list}") #string and int element didn't change, but all others change
print(f"shallow_copied_list after changes in shallow copy: {shallow_copied_list}")


old_list = ['A','B',100,{1,2,3},[4,5,6]]
deep_copied_list = copy.deepcopy(old_list)
deep_copied_list[1] = 'Y'
deep_copied_list[2] = 300
deep_copied_list[4][0] = 15
deep_copied_list[3].add(30)
print(f"old_list after changes in deep copy: {old_list}")   #nothing will change
print(f"deep_copied_list after changes in deep copy: {deep_copied_list}")


#qt 5] How can you convert a number to a string?

number = 256
num_to_str = str(256)
print(f"Now type of {number} is: {type(num_to_str)}")

#qt 6] my_list = ['apple', 'banana', 'orange', 'pear', 'grape']
#     o/p= {1: 'apple', 2: 'banana'}

my_list = ['apple', 'banana', 'orange', 'pear', 'grape']
my_dict = {}
for i in range(len(my_list)):
    my_dict[i+1] = my_list[i]

print(my_dict)


#qt 7] my_string = "hello Python"
#      o/p= hello Sql

my_string = "hello Python"
new_string = my_string.replace('Python', 'sql')
print(new_string)


#qt 8] my_string = "hello python"
#     o/p= h1 e1 l2 l2 o2  p1 y1 t1 h1 o2 n1

my_string = "hello python"
new_string = ''
words = my_string.split()

for word in words:
    for ch in word:
        if ch in 'aeiou':
            new_string = new_string + ch + str(my_string.count(ch)) + ' '
        else:
            new_string = new_string + ch + str(word.count(ch)) + ' '

    new_string += ' '

print(new_string)

#qt 9] my_dict = {'a': 3, 'b': 2, 'c': 3, 'd': 1, 'e': 2}
'''       o/p= Maximum keys with their values:
                  a: 3
                  c: 3'''

my_dict = {'a': 3, 'b': 2, 'c': 3, 'd': 1, 'e': 2}

max_value = max(my_dict.values())
for k,v in my_dict.items():
    if v == max_value:
        print(f"{k}: {v}")

#qt 10] convert set into dict
'''     i/p=my_set = {('a', 1), ('b', 2), ('c', 3)}
    o/p= {'a': 1, 'c': 3, 'b': 2}'''

my_set = {('a', 1), ('b', 2), ('c', 3)}
my_dict = dict(my_set)
#print(my_dict)
sorted_dict = dict(sorted(my_dict.items(), key = lambda x: x[1]))
print(sorted_dict)




