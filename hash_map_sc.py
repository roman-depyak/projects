# Name:
# OSU Email: @oregonstate.edu
# Course: CS261 - Data Structures
# Assignment: 6 HashMap (Portfolio Assignment)
# Due Date: 8/13/24
# Description: An optimized HashMap class is implemented by using a dynamic
# array to store the hash table and implementing chaining for collision
# resolution by using a singly linked list. Chains of key/value pairs are
# stored in linked list nodes.


from a6_include import (DynamicArray, LinkedList,
                        hash_function_1, hash_function_2)


class HashMap:
    def __init__(self,
                 capacity: int = 11,
                 function: callable = hash_function_1) -> None:
        """
        Initialize new HashMap that uses
        separate chaining for collision resolution
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self._buckets = DynamicArray()

        # capacity must be a prime number
        self._capacity = self._next_prime(capacity)
        for _ in range(self._capacity):
            self._buckets.append(LinkedList())

        self._hash_function = function
        self._size = 0

    def __str__(self) -> str:
        """
        Override string method to provide more readable output
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = ''
        for i in range(self._buckets.length()):
            out += str(i) + ': ' + str(self._buckets[i]) + '\n'
        return out

    def _next_prime(self, capacity: int) -> int:
        """
        Increment from given number and the find the closest prime number
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        if capacity % 2 == 0:
            capacity += 1

        while not self._is_prime(capacity):
            capacity += 2

        return capacity

    @staticmethod
    def _is_prime(capacity: int) -> bool:
        """
        Determine if given integer is a prime number and return boolean
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        if capacity == 2 or capacity == 3:
            return True

        if capacity == 1 or capacity % 2 == 0:
            return False

        factor = 3
        while factor ** 2 <= capacity:
            if capacity % factor == 0:
                return False
            factor += 2

        return True

    def get_size(self) -> int:
        """
        Return size of map
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self._size

    def get_capacity(self) -> int:
        """
        Return capacity of map
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self._capacity

    # ------------------------------------------------------------------ #

    def put(self, key: str, value: object) -> None:
        """
        Updates the key/value pair in the hash map. If the given key already exists in
        the hash map, its associated value is replaced with the new value. If the given
        key is not in the hash map, a new key/value pair is added.
        """

        # if current load factor >= 1.0, table is resized to twice its current capacity
        if self.table_load() >= 1.0:
            self.resize_table(self._capacity * 2)

        # calculates bucket index
        index = self._hash_function(key) % self._capacity
        # get the bucket (linked list) mapped to the calculated index
        bucket = self._buckets[index]
        # see if the key is already in the bucket
        node = bucket.contains(key)

        # if the key is already in the bucket, update its value
        if node:
            node.value = value
        # if key is not in the bucket, add key to bucket & increment size
        else:
            bucket.insert(key, value)
            self._size += 1

    def resize_table(self, new_capacity: int) -> None:
        """
        Changes the capacity of the underlying table. All hash table
        links are rehashed, then all existing key/value pairs
        are put into the new table.
        """

        # if new capacity is less than 1 then this method does nothing
        if new_capacity < 1:
            return

        # makes sure that new capacity is a prime number
        if not self._is_prime(new_capacity):
            # if new capacity isn't a prime number uses next_prime
            # to change new capacity to next higher prime number
            new_capacity = self._next_prime(new_capacity)

        # saves old buckets & capacity before rehashing
        old_buckets = self._buckets
        old_capacity = self._capacity

        # uses the new capacity to makes a new DynamicArray with empty SLLs
        self._capacity = new_capacity
        self._buckets = DynamicArray()
        for index in range(self._capacity):
            self._buckets.append(LinkedList())

        self._size = 0

        # rehashes all the key value pairs from old buckets into new table
        for i in range(old_capacity):
            bucket = old_buckets[i]
            node = bucket._head
            while node:
                self.put(node.key, node.value)
                node = node.next


    def table_load(self) -> float:
        """
        Returns the current hash table load factor.
        """

        return self.get_size() / self.get_capacity()

    def empty_buckets(self) -> int:
        """
        Returns the number of empty buckets in the hash table.
        """

        counter = 0
        # iterates over each bucket & increments counter every time an empty
        # bucket (SLL with length equal to 0) is encountered.
        for i in range(self._buckets.length()):
            if self._buckets[i].length() == 0:
                counter += 1

        return counter

    def get(self, key: str):
        """
        Returns the value associated with the given key.
        If the key is not in the hash map, returns None.
        """

        # calculates the index for the given key
        index = self._hash_function(key) % self._capacity
        # gets the bucket at that index
        bucket = self._buckets[index]
        # checks to see if any of the nodes contain the given key
        node = bucket.contains(key)
        # if a node with the given key exists, return its associated value
        # Otherwise, return None
        return node.value if node else None

    def contains_key(self, key: str) -> bool:
        """
        Returns True if the given key is in the hash map, otherwise returns False.
        """

        # calculates index
        index = self._hash_function(key) % self._capacity
        # gets the bucket at that index
        bucket = self._buckets[index]
        # if the given key is within the bucket returns True
        # otherwise returns False
        return bucket.contains(key) is not None

    def remove(self, key: str) -> None:
        """
        Removes the given key and its associated value from the hash map. If the key
        is not in the hash map, this method does nothing.
        """

        index = self._hash_function(key) % self._capacity
        bucket = self._buckets[index]

        # uses the remove method from the LinkedList class to remove the given key
        # & its associated value from the hash map
        # if the key is successfully removed, then size of the hash map is decremented
        if bucket.remove(key):
            self._size -= 1

    def get_keys_and_values(self) -> DynamicArray:
        """
        Returns a dynamic array where each index contains a tuple of a key/value pair
        stored in the hash map. The order of the keys in the dynamic
        array does not matter.
        """

        # will store a tuple of key/value pairs
        tuple_array = DynamicArray()

        # iterate over all buckets and get all nodes
        for i in range(self._buckets.length()):
            bucket = self._buckets[i]
            node = bucket._head

            # take the key value pair from each node and appends
            # it as a tuple to the tuple array
            while node:
                tuple_array.append((node.key, node.value))
                node = node.next

        return tuple_array

    def clear(self) -> None:
        """
        Clears the contents of the hash map. It does not change the underlying hash
        table capacity.
        """

        # make a new, empty DynamicArray for buckets
        self._buckets = DynamicArray()
        # use current capacity to create new, empty SLLs for each bucket
        # and append them to the bucket
        for i in range(self._capacity):
            self._buckets.append(LinkedList())
        # reset size of the LinkedLists to 0 without changing hash table capacity
        self._size = 0



def find_mode(da: DynamicArray) -> tuple[DynamicArray, int]:
    """
    Standalone function outside the HashMap class that receives a dynamic array.
    Return a tuple containing a dynamic array comprising the most occurring
    value(s) of the given array, and an int representing the highest frequency of
    occurrence for the most occurring value(s). 
    """
    # if you'd like to use a hash map,
    # use this instance of your Separate Chaining HashMap
    map = HashMap()

    # iterates over each element in the da
    for i in range(da.length()):
        # gets value at current index
        value = da[i]
        # gets the current count of the value from hash map
        # if the value isn't found in the hash map gets the value 0
        current_count = map.get(value) or 0
        # updates count for that value in hash map
        map.put(value, current_count + 1)

    # make a new da to store modes
    mode_array = DynamicArray()
    # represents highest frequency in hash map
    max_count = 0

    # get all the key value pairs from hash map
    keys_and_values = map.get_keys_and_values()
    # iterate over all the key value pairs
    for i in range(keys_and_values.length()):
        # get the key and its count from tuple
        key, count = keys_and_values[i]
        # see if current count is greater than max count
        if count > max_count:
            # if curr count > max count, mode array is reset so it only holds current key
            mode_array = DynamicArray()
            mode_array.append(key)
            # update max count to value of current count
            max_count = count
        # if curr count equals max count then current key is added to mode array
        elif count == max_count:
            mode_array.append(key)

    return mode_array, max_count


# ------------------- BASIC TESTING ---------------------------------------- #

if __name__ == "__main__":

    print("\nPDF - put example 1")
    print("-------------------")
    m = HashMap(53, hash_function_1)
    for i in range(150):
        m.put('str' + str(i), i * 100)
        if i % 25 == 24:
            print(m.empty_buckets(), round(m.table_load(), 2), m.get_size(), m.get_capacity())

    print("\nPDF - put example 2")
    print("-------------------")
    m = HashMap(41, hash_function_2)
    for i in range(50):
        m.put('str' + str(i // 3), i * 100)
        if i % 10 == 9:
            print(m.empty_buckets(), round(m.table_load(), 2), m.get_size(), m.get_capacity())

    print("\nPDF - resize example 1")
    print("----------------------")
    m = HashMap(20, hash_function_1)
    m.put('key1', 10)
    print(m.get_size(), m.get_capacity(), m.get('key1'), m.contains_key('key1'))
    m.resize_table(30)
    print(m.get_size(), m.get_capacity(), m.get('key1'), m.contains_key('key1'))

    print("\nPDF - resize example 2")
    print("----------------------")
    m = HashMap(75, hash_function_2)
    keys = [i for i in range(1, 1000, 13)]
    for key in keys:
        m.put(str(key), key * 42)
    print(m.get_size(), m.get_capacity())

    for capacity in range(111, 1000, 117):
        m.resize_table(capacity)

        m.put('some key', 'some value')
        result = m.contains_key('some key')
        m.remove('some key')

        for key in keys:
            # all inserted keys must be present
            result &= m.contains_key(str(key))
            # NOT inserted keys must be absent
            result &= not m.contains_key(str(key + 1))
        print(capacity, result, m.get_size(), m.get_capacity(), round(m.table_load(), 2))

    print("\nPDF - table_load example 1")
    print("--------------------------")
    m = HashMap(101, hash_function_1)
    print(round(m.table_load(), 2))
    m.put('key1', 10)
    print(round(m.table_load(), 2))
    m.put('key2', 20)
    print(round(m.table_load(), 2))
    m.put('key1', 30)
    print(round(m.table_load(), 2))

    print("\nPDF - table_load example 2")
    print("--------------------------")
    m = HashMap(53, hash_function_1)
    for i in range(50):
        m.put('key' + str(i), i * 100)
        if i % 10 == 0:
            print(round(m.table_load(), 2), m.get_size(), m.get_capacity())

    print("\nPDF - empty_buckets example 1")
    print("-----------------------------")
    m = HashMap(101, hash_function_1)
    print(m.empty_buckets(), m.get_size(), m.get_capacity())
    m.put('key1', 10)
    print(m.empty_buckets(), m.get_size(), m.get_capacity())
    m.put('key2', 20)
    print(m.empty_buckets(), m.get_size(), m.get_capacity())
    m.put('key1', 30)
    print(m.empty_buckets(), m.get_size(), m.get_capacity())
    m.put('key4', 40)
    print(m.empty_buckets(), m.get_size(), m.get_capacity())

    print("\nPDF - empty_buckets example 2")
    print("-----------------------------")
    m = HashMap(53, hash_function_1)
    for i in range(150):
        m.put('key' + str(i), i * 100)
        if i % 30 == 0:
            print(m.empty_buckets(), m.get_size(), m.get_capacity())

    print("\nPDF - get example 1")
    print("-------------------")
    m = HashMap(31, hash_function_1)
    print(m.get('key'))
    m.put('key1', 10)
    print(m.get('key1'))

    print("\nPDF - get example 2")
    print("-------------------")
    m = HashMap(151, hash_function_2)
    for i in range(200, 300, 7):
        m.put(str(i), i * 10)
    print(m.get_size(), m.get_capacity())
    for i in range(200, 300, 21):
        print(i, m.get(str(i)), m.get(str(i)) == i * 10)
        print(i + 1, m.get(str(i + 1)), m.get(str(i + 1)) == (i + 1) * 10)

    print("\nPDF - contains_key example 1")
    print("----------------------------")
    m = HashMap(53, hash_function_1)
    print(m.contains_key('key1'))
    m.put('key1', 10)
    m.put('key2', 20)
    m.put('key3', 30)
    print(m.contains_key('key1'))
    print(m.contains_key('key4'))
    print(m.contains_key('key2'))
    print(m.contains_key('key3'))
    m.remove('key3')
    print(m.contains_key('key3'))

    print("\nPDF - contains_key example 2")
    print("----------------------------")
    m = HashMap(79, hash_function_2)
    keys = [i for i in range(1, 1000, 20)]
    for key in keys:
        m.put(str(key), key * 42)
    print(m.get_size(), m.get_capacity())
    result = True
    for key in keys:
        # all inserted keys must be present
        result &= m.contains_key(str(key))
        # NOT inserted keys must be absent
        result &= not m.contains_key(str(key + 1))
    print(result)

    print("\nPDF - remove example 1")
    print("----------------------")
    m = HashMap(53, hash_function_1)
    print(m.get('key1'))
    m.put('key1', 10)
    print(m.get('key1'))
    m.remove('key1')
    print(m.get('key1'))
    m.remove('key4')

    print("\nPDF - get_keys_and_values example 1")
    print("------------------------")
    m = HashMap(11, hash_function_2)
    for i in range(1, 6):
        m.put(str(i), str(i * 10))
    print(m.get_keys_and_values())

    m.put('20', '200')
    m.remove('1')
    m.resize_table(2)
    print(m.get_keys_and_values())

    print("\nPDF - clear example 1")
    print("---------------------")
    m = HashMap(101, hash_function_1)
    print(m.get_size(), m.get_capacity())
    m.put('key1', 10)
    m.put('key2', 20)
    m.put('key1', 30)
    print(m.get_size(), m.get_capacity())
    m.clear()
    print(m.get_size(), m.get_capacity())

    print("\nPDF - clear example 2")
    print("---------------------")
    m = HashMap(53, hash_function_1)
    print(m.get_size(), m.get_capacity())
    m.put('key1', 10)
    print(m.get_size(), m.get_capacity())
    m.put('key2', 20)
    print(m.get_size(), m.get_capacity())
    m.resize_table(100)
    print(m.get_size(), m.get_capacity())
    m.clear()
    print(m.get_size(), m.get_capacity())

    print("\nPDF - find_mode example 1")
    print("-----------------------------")
    da = DynamicArray(["apple", "apple", "grape", "melon", "peach"])
    mode, frequency = find_mode(da)
    print(f"Input: {da}\nMode : {mode}, Frequency: {frequency}")

    print("\nPDF - find_mode example 2")
    print("-----------------------------")
    test_cases = (
        ["Arch", "Manjaro", "Manjaro", "Mint", "Mint", "Mint", "Ubuntu", "Ubuntu", "Ubuntu"],
        ["one", "two", "three", "four", "five"],
        ["2", "4", "2", "6", "8", "4", "1", "3", "4", "5", "7", "3", "3", "2"]
    )

    for case in test_cases:
        da = DynamicArray(case)
        mode, frequency = find_mode(da)
        print(f"Input: {da}\nMode : {mode}, Frequency: {frequency}\n")
