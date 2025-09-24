""" Python provides two built - in functions : enumerate and zip"""

"""Using enumerate"""

my_list = ['apple', 'banana', 'orange']

for i, item in enumerate(my_list):
    print(i, item)


"""zip"""

list_a = [1, 2, 3]
list_b = ['a', 'b', 'c']

for item_a, item_b in zip(list_a, list_b):
    print(item_a, item_b)


"""We can use it together that is so powerful"""

my_list1 = ['apple', 'banana', 'orange']
for i, item in enumerate(zip(my_list1, range(len(my_list1)))):
    print(i, item[0], item[1])


