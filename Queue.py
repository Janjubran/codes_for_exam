def q_push(q, node):
    if q is None:
        return node
    
    curr = q
    while curr.next:
        curr = curr.next
    curr.next = node
    return q
#%%
def q_pop(q, node):
    if q is None:
        return None, None
    new_q = q.next
    q.next = None
    return new_q, q
