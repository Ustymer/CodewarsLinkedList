def sorted_insert(head, data):
    if head is None or data <= head.data:
        res = Node(data)
        res.next = head
        return res
    probe = head
    maker = Node(data)
    while probe is not None:
        if data >= probe.data:
            if probe.next is None:
                probe.next = maker
                return head
            if probe.next.data >= data: 
                maker.next = probe.next
                probe.next = maker
                return head
        probe = probe.next
