from Stack_Queue_Deque import Stack, Queue


class TreeNode:
    def __init__(self, data):
        self.data = data
        self.parent = None
        self.children = []

class Tree:
    def __init__(self):
        self.root = None
        self.stack = Stack() #? For DFS traversal
        self.queue = Queue() #* For BFS traversal

    def set_root(self, root):
        self.root = TreeNode(root)

    def add_child(self, child_dt, parent_dt):
        parent_obj = self.find_parent(parent_dt)
        if parent_obj:
            child_obj = TreeNode(child_dt)
            parent_obj.children.append(child_obj)
            child_obj.parent = parent_obj
            return
        print("Parent not found")

    def remove_child(self, child_dt, parent_dt):
        parent_obj = self.find_parent(parent_dt)
        if parent_obj:
            for child in parent_obj.children:
                if child.data == child_dt:
                        parent_obj.children.remove(child)
                        return
            print("Item not found")
            return
        print("Parent not found")

    def get_all_child(self, parent_dt):
        parent_obj = self.find_parent(parent_dt)
        if parent_obj.children:
            for child in parent_obj.children:
                print(child.data)
            return
        print("No child found")

    def find_parent(self, parent_dt, current = None): #Laptop > HP,Lenovo // phone >> iphone, samsung
        if self.is_empty():
            print("Empty Tree!")
            return
        if current == None:
            current = self.root
            if current.data == parent_dt:
                return current

        for child in current.children:
            if child.data == parent_dt:
                return child
            if child.children:
                value = self.find_parent(parent_dt, child)
                if value is not None:
                    return value
                
    def dfs_traversal(self, node = None): #*Uses Stack
        if node is None:
            node = self.root
            self.stack.push(node)
            print(self.stack.pop().data)
        
        if node.children:
            for i in range(len(node.children)-1, -1, -1):
                self.stack.push(node.children[i])
        
        while not self.stack.is_empty():
            popped_item = self.stack.pop()
            print(popped_item.data)
            if popped_item.children:
                self.dfs_traversal(popped_item)
                
    def bfs_traversal(self, node = None): #*Uses Queue
        if node is None:
            node = self.root
            self.queue.enqueue(node)
            print(self.queue.dequeue())
        
        if node.children:
            for child in node.children:
                self.queue.enqueue(child)
        
        while not self.queue.is_empty():
            popped_item = self.queue.dequeue()
            print(popped_item.data)
            if popped_item.children:
                self.bfs_traversal(popped_item)

    def is_empty(self):
        return self.root is None

    def get_level(self, node): # get level
        if node.parent is None:
            return 3
        return 3 + self.get_level(node.parent)   

    def printtree(self, node = None): # print the tree
        if node is None: # print root and recursive func
            print(self.root.data)
            self.printtree(self.root)
            return

        space = " " * self.get_level(node)
        prefix = space + "|__"

        if node.children != []: # if child node is not empty
            for child in node.children: # get the childs
                print(prefix + child.data)
                if child.children:
                    self.printtree(child)
                

        
if __name__ == '__main__':
    tree = Tree()
    tree.set_root("Electronics")
    tree.add_child("Laptop", "Electronics")
    tree.add_child("HP", "Laptop")
    tree.add_child("Mobile", "Electronics")
    tree.add_child("Monitor", "Electronics")
    tree.add_child("Iphone", "Mobile")
    tree.add_child("Lenovo", "Laptop")
    tree.add_child("Lenovo Flex 3", "Lenovo")
    tree.add_child("Lenovo Flex 5", "Lenovo")
    tree.add_child("HP 15", "HP")
    tree.add_child("HP 16", "HP")
    tree.add_child("HP 13", "HP")
    tree.add_child("Dell", "Laptop")
    tree.add_child("Dell XPS 14", "Dell")
    tree.add_child("Dell XPS 16", "Dell")
    tree.add_child("Samsung", "Mobile")
    tree.add_child("Samsung Galaxy Note 11", "Samsung")
    tree.add_child("Samsung S10", "Samsung")
    tree.add_child("Iphone 6s", "Iphone")
    tree.add_child("Iphone X", "Iphone")
    tree.add_child("Iphone Xs", "Iphone")
    # tree.get_all_child("Laptop")
    # tree.remove_child("Iphone", "Mobile")
    tree.printtree()
    # tree.bfs_traversal()
    
    
    
#?Electronics
#! -- Laptop
#! -- Mobile