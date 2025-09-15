# Principle 1: Beautiful is better than ugly

# Bad Code
a = 4
b = 2
c = a + b
print(c)  # output : 6

# Good code 
num1 = 4 
num2 = 2

sum = num1 + num2
num1 and num2
print(sum)          # output : 6 

# Principle 2: Explicit is better than implicit

# Bad code
lst = [1, 2, 3, 4, 5]
result = filter(lambda x: x % 2 == 0, lst)

print(list(result))             # [2, 4]

# Good code
def is_even(num):
    return num % 2 == 0

numbers = [1, 2, 3, 4, 5]
even_numbers = filter(is_even, numbers)

print(list(even_numbers))  # [2, 4]

# Simpler is better than complex

# Using for loop to create a new list
squares = []
for i in range(10):
    squares.append(i**2)
print(squares)              # Output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# Using list comprehension
squares = [i**2 for i in range(10)]
print(squares)               # Output; [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]