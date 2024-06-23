class BSTNode:  #* Binary Tree Node
    def __init__(self, val):
        self.val = val # value
        self.left = None # left node
        self.right = None # right node

class GraphNode: #* Graph Tree Node
    def __init__(self, start = None):
        self.start = start # start node
        self.routes = [] # routes contains (destination, distance)
        
class Graph: #* Graph Tree
    def __init__(self):
        self.root = None #Binary tree root
        
    def _emptyTree(self): # if tree is empty
        return self.root == None
        
    def _find_gnode(self, node_v, f_type): #? Find the graph node
        if self._emptyTree():
            if f_type == "create": # if creation is necessary
                g_node = GraphNode(node_v)
                self.root = BSTNode(g_node)
                return g_node
            if f_type == "find" or f_type == "delete": # empty tree cannot be found or deleted
                return
        
        if self.root.val.start == node_v: #if root is value
            return self.root.val
        return self._rec_find_gnode(node_v, self.root, f_type) # recursive call
    
    def _rec_find_gnode(self, node_v, cur_node, f_type): #? Recursive finding
        if node_v == cur_node.val.start: # if value is found
            if f_type == "delete": # return the binary node
                return cur_node
            return cur_node.val # return the graph node
        
        if node_v < cur_node.val.start: # if less than cur_node
            if cur_node.left:
                return self._rec_find_gnode(node_v, cur_node.left, f_type)
        
        if node_v > cur_node.val.start: # if greater than cur_node
            if cur_node.right:
                return self._rec_find_gnode(node_v, cur_node.right, f_type)
            
        if f_type == "create": # for creating nodes
            return self._insert_node(node_v, cur_node)
        if f_type == "find" or f_type == "delete": # if not found return False
            return False
        
    def _min_node(self, node): #? Minimum Node
        if node.left:
            return self._min_node(node.left)
        return node
    
    def _insert_node(self, node_v, cur_node): #? Recursive insertion Bin Node
        if node_v < cur_node.val.start: # for left node
            g_node = GraphNode(node_v)
            cur_node.left = BSTNode(g_node)
            return g_node
        
        if node_v > cur_node.val.start: # for right node
            g_node = GraphNode(node_v)
            cur_node.right = BSTNode(g_node)
            return g_node
    
    def insert_path(self, start, end, dis): #? Inserting path
        p_start = self._find_gnode(start, "create") # Starting Node
        p_end = self._find_gnode(end, "create") # Ending Node
        p_start.routes.append((p_end, dis)) # Append end node to routes of start node
        
    def _delete_node(self, node, parent): # for deleting a node from the Binary tree
        child = 0 # childrens
        if node.left:
            child += 1
        if node.right:
            child += 1
            
        if child == 0: # if no children
            if parent == None: # for root
                self.root = None
            elif parent.left == node: # for left side of parent node
                parent.left = None
            elif parent.right == node: # for right side of parent node
                parent.right = None
                
        if child == 1: # if 1 child
            if parent == None: # for root
                if node.left: # if node has a left child
                    self.root = node.left
                if node.right: # if node has a right child
                    self.root = node.right
            else:
                if parent.left == node: # for left side of parent node
                    if node.left: # if node has a left child
                        parent.left = node.left
                    if node.right == node: # if node has a right child
                        parent.left = node.right
                if parent.right == node: # for right side of parent node
                    if node.left: # if node has a left child
                        parent.right = node.left
                    if node.right == node: # if node has a right child
                        parent.right = node.right
                        
        if child == 2: # for 2 child nodes
            min_v = self._min_node(node.right) # find the min node
            node.val.start = min_v.val.start # node start is min start
            node.val.routes = min_v.val.routes # node routes are min routes
            self._delete_node(min_v, node) # delete the min node
            return
    
    def _delete_path(self, path, cur_node): # deleting a path recursively
        if cur_node == None: # if node is none
            return
        
        for child in cur_node.val.routes: # check for path in the routes of the cur_node
            if child[0].start == path:
                cur_node.val.routes.remove(child) # delete the path
        
        val1 = None
        val2 = None
                
        if cur_node.left: # if there is a left node
            val1 = self._delete_path(path, cur_node.left)
        if cur_node.right: # if there is a right node
            val2 = self._delete_path(path, cur_node.right)
        # if val1 or val2 returns the parent of deleted node
        if val1: 
            return val1
        if val2:
            return val2
        
        if cur_node.left: # if there is a left node
            if path == cur_node.left.val.start: # if parent found
                return cur_node
        if cur_node.right: # if there is a right node
            if path == cur_node.right.val.start: # if parent found
                return cur_node
        
    def delete_path(self, path): # delete the path
        del_node = self._find_gnode(path, "delete") # searching for the node
        if del_node: # if node found
            parent = self._delete_path(path, self.root) # find the parent
            return self._delete_node(del_node, parent) # pass the parent and the node
        else: # if node not found
            print("Node not found")
            return 
        
    def get_all_paths(self, start, end): # for getting all the paths
        p_start = self._find_gnode(start, "find") # find the start path
        if not p_start: # if start node is not found
            print("Start node not found")
            return
        return self._get_all_paths(p_start, end, 0)
    
    def _get_all_paths(self, p_start, end, dis, path = []): # getting all paths recursively
        path = path + [p_start.start] # the traversed paths
        
        if p_start.start == end: # if end node is found
            return [(path, dis)]
        
        if p_start.routes == []: # if end of a route is reached
            return []
        
        paths = []
        
        for route, r_dis in p_start.routes: # loop through all routes
            if route.start not in path: # if route is not on the path
                new_path = self._get_all_paths(route, end, dis + r_dis, path) # find the path recursively
                for p in new_path: # if a path is found
                    paths.append(p)
                
        return paths # return all the paths
    
    def get_shortest_path(self, start, end): # for getting shortest path
        p_start = self._find_gnode(start, "find") # find the starting path
        if not p_start: # if start path not found
            print("Start node not found")
            return
        return self._get_shortest_path(p_start, end, 0)
    
    def _get_shortest_path(self, p_start, end, dis, path = []): # for getting shortest path recursively
        path = path + [p_start.start] # traversed paths
        
        if p_start.start == end: # if end path found
            return (path, dis)
        
        if p_start.routes == []: # if routes have reached the end
            return []
        
        sp = None # shortest path
        
        for route, r_dis in p_start.routes: # loop through routes
            if route.start not in path: # if route not in path
                new_path = self._get_shortest_path(route, end, dis + r_dis, path) # get shortest path recursively
                if sp is None: # if there is no shortest path
                    sp = new_path
                if sp[0][-1] == end: # if shortest path exists
                    if new_path[1] < sp[1]: # check for smaller distance
                        sp = new_path
                
        return sp # return shortest path
        
if __name__ == '__main__':
    roots = [
        ("Mumbai", "Paris", 8000),
        ("Mumbai", "Dubai", 3000),
        ("Mumbai", "Boston", 12000),
        ("Boston", "Hartford", 500),
        ("Hartford", "New York", 1000),
        ("Paris", "Dubai", 3000),
        ("Paris", "New York", 5000),
        ("Dubai", "New York", 7500),
        ("New York", "Toronto", 2000),  
    ]
    
    graph = Graph()
    for i in roots:
        graph.insert_path(i[0], i[1], i[2])
        
    # print(graph.insert_path(roots[0][0], roots[0][1], roots[0][2]))
    print(graph.get_all_paths("Mumbai", "Toronto"))
    print(graph.get_shortest_path("Mumbai", "Toronto"))
    graph.delete_path("Paris")
    # print(graph.get_all_paths("Mumbai", "Toronto"))
    print("hello")
        
        
    