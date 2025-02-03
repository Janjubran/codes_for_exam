def s_push(s, node):
    if s is None:
        return node 
    node.next = s
    return node
def s_top(s):
    return s
def s_pop(s):
    if s is None:
        return None, None 
    new_s = s.next
    s.next = None
    return new_s, s
