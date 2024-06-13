# Dictionaries key is the reference to the index of the value in an array

#Hash function
#Finding the ascii value of the one letter of the key and then adding
#all the ascii values and dividing it by 10 get the remainder that is the index

#Look up O(1), inserting deletion O(1)
        
        
# *Handling collisions (chaining)
class HashTable:
    
    def __init__(self):
        self.Max = 10
        self.arr = [[] for i in range(self.Max)]
        
    def get_hash(self, key):
        h = 0
        for char in key:
            h += ord(char)
        return h % self.Max
    
    def __setitem__(self, key, value): # def insert(self, key, value):
        index = self.get_hash(key)
        found = False
        for idx, element in enumerate(self.arr[index]):
            if len(element) == 2 and element[0] == key:
                self.arr[index][idx] = (key, value)
                found = True
                break
        if not found:
            self.arr[index].append((key, value))
        
    def __getitem__(self, key): # def get(self, key):
        index = self.get_hash(key)
        for element in self.arr[index]:
            if element[0] == key:
                return element[1]
    
    def __delitem__(self, key):
        index = self.get_hash(key)
        for idx, element in enumerate(self.arr[index]):
            if element[0] == key:
                del self.arr[index][idx]

#? Linear and quadratic probing
class HashTable:
    
    def __init__(self, size):
        self.size = size #max size
        self.arr = [None for i in range(self.size)] #array
        
    def arr_size_i(self):
        self.size *= 2 # increase the size
        temp_arr = [None for i in range(self.size)] # new arr
        for ind in range(len(self.arr)): #putting previous data on the new arr
            temp_arr[ind] = self.arr[ind]
        self.arr = temp_arr
        
    def hash_func(self, key):
        h = 0 
        for letter in key: # getting the ascii value and adding them up
            h += ord(letter)
        
        return h % self.size # remainder returned by moding it with size
        
    def __setitem__(self, key, value):
        hash = self.hash_func(key)
        
        if self.arr[hash]: # if item found
            if self.arr[hash][0] == key: # if key matches
                self.arr[hash][1] = value #change the value
                return 
                
            if None not in self.arr: # every slot is filled
                self.arr_size_i() 
                
            i = 1
            k = 1
            j = 2
            while True:
                # hash = (hash + 1) % self.size #* Linear probing
                hash = (hash + j*i + k*(i**2)) % self.size #* Quadratic probing
                # print(hash)
                    
                if not self.arr[hash]:
                    self.arr[hash] = [key, value]
                    break
                
                i += 1
        else:
            self.arr[hash] = [key, value]
        
        
    def __getitem__(self, key):
        hash = self.hash_func(key)
        
        i = 1
        k = 1
        j = 2
        while True:
            # if self.arr[hash]: #* Linear probing
            #     if self.arr[hash][0] == key:
            #         return self.arr[hash][1]
                
            #     # if i == self.size:
            #     #     return "Item not found"
                
            #     hash = (hash + 1) % self.size 
                
            #     i += 1
        
            # else:
            #     return "Item not found"
            
            if self.arr[hash]: #* Quadratic probing
                if self.arr[hash][0] == key:
                    return self.arr[hash][1]
                
            if i == self.size:
                return "Item not found"
                
            # hash = (hash + i**2) % self.size #?Normal quadratic equation
            hash = (hash + j*i + k*(i**2)) % self.size  #?Better quadratic equation
            i += 1
            
            
#?Double hashing
class HashTable:
    
    def __init__(self, size):
        self.size = size
        self.arr = [None for i in range(size)] # array
        
    def hashk_val(self, key):
        h = 0
        for letter in key:
            h += ord(letter)
            
        return h
    
    def hash_func_1(self, a_key): #*hash func 1
        return a_key % self.size
    
    def hash_func_2(self, a_key): #*hash func 2
        return 3 - (a_key % 3)
    
    def arr_size_i(self):
        self.size += int(self.size * 0.5) # increase the size
        temp_arr = [None for i in range(self.size)] # new arr
        for ind in range(len(self.arr)): #putting previous data on the new arr
            temp_arr[ind] = self.arr[ind]
        self.arr = temp_arr

    def __setitem__(self, key, value):
        attempt = 0
        hash_k = self.hashk_val(key)
        h1 = self.hash_func_1(hash_k)
        h2 = self.hash_func_2(hash_k)
        
        if None not in self.arr: # every slot is filled
            self.arr_size_i()
        
        limit = self.size
        while attempt <= limit:
            double_h_val = (h1 + attempt*h2) % self.size #?Double hashed with quadratic probing
            print(double_h_val)
            if self.arr[double_h_val]:
                if self.arr[double_h_val][0] == key: # if key matches
                    self.arr[double_h_val][1] = value #change the value
                    return 
            else:
                self.arr[double_h_val] = [key, value]
                return
                
            attempt += 1
        
    def __getitem__(self, key):
        attempt = 0
        hash_k = self.hashk_val(key)
        h1 = self.hash_func_1(hash_k)
        h2 = self.hash_func_2(hash_k)
        
        limit = self.size
        while attempt <= limit:
            double_h_val = (h1 + attempt*h2) % self.size #?Double hashed with quadratic probing
            if self.arr[double_h_val]:
                if self.arr[double_h_val][0] == key: # if key matches
                    return self.arr[double_h_val][1]
                
            attempt += 1
            
            
#! Linear probing and Double hashing (New)
class HashTable:
    def __init__(self):
        self.max = 10
        self.ky = [None] * self.max
        self.val = [None] * self.max
        
    def hash_func(self, key):
        h = 0
        for letter in key:
            h += ord(letter)
            
        # return h % self.max #* Linear and quadratic probing #Division method
        return h #* Double hashing
    
    def hash_1(self, key, table_size): #*Folding method #Predictable algorithm
        key_str = str(key)
        chunk_size = len(key_str) // 2
        hash_value = 0

        for i in range(0, len(key_str), chunk_size):
            chunk = key_str[i:i + chunk_size]
            chunk_value = int(chunk)
            hash_value += chunk_value

        hash_value %= table_size
        return hash_value
    
    def hash_2(self, key, table_size): #* Mid_square_hash method #Unpredictable algorithm
        key_square = key * key
        key_str = str(key_square)
        mid_digits = len(key_str) // 2 - 1
        hash_value_str = key_str[mid_digits:mid_digits + ((len(key_str) // 2) // 2)]
        rand_val = 0
        if hash_value_str[-1] == "0": #Second hash should never return zero
            rand_val = 1
        hash_value = (int(hash_value_str) + rand_val) % table_size
        return hash_value
    
    def size_inc(self):
        self.max += int(self.max * 0.5)
        new_ky = [None] * self.max
        new_val = [None] * self.max
        
        for i in range(len(self.ky)):
            new_ky[i] = self.ky[i]
            new_val[i] = self.val[i]
            
        self.ky = new_ky
        self.val = new_val
        
    def is_empty(self):
        return all(ele is None for ele in self.ky)
    
    def is_full(self):
        return None not in self.ky
    
    def __setitem__(self, key, value): #* Double hashing
        if self.is_full():
            self.size_inc()
            
        if key in self.ky:
            ind = self.ky.index(key)
            self.val[ind] = value
            return
            
        h_key = self.hash_func(key)
        h1 = self.hash_1(h_key, self.max)
        
        if self.ky[h1]:
            while self.ky[h1] is not None:
                h2 = self.hash_2(h_key, self.max)
                h1 = (h1 + h2) % self.max
                h_key += 1
            self.ky[h1] = key
            self.val[h1] = value
            
        else:
            self.ky[h1] = key
            self.val[h1] = value
            
    def __getitem__(self, key): #* Double hashing
        if self.is_empty():
            print("Empty hash table")
            return
        
        if key in self.ky:
            h_key = self.hash_func(key)
            h1 = self.hash_1(h_key, self.max)
            
            if key == self.ky[h1]:
                return self.val[h1]
            
            while self.ky[h1] != key:
                h2 = self.hash_2(h_key, self.max)
                h1 = (h1 + h2) % self.max
                h_key += 1
                
            return self.val[h1]
        else:
            print("Item does not exist in hash table")
            return
        
    def __delitem__(self, key): #* Double hashing
        if self.is_empty():
            print("Empty hash table")
            return
        
        if key in self.ky:
            h_key = self.hash_func(key)
            h1 = self.hash_1(h_key, self.max)
            
            if key == self.ky[h1]:
                self.ky[h1] = None
                self.val[h1] = None
                
            while self.ky[h1] != key:
                h2 = self.hash_2(h_key, self.max)
                h1 = (h1 + h2) % self.max
                h_key += 1
                
            self.ky[h1] = None
            self.val[h1] = None
        else:
            print("Item does not exist in hash table")	
            return   
        
    # def __setitem__(self, key, value): #* Probings
    #      if self.is_full():
    #           self.size_inc()
            
    #      h = self.hash_func(key)
    #      if self.ky[h]:
    #           if key in self.ky:
    #                ind = self.ky.index(key)
    #                self.val[ind] = value
    #                return
            
    #           i = 1
    #           j = 2
    #           while True:
    #                if h == len(self.ky) - 1:
    #                     h = -1
                        
    #                # h += 1 #* Linear probing
    #                # h = (h + i**2) % self.max #*Quadratic probing
    #                h = (h + i**j) % self.max #* Better Quadratic probing
    #                if self.ky[h] == None:
    #                     self.ky[h] = key
    #                     self.val[h] = value
    #                     return
    #                i += 1
    #                j += 1
                
    #      else:
    #           self.ky[h] = key
    #           self.val[h] = value
            
    # def __delitem__(self, key): #* Probings
    #      if self.is_empty():
    #           print("Empty hash table")
    #           return
        
    #      if key in self.ky:
    #           h = self.hash_func(key)
    #           i = 1
    #           j = 2
    #           while True:
    #                if self.ky[h] == key:
    #                     self.ky[h] = None
    #                     self.val[h] = None
    #                     return
                
    #                if h == len(self.ky) - 1:
    #                     h = -1
                
    #                # h += 1 #* Linear probing
    #                # h = (h + i**2) % self.max #* Quadratic probing
    #                h = (h + i**j) % self.max #* Better Quadratic probing
    #                i += 1
    #                j += 1
    #      else:
    #           print("Item does not exist")
    #           return
        
    # def __getitem__(self, key):#* Probings
    #      if self.is_empty():
    #           print("Empty hash table")
    #           return
        
    #      if key in self.ky:
    #           h = self.hash_func(key)
    #           i = 1
    #           j = 2
    #           while True:
    #                if self.ky[h] == key:
    #                     return self.val[h]
                
    #                if h == len(self.ky) - 1:
    #                     h = -1
                
    #                # h += 1 #* Linear probing
    #                # h = (h + i**2) % self.max #* Qudratic probing
    #                h = (h + i**j) % self.max #* Better Quadratic probing
    #                i += 1
    #                j += 1
    #      else:
    #           print("Key does not exist")
    #           return
        
        
    def printht(self):
        print(self.ky)
        print(self.val) 
    
if __name__ == '__main__':
    HT = HashTable(10)
    # HT["grapes"] = 10000
    HT["grapes"] = 2000
    HT["mango"] = 234
    HT["apple"] = 345
    HT["lychee"] = 908
    HT["orange"] = 834
    HT["blueberry"] = 3789
    HT["raspberry"] = 50000
    HT["jackfruit"] = 621
    HT["biscuit"] = 9000
    HT["chips"] = 89034
    HT["soda"] = 2345
    HT["banana"] = 9345
    # HT.set("grapes", 10000)
    # HT.set("grapes", 2000)
    # HT.set("banana", 234)
    # HT.set("apple", 345)
    # HT.set("mango", 908)
    # HT.set("jackfruit", 3786)
    print(HT.arr)
    print(HT["chips"])
    print(HT["something"])