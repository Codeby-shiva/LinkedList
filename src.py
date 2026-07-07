# Node class
class Node:
    def __init__(self,value):
        self.data = value
        self.next = None


# LinkedList Class
class LinkedList:
    def __init__(self):
        self.head = None
        self.node_conut = 0

    def insert_by_head(self,value):
        new_node = Node(value)

        if self.head == None:
            self.head = new_node
            self.node_conut += 1 

        else:
            new_node.next = self.head
            self.head = new_node
            self.node_conut += 1


    def insert_by_tail(self,value):
        new_node = Node(value)

        if self.head == None:
            self.head = new_node

        curr = self.head
        while curr.next != None:
            curr = curr.next

        curr.next = new_node
        self.node_conut += 1

    def traverse(self):
        if self.head == None:
            return "Empty LinkList"

        curr = self.head
        while curr != None:
            print(curr.data)
            curr = curr.next


    def delete_by_value(self,value):
        if self.head.data == value:
            self.head = self.head.next
        
        curr = self.head

        while curr.next.data != value:
            curr = curr.next
            if curr.next == None:
                break
        if curr.next != None:
            curr.next = curr.next.next
        else:
            print("value not found")
            return
        
        # Decrement node count        
        self.node_conut -= 1


    def __str__(self):
        
        ll = ""

        if self.head == None:
            return "Empty LL"
        
        else:
            curr = self.head
            while curr != None:
                ll = ll + curr.data + "->"
                curr = curr.next

            return ll[:-2]


    def __len__(self):
        return  self.node_conut