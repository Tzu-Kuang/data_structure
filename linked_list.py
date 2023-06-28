class node:
    def __init__(self, data = None):
        self.data = data
        self.next = None

class linked_list:
    def __init__(self):
        self.head = node()
        
    def append(self, data):
        new_node = node(data)
        cur  = self.head
        while cur.next != None:
            cur = cur.next
        cur.next = new_node

    def length(self):
        cur = self.head
        total = 0
        while cur.next != None:
            cur = cur.next
            total += 1
        return total
    
    def display(self):
        ele = []
        cur_node = self.head
        while cur_node.next != None:
            cur_node = cur_node.next
            ele.append(cur_node.data)
        return ele

    def get(self, index):
        if index >= self.length():
            print("Error! The index you entered is out of range")
            return None
        cur_node = self.head
        cur_idx = 0
        while True:
            cur_node = cur_node.next
            if cur_idx == index:
                return cur_node.data
            cur_idx += 1
        
    
    def erase(self, index):
        if index >= self.length():
            print("Error! The index you entered is out of range!")
            return None
        cur_idx = 0
        cur_node = self.head
        while True:
            last_node = cur_node
            cur_node = cur_node.next
            if cur_idx == index:
                last_node.next = cur_node.next
                return 
            cur_idx += 1

lst = linked_list()
lst.append(1)
lst.append(2)
lst.append(3)
lst.append(4)
lst.append(5)
print(lst.display())
lst.erase(1)
print(lst.display())