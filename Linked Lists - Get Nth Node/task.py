def get_nth(node, index):
    if node is None or index < 0:
        raise Exception("Invalid index")
    current = node
    count = 0
    while current is not None:
        if count == index:
            return current
        count += 1
        current = current.next
    raise Exception("Index out of range")
  
