from dataclasses import dataclass
from typing import TypeVar
Node = TypeVar("Node")
@dataclass
class Node:
    id: int
    x: int
    y: int
    next: Node = None ##this means that there is no next (by Default) unless i specify one

node = Node(1,10,20)
my_list = node

#example for adding next
node.next = Node(2,10,30, Node(3,50,60))# that means the next node has also a next node with values of(3,50,60) and the next after it is by Default None
print(my_list)
##########################################################################
#%%
## We can also use linked lists in Dictionaries
node3 = {"id": 3,"x" :50,"y":60, "next":None}
node2 = { "id": 2, "x": 10, "y": 30, "next": node3}
node1 = { "id": 1, "x": 10, "y": 20, "next": node2}
lst2 = node1
print(lst2)
# %%
##########################################################################
def search(lst,id): # DATACLASS
    while lst:
        if lst.id == id:
            print("Found")
        lst = lst.next
#%%
def search(lst,id): #DICTIONARIES
    while lst:
        if lst['id'] == id:
            print("Found")
        lst = lst['next']
##########################################################################
#%%
def insert(lst, new_node):  ######### Inserting a new node to a list 
    if lst in None:
        return new_node
    curr = lst
    while curr.next:
        curr = curr.next
    curr.next = new_node
    return lst
##########################################################################
#%%
def remove_from_list(lst, id):
    current = lst
    prev = lst
    while current:
        if current.id == id:
            if prev is lst:
                lst = current.next
            else:
                prev.next = current.next
        prev = current
        current = current.next
    return lst
##########################################################################
#%%
def reversed_linked_list_recursive(node):
    if node is None or node.next is None:
        return node
    
    reversed_list = reversed_linked_list_recursive(node.next)

    node.next.next = node
    node.next = None

    return reversed_list
#%%
def reverse_linked_list(head):#non recursive
    prev_node = None
    current_node = head
    while current_node is not None:
        next_node = current_node.next
        current_node.next = prev_node
        prev_node = current_node
        current_node = next_node
    return prev_node
##########################################################################
#%%
def find_circle(lst):
    slow = lst
    fast = lst

    while slow and fast:
        slow = slow.next
        fast = fast.next.next

        if slow is fast:
            return True
    return False
#%%
def print_sorted(n):
    head = None
    for i in range(n):
        value = int(input("Enter an integer :"))
        head = insert_sorted(head,value)

    current = head
    while current :
        print(current.value , end =' -> ')
        current = current.next
    print("None")


def insert_sorted(head, value):
	new_node = Node(value)

	if head is None or value < head.value:
		new_node.next = head
		return new_node

	current = head
	while current.next and value > current.next.value:
		current = current.next
	new_node.next = current.next
	current.next = new_node
	
	return head
#%%
