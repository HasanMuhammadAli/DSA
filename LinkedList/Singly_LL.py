class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_first(self, val):
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node
    
    def insert_last(self, val):
        new_node = Node(val)

        if not self.head:
            self.head = new_node
            return 
        
        curr = self.head
        prev = None
        while curr:
            prev = curr
            curr = curr.next
        
        prev.next = new_node

    def insert_pos(self, val, pos):
        new_node = Node(val)

        if pos == 0:
            new_node.next = self.head
            self.head = new_node
            return
        
        curr_pos = 0
        curr = self.head
        prev = None

        while curr and curr_pos < pos:
            prev = curr
            curr = curr.next
            curr_pos += 1

        if curr_pos != pos:
            return "Invalid position"
        
        prev.next = new_node
        new_node.next = curr

    def insert_after_val(self, val, value):
        new_node = Node(val)
        curr = self.head
        if not self.head:
            return "No LL Found"

        if value == curr.val:
            nxt = curr.next
            curr.next = new_node
            new_node.next = nxt
            return 
        
        while curr.next and curr.val != value:
            curr = curr.next
        
        if curr.val != value:
            return "Invalid Value"
        
        nxt = curr.next
        curr.next = new_node
        new_node.next = nxt
    

    def delete(self, val):
        curr = self.head
        prev = None

        while curr and curr.val != val:
            prev = curr
            curr = curr.next
        
        if curr is None:
            return "Element is not found."
        
        if prev is None:
            self.head = self.head.next

        prev.next = curr.next

    def delete_first(self):
        if self.head:
            self.head = self.head.next
            return

        return "No head to delete."
    


    def delete_last(self):
        if not self.head:
            return "No LL found."
        
        if self.head.next is None:
            self.head = None
            return
        
        curr = self.head
        prev = None

        while curr.next:
            prev = curr
            curr = curr.next
        
        prev.next = curr.next
