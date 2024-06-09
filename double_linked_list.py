class Node:
    """
    A class representing a node in a double-linked list.

    Each node contains a value and maintains references to the previous and next nodes.

    Attributes:
        value: The value stored in the node.
        prev_node: The previous node in the list.
        next_node: The next node in the list.
    """

    def __init__(self, data=None, next=None, prev=None):
        """
        Initializes a new instance of the Node class.

        Args:
            value: The value to be stored in the node.
        """
        
        self.data = data
        self.next = next
        self.prev = prev

    def __repr__(self) -> str:
        return f"Obj: {self.data}, Prev_obj: {self.next}, Next_obj: {self.next}"


class DoubleLinkedLst:

    """Double Linked list, links each node to it's previous and next node
    Contains a head and a tail, representing the start and end of the list

    Methods:
    1) node_create(data, obj, after=False) -> Creates a nodes and sets the previous and next nodes
        Updates the node of other items as insert methods demand.
    2) insert_at_start(data) -> Inserts a node at the head of the list. 
        Updates the head of the list.
    3) insert_at_end() -> Inserts a node at the tail of the list. 
        Updates the tail of the list.
    4) insert_at(data, index) -> Insets a node a certain index. Uses node_create method
    5) insert_before_value(data_before, data) -> Inserts a node before the obj. Uses node_create method
    6) insert_after_value(data_after, data) -> Inserts a node after the obj. Uses node_create method
    7) node_remove(obj) -> Removes a nodes and sets the previous and next nodes
        Updates the node of other items as remove methods demand
    8) remove_at_start() -> Removes the head of the list. 
        Updates the head of the list
    9) remove_at_end() -> Removes the tail of the list. 
        Updates the tail of the list
    10) remove_at(index) -> Removes a node a certain index. Uses node_remove method
    11) remove_value(data) -> Removes a data by traversing the list. Uses node_remove method
    12) get_length() -> Traverses through the list and finds the length
    13) print_lst(rev=False) -> Prints a list in ascending or descending order
    """

    def __init__(self, head=None, tail=None):
        """
        Initializes a new instance of the DoubleLinkedList class.

        This constructor creates an empty list by setting the head and tail references to None.
        """
        
        self.head = head
        self.tail = tail

    def node_create(self, node_data, obj, after=False):
        """node_create(data, obj, after=False) -> Creates a nodes and sets the previous and next nodes
        Updates the node of other items as insert methods demand.

        Args:
            node_data (_datatypes_): New data to create a new node\n
            obj (_obj_): Object to connect the new node\n
            after (bool): (True for after insertion, False for before insertion). Defaults to False.
        """
        if obj.next == None:  # if the obj is the tail
            self.insert_at_end(node_data)
        elif obj.prev == None:  # if the obj is the head
            self.insert_at_start(node_data)
        else:
            if not after:  # if the insertion is before the object
                node = Node(node_data, obj, obj.prev)  # creating the node
                obj.prev.next = node  # changing the next of the previous object to this node
                obj.prev = node  # changing the prev of this obj to the node
            else:  # if the insertion is after the object
                node = Node(node_data, obj.next, obj)
                obj.next.prev = node  # changing the prev of the next object to this node
                obj.next = node  # changing the next of this obj to the node
        return

    def insert_at_start(self, data):
        """insert_at_start(data) -> Inserts a node at the head of the list. 
        Updates the head of the list.

        Args:
            data (_datatypes_): New data to create a new node

        Time complexity: O(1) as inserting at the head is constant time
        """
        node = Node(data, self.head)
        if self.head == None:  # creating the list if it's empty
            self.head = node  # head and tail both are the same node for one item
            self.tail = node
            return
        self.head.prev = node  # setting the prev of head to the node
        self.head = node  # setting the new node as the new head

    def insert_at_end(self, data):
        """insert_at_end() -> Inserts a node at the tail of the list. 
        Updates the tail of the list.

        Args:
            data (_datatypes_): New data to create a new node

        Time complexity: O(1) as inserting at the tail is constant time
        """
        node = Node(data)
        if self.head == None:  # creating the list if it's empty
            self.head = node
            self.tail = node
            return

        self.tail.next = node  # setting the node as the tail object's next
        node.prev = self.tail  # connecting the node with the tail
        self.tail = node  # updating the node to current tail

    def insert_at(self, index, data):
        """insert_at(data, index) -> Insets a node a certain index. Uses node_create method

        Args:
            index (_int_): Insertion index\n
            data (_datatypes_): New data to create a new node

        Raises:
            ValueError: Index not an integer if index type is not int
            Exception: Index out of range if index is < 0 or > length of the list

        Time complexity: O(n) as we divide the list then compare it with index and 
        choose to start either from tail or head but twice faster than normal method
        """
        length = self.get_length()
        if type(index) != int:
            raise ValueError("Index is not an integer")

        if index < 0 or index > length:
            raise Exception("Index out of range")

        if index == 0:  # first item
            self.insert_at_start(data)
            return
        elif index == length:  # after last item
            self.insert_at_end(data)
            return

        pos = length // 2  # dividing the list to two parts
        if index <= pos:  # if index less than pos we take the head else the tail
            count = 0  # index
            itr = self.head
            while itr:  # untill we reach the last object
                if count == index:
                    # create the node at that index
                    self.node_create(data, itr)
                    return
                itr = itr.next  # iterate to the next obj
                count += 1
        else:
            count = length - 1  # last index
            itr = self.tail
            while itr:
                if count == index:
                    self.node_create(data, itr)
                    return
                itr = itr.prev
                count -= 1

    def insert_before_value(self, data_before, data):
        """insert_before_value(data_before, data) -> Inserts a node before the obj. Uses node_create method

        Args:
            data_before (_obj_): The obj before the data will be inserted\n
            data (_datatypes_): New data to create a new node

        Raises:
            Exception: Raise data not in list, if obj not in list

        Time complexity: O(n) as we have to iterate over the list one by one to find the data_after
        """
        itr = self.head
        while itr:
            if itr.data == data_before:  # data matches with the obj.data of the list
                self.node_create(data, itr)
                return
            itr = itr.next
        else:  # if data doesn't exist
            raise Exception("Data not in the list")

    def insert_after_value(self, data_after, data):
        """insert_after_value(data_before, data) -> Inserts a node after the obj. Uses node_create method

        Args:
            data_after (_obj_): The obj after the data will be inserted\n
            data (_datatypes_): New data to create a new node

        Raises:
            Exception: Raise data not in list, if obj not in list

        Time complexity: O(n) as we have to iterate over the list one by one to find the data_after
        """
        itr = self.head
        while itr:
            if itr.data == data_after:
                # using after = True as we insert after the object
                self.node_create(data, itr, after=True)
                return
            itr = itr.next
        else:
            raise Exception("Data not in the list")

    def node_remove(self, obj):
        """node_remove(obj) -> Removes a nodes and sets the previous and next nodes.
        Updates the node of other items as remove methods demand

        Args:
            obj (_obj_): the obj to be removed
        """
        if obj.next == None:  # if the obj is the tail
            self.remove_at_end()
        elif obj.prev == None:  # if the obj is the head
            self.remove_at_start()
        else:
            # changing the next of the previous object to the next obj of this node
            obj.prev.next = obj.next
            # changing the prev of the next object to the next obj of this node
            obj.next.prev = obj.prev
        return

    def remove_at_start(self):
        """remove_at_start() -> Removes the head of the list. 
        Updates the head of the list

        Raises:
            Exception: Raise cannot remove from empty list if head == None

        Time complexity: O(1) as we remove the head and it happens in constant time
        """
        if self.head == None:  # cannot remove if list is empty
            raise Exception("Cannot remove from empty list")

        self.head = self.head.next  # setting the next obj as the new head
        self.head.prev = None  # setting the prev of head to none and unlinking the previous head

    def remove_at_end(self):
        """remove_at_end(data) -> Removes the tail of the list. 
        Updates the tail of the list

        Raises:
            Exception: Raise cannot remove from empty list if head == None

        Time complexity: O(1) as we remove the tail and it happens in constant time
        """
        if self.head == None:
            raise Exception("Cannot remove from empty list")

        self.tail = self.tail.prev  # setting new tail as the prev obj of the current tail
        # setting None to the tail's next object unlinking the previous tail
        self.tail.next = None

    def remove_at(self, index):
        """remove_at(index) -> Removes a node a certain index. Uses node_remove method

        Args:
            index (_int_): removal index

        Raises:
            ValueError: Index not an integer if index type is not int
            Exception: Index out of range if index is < 0 or > length of the list

        Time complexity: O(n) as we divide the list then compare it with index and 
        choose to start either from tail or head but twice faster than normal method
        """
        length = self.get_length()
        if type(index) != int:
            raise ValueError("Index is not an integer")

        if index < 0 or index >= length:
            raise Exception("Index out of range")

        if index == 0:
            self.remove_at_start()
            return
        elif index == length - 1:
            self.remove_at_end()
            return

        pos = length // 2  # dividing the list to two parts
        if index <= pos:  # if index less than pos we take the head else the tail
            count = 0  # index
            itr = self.head
            while itr:  # untill we reach the last object
                if count == index:
                    self.node_remove(itr)  # remove the node at that index
                    return
                count += 1
                itr = itr.next  # iterate to next node
        else:
            count = length - 1  # last index
            itr = self.tail
            while itr:
                if count == index:
                    self.node_remove(itr)
                    return
                count -= 1
                itr = itr.prev

    def remove_value(self, data):
        """remove_value(data) -> Removes a data by traversing the list. Uses node_remove method

        Args:
            data (_datatypes_): Data to remove from list

        Raises:
            Exception: Raise data not in list, if obj not in list

        Time complexity: O(n) as we have to iterate over the list one by one to find the value
        """
        itr = self.head
        while itr:
            if itr.data == data:  # if obj.data is equal to the given data
                self.node_remove(itr)  # remove that obj
                return
            itr = itr.next
        else:  # if data not found in the list
            raise Exception("Data not in the list")

    def get_length(self):
        """get_length() -> Traverses through the list and finds the length

        Returns:
            _int_: length of the list

        Time complexity: O(n) as we have to iterate over every obj
        """
        count = 0
        itr = self.head
        while itr:  # iterate over each object and increment
            count += 1
            itr = itr.next
        return count

    def printlst(self, rev=False):
        """print_lst(rev=False) -> Prints a list in ascending or descending order

        Args:
            rev (bool): rev = True is descending, else ascending order. Defaults to False.

        Time complexity: O(n) as we have to iterate over every obj
        """
        main_str = ""
        if not rev:  # ascending order print
            itr = self.head
            while itr:
                main_str += str(itr.data) + "--> "
                itr = itr.next
        else:  # descending order print
            itr = self.tail
            while itr:
                main_str += " <--" + str(itr.data)
                itr = itr.prev
        print(main_str)
        return


if __name__ == "__main__":
    ll = DoubleLinkedLst()
    ll.insert_at_start("banana")
    ll.insert_at_start("apple")
    ll.insert_at_end("orange")
    ll.insert_at_end("mango")
    ll.printlst()
    ll.printlst(rev=True)
    print(ll.get_length())
    ll.insert_at(2, "jackfruit")
    ll.insert_at(4, "grapes")
    # ll.printlst()
    # ll.remove_at_start()
    # ll.remove_at_end()
    ll.printlst()
    ll.remove_at(1)
    ll.remove_at(3)
    ll.printlst()
    ll.remove_value("apple")
    ll.printlst()
    ll.insert_before_value("orange", "apple")
    ll.insert_after_value("grapes", "banana")
    ll.printlst()
