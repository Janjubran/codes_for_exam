from dataclasses import dataclass
@dataclass
class students:
    name: str
    age: int
    id: int
    Major: str = 'CS'

student3 = students('chris',5,3234234)
print(student3.id)

#%%
class Node:
    def __init__(self, value, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right

node1 = Node(9)
node2 = Node(10)
root = Node(3)
root.left = node1
root.right = node2
tree_list = [root.value, root.left.value, root.right.value]
print(tree_list)
#%%
