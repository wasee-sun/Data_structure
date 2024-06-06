
#!linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None #* Mango object
     
    def insert_begin(self, data):
        if self.is_empty():
            self.head = Node(data)
            return
            
        node = Node(data) #* node.next = None  # Apple object
        node.next = self.head #* node.next none replace self.head
        self.head = node #* Apple -> Mango
        
    def insert_end(self, data): #* Grape > Apple > Mango > None
        if self.is_empty():
            self.head = Node(data)
            return
        
        node = Node(data)
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = node
        
    def insert_index(self, data, index):
        if self.is_empty():
            self.head = Node(data)
            return
        
        if index < 0 or index >= self.get_length():
            print("Index out of range")
            return
        
        if index == 0:
            self.insert_begin()
            return
        
        node = Node(data) #*LYchee
        current = self.head
        i = 0
        while i < self.get_length():
            if i == index - 1:
                node.next = current.next
                current.next = node
            current = current.next
            i += 1
            
    def check_value(self, data):
        current = self.head
        while current is not None:
            if current.data == data:
                return True
            current = current.next
            
        return False
            
    def insert_after_value(self, data, value):
        if self.is_empty():
            print("Empty value")
            return
        
        if self.check_value(value):
            current = self.head
            node = Node(data) #* Pineapple
            while current is not None:
                if current.data == value:
                    node.next = current.next #*jackfruit
                    current.next = node
                current = current.next
        else:
            print("Object in list not found")
            return
        
    def insert_before_value(self, data, value):
        if self.is_empty():
            print("Empty value")
            return
        
        if self.check_value(value):
            if self.head.data == value:
                self.insert_begin()
                return
            
            current = self.head
            node = Node(data) #* Orange
            while current.next is not None:
                if current.next.data == value: #*Apple before Lychee
                    node.next = current.next
                    current.next = node
                    return
                current = current.next
        else:
            print("Object in list not found")
            return
        
    def insert_value(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)
            
    def remove_begin(self):
        if self.is_empty():
            print("Empty head")
            return
        
        self.head = self.head.next
        
    def remove_end(self):
        if self.is_empty():
            print("Empty head")
            return
        
        current = self.head
        while current.next.next is not None:
            current = current.next
            
        current.next = None
        
    def remove_index(self, index):
        if self.is_empty():
            print("Empty head")
            return
        
        length = self.get_length()
        
        if index < 0 or index >= length:
            print("Index out of range")
            return
        
        if index == 0:
            self.remove_begin()
            return
        
        current = self.head
        i = 0
        while i < length:
            if i == index - 1:
                current.next = current.next.next
                return
            current = current.next
            i += 1
            
    def remove_value(self, value):
        
        if self.check_value(value):
            if self.head.data == value:
                self.remove_begin()
                
            current = self.head
            while current.next is not None:
                if current.next.data == value:
                    current.next = current.next.next
                current = current.next
        else:
            print("Object in list not found")
            return
    
    def reverse_list(self):
        current = self.head.next
        new_head = self.head
        new_head.next = None
        while current is not None: #*Apple
            temp = current #*Apple
            current = current.next #*Orange
            temp.next = new_head #*Apple.next == Grape
            new_head = temp #* Apple
        self.head = new_head
        
    def ltr_rotation(self, num_val):
        i = self.get_length()
        current = self.head
        tmp = None
        
        if i == num_val:
            self.reverse_list()
            return
        
        while i > 0:
            if i == num_val + 1:
                tmp = current.next
                current.next = None
                break
            current = current.next
            i -= 1
        temp = self.head
        self.head = tmp
        while tmp.next is not None:
            tmp = tmp.next
        tmp.next = temp
        
    def get_length(self):
        i=0
        current = self.head
        while current is not None:
            i += 1
            current = current.next
            
        return i
    
    def is_empty(self):
        if self.head is None:
            print("Empty head")
            return True
        return False
        
    def print_list(self):
        current = self.head
        main_str = ""
        while current is not None:
            main_str += current.data + "->> "
            current = current.next
        print(main_str)
    

if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_begin("Mango")
    # print(ll.head)
    # print(ll.head.data)
    ll.insert_begin("Apple")
    ll.insert_begin("Grape")
    ll.insert_end("Jackfruit")
    ll.insert_index("Lychee", 2)
    # ll.remove_end()
    # ll.remove_index(2)
    ll.insert_after_value("Pineapple", "Jackfruit")
    ll.insert_before_value("Orange", "Lychee")
    ll.remove_value("Lychee")
    # ll.reverse_list()
    # ll.ltr_rotation(2)
    ll.print_list()