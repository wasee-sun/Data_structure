from heap_tree import Min_Heap

class Priority_Queue:
    def __init__(self):
        self.queue = Min_Heap()
        
    def enqueue(self, ele):
        self.queue.insert(ele)
        
    def dequeue(self):
        return self.queue.extract_min()
        
    def peek(self):
        return self.queue.get_min()
    
    def change_priority(self, old, new):
        self.queue.update(old, new)
        
    def is_empty(self):
        return len(self.queue) == 0