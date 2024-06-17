class Min_Heap:
    def __init__(self):
        self.heap = []  # Initialize an empty heap
        
    def _stifup(self, idx):
        par_idx = (idx -1) // 2  # Calculate the parent index
        if par_idx < 0:
            return
        # If the parent node is greater than the current node, swap them
        if self.heap[par_idx] > self.heap[idx]:
            self.heap[par_idx], self.heap[idx] = self.heap[idx], self.heap[par_idx]
        # Recursively sift up the parent node
        return self._stifup(par_idx)
        
    def _stifdown(self, idx):
        left_idx = (2 * idx) + 1  # Calculate the left child index
        right_idx = (2 * idx) + 2  # Calculate the right child index
        min_idx = None
        
        # If there is no left child, return
        if left_idx >= len(self.heap):
            return
        
        # If there is no right child, the minimum index is the left child index
        if right_idx >= len(self.heap):
            min_idx = left_idx
        else:
            # Otherwise, the minimum index is the index of the smaller child
            if self.heap[left_idx] < self.heap[right_idx]:
                min_idx = left_idx
            else:
                min_idx = right_idx
                
        # If the current node is greater than the minimum child, swap them
        if self.heap[idx] > self.heap[min_idx]:
            self.heap[min_idx], self.heap[idx] = self.heap[idx], self.heap[min_idx]
        # Recursively sift down the minimum child
        return self._stifdown(min_idx)
        
    def insert(self, val):
        self.heap.append(val)  # Insert the value at the end of the heap
        self._stifup(len(self.heap) - 1)  # Sift up the inserted value
        
    def get_min(self):
        return self.heap[0]  # Return the minimum value (root of the heap)
    
    def extract_min(self):
        if len(self.heap) == 0:
            return None
        min_val = self.heap[0]  # Store the minimum value
        self.heap[0] = self.heap[-1]  # Replace the root with the last value in the heap
        self.heap.pop()  # Remove the last value (now at the root)
        self._stifdown(0)  # Sift down the root value
        return min_val  # Return the minimum value
    
    def update_idx(self, val, idx):
        if idx < 0 or idx >= len(self.heap):
            print("Invalid index")
            return
        
        old_val = self.heap[idx]  # Store the old value
        self.heap[idx] = val  # Update the value at the index
        
        # If the new value is less than the old value, sift up; otherwise, sift down
        if val < old_val:
            self._stifup(idx)
        else:
            self._stifdown(idx)
            
    def update_val(self, val, rep_val):
        rep_idx = None
        for i in range(len(self.heap)):
            if self.heap[i] == rep_val:
                rep_idx = i
        self.update_idx(self, val, rep_idx)  # Update the value at the found index
        
    def heapify(self, arr):
        self.heap = arr  # Replace the heap with the new array
        # Sift down all values starting from the end of the heap
        for i in range(len(self.heap) - 1, -1, -1):
            self._stifdown(i)
        return self.heap  # Return the heapified array
    
    def heapsort(self):
        sort_arr = []
        # Extract the minimum value and append it to the sorted array until the heap is empty
        for i in range(len(self.heap)):
            val = self.extract_min()
            sort_arr.append(val)
        return sort_arr  # Return the sorted array
        
        
if __name__ == "__main__":
    # arr = [4, 8,6, 9, 12, 7, 10, 14, 15, 13, 18, 11, 9]
    # arr = [2, 5, 4, 8, 12, 7, 6, 14, 15, 13, 18, 11, 9, 10]
    # arr = [4, 5, 6, 8, 12, 7, 10, 14, 15, 13, 18, 11, 9]
    arr = [9, 11, 18, 13, 15, 14, 7, 8, 12, 10, 4, 6, 3]
    min_heap = Min_Heap()
    min_heap.heapify(arr)
    # for i in arr:
    #     min_heap.insert(i)
    # print(min_heap.heap)
    # # min_heap.insert(5)
    # # print(min_heap.extract_min())
    # min_heap.update_idx(2, 5)
    # min_heap.update_idx(16, 4)
    print(min_heap.heap)
    print(min_heap.heapsort())
    