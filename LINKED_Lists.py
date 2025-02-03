from dataclasses import dataclass
from typing import TypeVar
Node = TypeVar("Node")


@dataclass
class Node:
    id: int
    x: int
    y: int
    next: Node = None ##this means that the next is a new member of the class that his values are none by default

node = Node(1,10,20)
my_list = node

#example for adding next
node.next = Node(2,10,30, Node(3,50,60))# that means the next node has also a next node with values of(3,50,60) and the next after it is by Default None
print(my_list)