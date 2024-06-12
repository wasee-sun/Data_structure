class Array:
    """
    A class representing a dynamic array.

    Attributes:
        length (int): The current length of the array.
        val (dict): A dictionary that stores the array elements.

    Methods:
        push(item):
            Adds an item to the end of the array.

        pop():
            Removes and returns the last item from the array.

        insert(index, item):
            Inserts an item at the specified index in the array.

        remove(index):
            Removes the item at the specified index from the array.

        get(index):
            Retrieves the item at the specified index from the array.

        __str__():
            Returns a string representation of the array.
    """

    def __init__(self) -> None:
        """
        Initializes a new instance of the Array class.

        This constructor sets the initial length of the array to 0
        and creates an empty dictionary to store the array elements.
        """
        self.length = 0
        self.val = {}

    def push(self, item):
        """
        Adds an item to the end of the array.

        Args:
            item: The item to be added to the array.
        """
        self.val[self.length] = item
        self.length += 1

    def pop(self):
        """
        Removes and returns the last item from the array.

        Returns:
            The last item that was removed from the array.
        """
        self.length -= 1
        last_item = self.val[self.length]
        del self.val[self.length]
        return last_item

    def insert(self, index, item):
        """
        Inserts an item at the specified index in the array.

        Args:
            index: The index at which the item should be inserted.
            item: The item to be inserted into the array.
        """
        self.length += 1
        for i in range(self.length - 1, index, -1):
            self.val[i] = self.val[i - 1]
        self.val[index] = item

    def remove(self, index):
        """
        Removes the item at the specified index from the array.

        Args:
            index: The index of the item to be removed.
        """
        self.length -= 1
        for i in range(index, self.length):
            self.val[i] = self.val[i + 1]
        del self.val[self.length]

    def get(self, index):
        """
        Retrieves the item at the specified index from the array.

        Args:
            index: The index of the item to retrieve.

        Returns:
            The item at the specified index.
        """
        return self.val[index]

    def __str__(self):
        """
        Returns a string representation of the array.

        Returns:
            A string representation of the array.
        """
        return str(self.val)
    
#static vs dynamic array
class StaticArr: #? Static Array where size is determined
    def __init__(self, maxim = 10):
        self.max = maxim
        self.arr = [None] * self.max
        
    def append(self, val): # Insertion through value
        if None not in self.arr: # If array is full
            print("Static array ran out of space")
        else:
            i = 0
            while self.arr[i] is not None: # Looping until we find an empty space
                i += 1
            self.arr[i] = val
            
    def pop(self): # Removing
        if all(ele is None for ele in self.arr): # If all the elements are empty
            print("Static array doesn't contain any elements")
            return
        
        if None not in self.arr: # If array is full
            self.arr[len(self.arr)-1] = None
            return
        
        i = 0
        while self.arr[i] is not None: # Looping untill we find an empty space
            i += 1
        self.arr[i - 1] = None # Removing the last element
        
    def length(self): # length of the array (None not considered)
        if None not in self.arr:
            return len(self.arr)
        
        i = 0
        while self.arr[i] is not None: # Looping untill we find an empty space
            i += 1
        return i
            
    def insert(self, val, index): # Insertion using index
        length = self.length() # Find the length of the array
        if length == len(self.arr):
            print("List is full")
            return
            
        if index < 0 or index >= length: # If index is out of bounds
            print("Index out of range")
            return
        
        temp = self.arr[index] # Keeping the prev value at temp
        self.arr[index] = val
        index += 1
        
        while index <= length: #Unitll the index is less than length
            x_temp = self.arr[index] # temp value
            self.arr[index] = temp # shifting right index
            temp = x_temp
            index += 1
        
    def printstlst(self): # Print the array
        print(self.arr)
        

if __name__ == '__main__':
    arr = Array()
    arr.push("A")
    arr.push("B")
    arr.push("C")
    arr.push("D")
    arr.push("E")
    print(arr)
    arr.pop()
    arr.pop()
    arr.insert(1, "F")
    print(arr)
    arr.remove(2)
    print(arr)
    print(arr.get(2))
    print("----------------------")
    st_arr = StaticArr()
    st_arr.append("A")
    st_arr.append("B")
    st_arr.append("C")
    st_arr.append("D")
    print(st_arr.arr)
    st_arr.pop()
    st_arr.insert("F", 1)
    print(st_arr.arr)
    
    