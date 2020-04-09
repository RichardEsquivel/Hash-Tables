# '''
# Linked List hash table key/value pair
# '''


class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''

    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity
        self.length = 0

    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.

        You may replace the Python hash with DJB2 as a stretch goal.
        '''
        #
        return hash(key)

    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash

        OPTIONAL STRETCH: Research and implement DJB2
        '''
        pass

    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash(key) % self.capacity

    def insert(self, key, value):
        '''
        Store the value with the given key.

        # Part 1: Hash collisions should be handled with an error warning. (Think about and
        # investigate the impact this will have on the tests)

        # Part 2: Change this so that hash collisions are handled with Linked List Chaining.

        Fill this in.
        '''
     # Check if node exists or doesn't and, if key exists replace that value and if it doesn't exist we're attaching a new node to that linked list

        index = self._hash_mod(key)
        curr_node = self.storage[index]

        if not curr_node:
            self.storage[index] = LinkedPair(key, value)
            self.length += 1
            if self.length > self.capacity * .66:
                self.resize()
            return
        # node has a value assigned to that key reassign the value to update the key
        while curr_node:
            if curr_node == key:
                curr_node.value = value
                break
        # continue on to traverse
            elif curr_node.next:
                curr_node = curr_node.next
        # When you reach None add this new value to the end as a node
            else:
                curr_node.next = LinkedPair(key, value)
                break

        #     print(

        #         f"ERROR: A collision has occurred and a value exists at {index}")
        #     return
        # # if no value exists assign the key and value to that index
        # else:
        #     self.storage[index] = (key, value)
        #     return

    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.
        '''
        # use same determination of index by passing in the key
        index = self._hash_mod(key)
        curr_node = self.storage[index]
        prev_node = None

        # iterate through the node list looking for the one matching your key
        while curr_node:
            # if key matches and there is a previous node make reference to next node skip the current node that matches and have pointer point to node.next
            if curr_node.key == key:
                prev_node.next = curr_node.next
                return None
            else:
                (f"ERROR: Given key of {key} was not found")
            # Traverse the linked list when current node does not match key.
            if curr_node.key != key:
                # Before we reach the end of the list continue to traverse
                while curr_node.next is not None:
                    prev_node = curr_node
                    curr_node = curr_node.next

    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''
        index = self._hash_mod(key)
        curr_node = self.storage[index]
        # Traverse the list and if key passed in matches return the value for that key
        while curr_node:
            if curr_node.key == key:
                return curr_node.value
            # While key does not match continue to traverse if you reach the end of the list
            # You have not found the key and will return None
            return None

    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        # Assign variable for what will be old storage area of values in hashtable
        old_buckets = self.storage
        # Increase capacity by 2
        self.capacity *= 2
        # resize to new capacity self.storage
        self.storage = [None] * self.capacity
        # Initialize item pointer to be utilized during the rehash
        moved_item = None
        # traverse through previosly hashed items and rehash as you place them into new storage
        for item in old_buckets:
            moved_item = item
            while moved_item:
                # call in insert in order to rehash key values
                self.insert(moved_item.key, moved_item.value)
                moved_item = moved_item.next


if __name__ == "__main__":
    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    print("")
