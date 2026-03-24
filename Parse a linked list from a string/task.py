def linked_list_from_string(list_repr: str) -> Node | None:
    if list_repr == 'None':
        return None
    workin = list_repr.split(' -> ')
    node = None
    for i in workin[:-1][::-1]:
        node = Node(int(i), node)
    return node
