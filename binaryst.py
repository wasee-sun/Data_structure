# binary tree is a set (no duplicates)
# traversal bfs or dfs
from Stack_Queue_Deque import Stack, Queue


class BTNode: #* Binary Node
    
    def __init__(self, val):
        self.val = val # val
        self.left = None #left node
        self.right = None #right node
        

class BST: # Binary Search Tree
    
    def __init__(self):
        self.root = None # root node
        self.stack = Stack() #* for DFS
        self.queue = Queue() #* For BFS
        
    def _is_empty_tree(self): # If empty tree
        return self.root is None
    
    def find_min(self): # find the minimum node
        return self._find_min(self.root)
    
    def _find_min(self, node):
        if node.left: # go to the left node
            return self._find_min(node.left)
        return node
    
    def find_max(self): #find the maximum node
        return self._find_max(self.root)
    
    def _find_max(self, node):
        if node.right: # go to the right node
            return self._find_max(node.right)
        return node
            
    def search(self, val): #search for the node
        if self._is_empty_tree(): # if there is no root
            print("No root found")
            return
        else:
            return self._search(val, self.root)
        
    def _search(self, val, node):
        if val == node.val: # if node found
            return True
        
        elif val < node.val and node.left is not None: # if node is on the left
            return self._search(val, node.left)
        
        elif val > node.val and node.right is not None: # if node is on the right
            return self._search(val, node.right)
        
        return False # if node not found
    
    def get_height(self): # find the height of the tree
        if self._is_empty_tree(): # if root is empty
            print("Empty tree")
            return
        return self._get_height(self.root)
    
    def _get_height(self, node): # find the height of the node
        if node == None: 
            return 0
        
        left_height = self._get_height(node.left) # left height
        right_height = self._get_height(node.right) # right height
            
        return max(left_height, right_height) + 1  # maximum between left and right plus the node
        
    def get_depth(self, node_v): # find depth of a node
        if self._is_empty_tree():
            print("Empty tree")
            return
        return self._get_depth(node_v, self.root)
        
    def _get_depth(self, node_v, cur_node):
        if cur_node.val == node_v:
            return 0
        
        left_depth = 0 # left depth
        right_depth = 0 # right depth
        
        if node_v < cur_node.val: # if node_v in left node
            left_depth = self._get_depth(node_v, cur_node.left)
            
        if node_v > cur_node.val: # if node_v in right node
            right_depth = self._get_depth(node_v, cur_node.right)
            
        return max(left_depth, right_depth) + 1 # maximum between left and right plus the node
    
    def max_path_sum(self, node): #* Only if the node value is number
        max_sum = 0 # maximum sum
        left = 0 # left sum
        right = 0 # right sum
        
        if node.left:
            left = self.max_path_sum(node.left) # left node
            left += node.left.val # left sum
            
        if node.right:
            right = self.max_path_sum(node.right) # right node
            right += node.right.val # right sum
            
        max_sum = max(left, right) # maximum between left and right
        if node == self.root: # just for the root
            max_sum += node.val # maximum sum + root
            
        return max_sum
    
    def insert(self, val): # insert value
        if self._is_empty_tree(): # root is empty
            self.root = BTNode(val)
        return self._insert(val, self.root)
    
    def _insert(self, val, cur_node): # recursive insertion
        if val == cur_node.val: # value found
            print("Value already exists")
            return
            
        if val < cur_node.val: # left node
            if cur_node.left is None: # left node exists
                cur_node.left = BTNode(val)
            else:
                self._insert(val, cur_node.left)
                
        if val > cur_node.val: # right node
            if cur_node.right is None: # right node exists
                cur_node.right = BTNode(val)
            else:
                self._insert(val, cur_node.right)
                
    def remove(self, val): # remove value
        if self._is_empty_tree(): # root is empty
            print("Empty tree")
            return
        if self.search(val): # if value is found in tree
            return self._remove(val, self.root)
        else:
            print("Node not found") # if node is not found
            return
    
    def _remove(self, val, cur_node): # recursive remove
        if cur_node.val == val: # value found
            return self._del_node(cur_node) # delete node 
        
        if val < cur_node.val: # left node
            if cur_node.left: # left node exists
                cur_node.left = self._remove(val, cur_node.left) # assign to current node left
        
        if val > cur_node.val: # right node
            if cur_node.right: # right node exists
                cur_node.right = self._remove(val, cur_node.right) # assign to current node right
                
        return cur_node # return the node
    
    def _del_node(self, node): # deleting the node
        child = 0 # childrens
        if node.left:
            child += 1
        if node.right:
            child += 1
            
        if child == 0: # if there are no children
            if self.root == node: # if root is node
                self.root = None
            else:
                return None
            
        if child == 1: # if there is 1 child
            if self.root == node: # if root is node
                if node.left: # find out if left or right child
                    self.root = node.left
                if node.right:
                    self.root = node.right
            else:
                if node.left:
                    return node.left
                if node.right:
                    return node.right
        
        if child == 2: # if there is 2 children
            min_node = self._find_min(node.right) # find the minimum node in the right subtree
            node.val = min_node.val # assign the min node value to the node value
            node.right = self._remove(min_node.val, node.right) # assign to node.right the remaining right subtree
            return node
        
    def in_order_traversal(self): # in-order traversal
        return self._in_order_traversal(self.root)
                
    def _in_order_traversal(self, node):
        elements = [] 
        
        if node.left: # traverse the left subtree
            elements += self._in_order_traversal(node.left)
            
        elements.append(node.val) # the root
        
        if node.right: # traverse the right subtree
            elements += self._in_order_traversal(node.right)
            
        return elements
    
    def pre_order_traversal(self): # pre-order traversal
        return self._pre_order_traversal(self.root)
    
    def _pre_order_traversal(self, node):
        elements = []
            
        elements.append(node.val) # the root
        
        if node.left: # traverse the left subtree
            elements += self._pre_order_traversal(node.left)
            
        if node.right: # traverse the right subtree
            elements += self._pre_order_traversal(node.right)
            
        return elements
    
    def post_order_traversal(self): # post-order traversal
        return self._post_order_traversal(self.root)
    
    def _post_order_traversal(self, node = None):
        elements = []
        
        if node.left: # traverse the left subtree
            elements += self._post_order_traversal(node.left)
        
        if node.right: # traverse the right subtree
            elements += self._post_order_traversal(node.right)
            
        elements.append(node.val) # the root
            
        return elements
    
    def dfs_traversal(self): # dfs traversal using recursion
        self.stack.push(self.root) # using a stack
        return self._dfs_traversal(self.root)
    
    def _dfs_traversal(self, node): #LIFO
        elements = []
        popped_item = self.stack.pop() # last element from the stack
        elements.append(popped_item.val) # append the popped item
        
        if node.right: # first right node
            self.stack.push(node.right)
            
        if node.left: # second left node
            self.stack.push(node.left)
            
        if not self.stack.is_empty(): # if stack is not empty
            if popped_item.left: # if there is a left node
                elements += self._dfs_traversal(popped_item.left)
            
            if popped_item.right: # if there is a right node
                elements += self._dfs_traversal(popped_item.right)
        
        return elements
    
    def dfs_traversal_loop(self): # dfs traversal using loop
        self.stack.push(self.root) # using a stack
        return self._dfs_traversal_loop()
    
    def _dfs_traversal_loop(self):
        elements = []
            
        while not self.stack.is_empty(): # looping until stack is empty
            popped_item = self.stack.pop() # last element from the stack
            elements.append(popped_item.val) # append the popped item
            
            if popped_item.right: # if there is a left node
                self.stack.push(popped_item.right)
                
            if popped_item.left: # if there is a right node
                self.stack.push(popped_item.left)
                
        return elements
    
    def bfs_traversal(self): # bfs traversal with looping
        self.queue.enqueue(self.root) # using queue
        return self._bfs_traversal()
    
    def _bfs_traversal(self): #FIFO
        elements = []
            
        while not self.queue.is_empty(): # looping until queue is empty
            popped_item = self.queue.dequeue() # dequeuing the first element
            elements.append(popped_item.val) # append the popped item
            
            if popped_item.left and popped_item.right: # if both left and right exists
                self.queue.enqueue(popped_item.left)
                self.queue.enqueue(popped_item.right)
                
            elif popped_item.left: # if only left elements
                self.queue.enqueue(popped_item.left)
            
            elif popped_item.right: # if only right elements
                self.queue.enqueue(popped_item.right)
        
        return elements
      

if __name__ == "__main__":
    bst = BST()
    # elements = [26, 34, 12, 67, 15, 9, 34, 14, 13, 18, 17, 28, 21, 32, 98, 54, 45, 10, 8, 3, 78]
    elements = [26, 34, 12, 67, 15, 9, 28, 32]
    elements = [70, 50, 90, 40, 60, 80, 95, 20, 75, 85, 99]
    for ele in elements:
        bst.insert(ele)
    print("Traversal")
    print(bst.in_order_traversal())
    print(bst.pre_order_traversal())
    print(bst.post_order_traversal())
    print("Min value and max value")
    print(bst.find_min().val)
    print(bst.find_max().val)
    bst.remove(70)
    print("Remove element")
    print(bst.in_order_traversal())
    print("Depth first search")
    print(bst.dfs_traversal())
    print(bst.dfs_traversal_loop())
    print("Height")
    print(bst.get_height())
    print("Depth")
    print(bst.get_depth(80))
    print("Search")
    print(bst.search(82))
    print("Breadth first search")
    print(bst.bfs_traversal())
    print("Max path sum")
    print(bst.max_path_sum(bst.root))
    
    
        
            
            
    