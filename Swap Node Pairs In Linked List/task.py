def swap_pairs(head):
    if head is None or head.next is None:
        return head
    new_head = head.next
    probe = head
    
    while probe is not None and probe.next is not None:
        first = probe
        second = probe.next
        next_pair = second.next
        second.next = first
        if next_pair is not None and next_pair.next is not None:
            first.next = next_pair.next
        else:
            first.next = next_pair
        probe = next_pair
        
    return new_head
