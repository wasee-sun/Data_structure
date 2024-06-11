from Stack_Queue_Deque import Stack


class Node:
    
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack_ll: #follows lifo 
    
    #Incase of stack the head is the last element of the stack
    def __init__(self):
        self.head = None
        
    def push(self, data): # push the data to the stack
        new_node = Node(data)
        new_node.next = self.head 
        self.head = new_node # new node is the head
        
    def pop(self):
        if self.head is None: # empty stack
            return "Empty stack"
        popped_item = self.head
        self.head = self.head.next # head is popped and next is the head
        return popped_item.data
    
    def peek(self):
        return self.head.data
    
    def is_empty(self):
        return self.head is None
    
    def size(self):
        count = 0
        current = self.head
        while current is not None:
            count += 1
            current = current.next
        return count
    
    def printStack(self):
        current = self.head
        main_str = ""
        while current is not None:
            main_str += " <--" + str(current.data)
            current = current.next
        print(main_str)
        
class Queue_ll:
    
    #Incase of queue the head is the first element of the stack
    def __init__(self):
        self.head = None
        
    def enqueue(self, item): # here enqueue is O(n) time
        node = Node(item)
        current = self.head
        if current is None:
            self.head = node
            return
        while current.next:
            current = current.next
        current.next = node
        
    def dequeue(self): # here dequeue is O(1) time
        if self.head is None:
            return "Empty Queue"
        dequeued_item = self.head
        self.head = self.head.next
        return dequeued_item.data
    
    def peek(self):
        return self.head.data
    
    def is_empty(self):
        return self.head is None
    
    def size(self):
        count = 0
        current = self.head
        while current is not None:
            count += 1
            current = current.next
        return count
    
    def printQueue(self):
        current = self.head
        main_str = ""
        while current is not None:
            main_str += str(current.data) + "--> "
            current = current.next
        print(main_str)
        
        
class Queue_ST:
    
    # Using the stack class to build a queue
    def __init__(self):
        self.s1 = Stack() # main stack 
        self.s2 = Stack() # secondary stack
        
    def dequeue(self): # normal poping as the end of the stack is considered first item of the queue
        if self.s1.items == []:
            return "Empty Queue"
        return self.s1.pop()
    
    def enqueue(self, item):
        for i in range(self.s1.size()):
            org_item = self.s1.pop() # pop the items form the main stack
            self.s2.push(org_item) # push them in the secondary stack
        self.s2.push(item) # push item in the secondary stack
        for i in range(self.s2.size()):
            popped_item = self.s2.pop() # pop the item form the main stack
            self.s1.push(popped_item) # push them in the main stack again
    
    def size(self):
        return self.s1.size()
    
    def peek(self):
        return self.s1.peek()
    
    def is_empty(self):
        return self.s1.is_empty()
    
    def printQueue(self):
        main_str = ""
        for item in self.s1.items:
            main_str += " <--" + str(item)
        print(main_str)
    
            
if __name__ == "__main__":
    # s1 = Stack_ll()
    # print(s1.pop())
    # s1.push(1)
    # s1.push(8)
    # s1.push(4)
    # s1.printStack()
    # print(s1.peek())
    # print(s1.pop())
    # s1.push(5)
    # s1.printStack()
    # print(s1.size())
    # q1 = Queue_ll()
    # print(q1.dequeue())
    # q1.enqueue(1)
    # q1.enqueue(5)
    # q1.enqueue(2)
    # q1.printQueue()
    # print(q1.peek())
    # print(q1.dequeue())
    # q1.enqueue(34)
    # q1.printQueue()
    # print(q1.size())
    q1 = Queue_ST()
    print(q1.dequeue())
    q1.enqueue(1)
    q1.enqueue(5)
    q1.enqueue(2)
    q1.printQueue()
    print(q1.peek())
    print(q1.dequeue())
    q1.enqueue(34)
    q1.printQueue()
    print(q1.size())
