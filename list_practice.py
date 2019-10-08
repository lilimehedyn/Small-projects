# create a list
nums = [1, 3, 5, 35, 567, 45673, 8, 890, 1000]
print(nums)

# print out a list with another name
my_list = []
for n in nums:
    my_list.append(n)
print(my_list)

# list comprehension, easier to code and understand
my_list = [n for n in nums]
print(my_list)

my_list = [n*n for n in nums] # n*n is a square of 2 numbers in the list
print(my_list)

my_list = [n for n in nums if n%2 == 0] # find and print out even numbers
print(my_list)

# nested loops
my_list = []
for letter in 'abcd':
    for n in nums:
        my_list.append((letter, n))
print(my_list)

# nested loops, list comprehension, the result will be the same
my_list = [(letter,n) for letter in 'abcd' for n in nums]
print(my_list)

#set comprehension
numbers = [1,2, 4, 6, 6, 7, 3, 2, 1, 5, 6, 8, 9, 10, 123, 34, 4, 7, 87, 11111, 11111, 2, 5]

my_set = {n for n in numbers}
print(my_set)

#Generator Expressions

def gen_func(numbers):
    for n in numbers:
        yield n*n

my_gen = gen_func(numbers)

for i in my_gen:
    print(i)

# Using comprehension

my_gen = (n*n for n in numbers)
for i in my_gen:
    print(i)
