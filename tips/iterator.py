# A simple list
fruits = ["apple", "banana", "cherry"]

# Create an iterator from the list
fruit_iterator = iter(fruits)

# Access elements one by one using next()
print(next(fruit_iterator))  # Output: apple
print(next(fruit_iterator))  # Output: banana
print(next(fruit_iterator))  # Output: cherry

# If we call next() again, it will raise StopIteration
# print(next(fruit_iterator))  # Uncommenting this line will cause an error
