""" Data Structure : Tree"""

"""Tree are used to represent the hierarchical relationships between elements."""

"""In python trees can be implemented using classes and objects"""

"""Creation of tree"""

"""For creating a tree in python, we can define a class for the class for the nodes of the tree, and use objects of this class to represent the nodes"""


class TreeNode: 
    def __init__(self, data):
        self. data = data
        self.left = None
        self.right = None
    
# Creating a tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)


""" Traversing a tree """

"""Here are common three ways to traverse a tree"""

"""In_order Traversal"""

def in_order(node):
    
    if node is not None:
        in_order(node.left)
        print(node.data)
        in_order(node.right)

# In-order traversal of the tree
print("in_order traversal")
in_order(root)


"""Pre_order Traversal"""

def pre_order(node):
    if node is not None:
        print(node.data)
        pre_order(node.left)
        pre_order(node.right)

# pre-order traversal
print("pre_order traversal")
pre_order(root)

"""Post_order traversal"""

def post_order(node):
    if node is not None:
        post_order(node.left)
        post_order(node.right)
        print(node.data)

# post_order traversal 
print("post_order traversal")
post_order(root)


"""Finding elements in a tree"""

def find(node, data):
    if node is None:
        return False
    elif node.data == data:
        return True
    elif node.data< data:
        return find(node.left,data)
    else:
        return find(node.right, data)

print(find(root, 2))