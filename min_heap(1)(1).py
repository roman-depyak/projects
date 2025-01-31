# Name:
# OSU Email: @oregonstate.edu
# Course: CS261 - Data Structures
# Assignment: 5 MinHeap Implementation
# Due Date: 8/5/24
# Description: The MinHeap class is implemented by using a DynamicArray
# as the underlying data structure. The implementation includes the following
# methods: add(), is_empty(), get_min(), remove_min(), build_heap(), size(),
# clear(), and heapsort().


from dynamic_array import *


class MinHeapException(Exception):
    """
    Custom exception to be used by MinHeap class
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    pass


class MinHeap:
    def __init__(self, start_heap=None):
        """
        Initialize a new MinHeap
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self._heap = DynamicArray()

        # populate MinHeap with initial values (if provided)
        # before using this feature, implement add() method
        if start_heap:
            for node in start_heap:
                self.add(node)

    def __str__(self) -> str:
        """
        Return MinHeap content in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        heap_data = [self._heap[i] for i in range(self._heap.length())]
        return "HEAP " + str(heap_data)

    def add(self, node: object) -> None:
        """
        Adds a new object to the MinHeap while maintaining heap property.
        """

        self._heap.append(node)
        # uses helper method to maintain heap property by percolating new
        # node up when new node is appended to Dynamic Array
        self.percolate_up(self._heap.length() - 1)

    def percolate_up(self, index: int) -> None:
        """
        Helper method to maintain the MinHeap's heap property by percolating
        elements up when a new object is added .
        """

        # index of current node's parent
        parent_index = (index - 1) // 2

        # keeps percolating element up while the current node isn't the root and
        # current node's value is less than its parent's value
        while index > 0 and self._heap[index] < self._heap[parent_index]:
            # swaps the current node with its parent
            self._heap[index], self._heap[parent_index] = self._heap[parent_index], self._heap[index]
            # updates current node's index to be parent's index
            # used to see if element needs to be percolated up again
            index = parent_index
            # calculates and assigns parent node's index after swapping
            parent_index = (index - 1) // 2

    def is_empty(self) -> bool:
        """
        Returns True if the heap is empty; otherwise, returns False.
        """

        if self._heap.length() == 0:
            return True

        return False

    def get_min(self) -> object:
        """
        Returns an object with the minimum key, without removing it from the heap.
        If the heap is empty, raises a MinHeapException.
        """

        # if heap is empty raise exception
        if self._heap.length() == 0:
            raise MinHeapException

        # else return object with min key, which is the first element of the array
        return self._heap[0]

    def remove_min(self) -> object:
        """
        Returns an object with the minimum key, and removes it from the heap.
        If the heap is empty, raises a MinHeapException.
        """

        if self._heap.length() == 0:
            raise MinHeapException

        # remembers the val of first element (min value) of the array
        min_val = self._heap[0]
        last_val = self._heap[self._heap.length() - 1]
        # replace val of first element with val of last element
        if self._heap.length() > 1:
            self._heap[0] = last_val

        # removes last element
        self._heap.remove_at_index(self._heap.length() - 1)
        # maintains / restores heap property by percolating down from root node
        if not self.is_empty():
            _percolate_down(self._heap, 0)

        return min_val

    def build_heap(self, da: DynamicArray) -> None:
        """
        Receives a DynamicArray with objects in any order, and builds a proper
        MinHeap from them. The current content of the MinHeap is overwritten.
        """

        self._heap = DynamicArray()

        # adds elements from input Dynamic Array into heap
        for index in range(da.length()):
            self._heap.append(da[index])

        # heapifies all non-leaf nodes
        # starts at last internal node and heapifies up to the root
        index = self._heap.length() // 2 - 1
        while index >= 0:
            _percolate_down(self._heap, index)
            index -= 1

    def size(self) -> int:
        """
        Returns the number of items currently stored in the heap.
        """

        return self._heap.length()

    def clear(self) -> None:
        """
        Clears the contents of the heap.
        """

        self._heap = DynamicArray()

def heapsort(da: DynamicArray) -> None:
    """
    Receives a DynamicArray and sorts its content in non-ascending order,
    using the Heapsort algorithm. The array is sorted in place without
    creating any data structures.
    """

    def heapify(start: int, end: int) -> None:
        """
        Helper method to maintain the MaxHeap property when
        sorting a DynamicArray into non-ascending order.
        """

        # largest represents the index of the greatest value of current node and
        # its two children
        # start and end are the starting and ending indices that the heapify
        # method acts upon
        largest = start
        # repeat below steps until the heap's heap property is restored
        while True:
            # represents left child
            left = 2 * largest + 1
            # represents right child
            right = 2 * largest + 2
            # start off by assuming greatest val is at parent node
            new_largest = largest

            # check if left child is present & is greater than current largest val
            if left < end and da[left] > da[new_largest]:
                # if val of left child > current largest val, left child becomes largest val
                new_largest = left

            # check if right child is present & is greater than current largest val
            if right < end and da[right] > da[new_largest]:
                # if right child val > current largest val, right child becomes largest val
                new_largest = right

            # If neither child was > than the parent, MaxHeap property is satisfied & we
            # can end the loop
            if new_largest == largest:
                break

            # Swaps current root with largest child
            da[largest], da[new_largest] = da[new_largest], da[largest]
            # updates index of current root to largest child's index
            largest = new_largest

    # Number of elements in Dynamic Array
    num_elements = da.length()

    # uses elements from Dynamic Array to build MaxHeap
    for i in range(num_elements // 2 - 1, -1, -1):
        heapify(i, num_elements)

    # Takes elements from heap & adds them to end of array
    for i in range(num_elements - 1, 0, -1):
        # Swaps the largest element with last element in array
        da[0], da[i] = da[i], da[0]
        # Maintains / restores MaxHeap property
        heapify(0, i)

    # Reverse array so it'll be in descending order
    left = 0
    right = num_elements - 1
    while left < right:
        da[left], da[right] = da[right], da[left]
        left += 1
        right -= 1

# It's highly recommended that you implement the following optional          #
# helper function for percolating elements down the MinHeap. You can call    #
# this from inside the MinHeap class. You may edit the function definition.  #

def _percolate_down(da: DynamicArray, parent: int) -> None:
    """
    Helper method to maintain the MinHeap's heap property by percolating
    elements down.
    """

    length = da.length()
    left_child = 2 * parent + 1

    # keep percolating down while current node has a child
    while left_child < length:
        right_child = left_child + 1
        # start off by assuming left child is smallest value
        smallest = left_child

        # see if there's a right child & if it's smaller than left
        if right_child < length and da[right_child] < da[left_child]:
            smallest = right_child

        # if parent <= child then Heap property is restored & loop should be exited
        if da[parent] <= da[smallest]:
            break

        # swaps parent with its smallest child
        da[parent], da[smallest] = da[smallest], da[parent]
        # parent index moved to smallest child's index
        parent = smallest
        # calculates & assigns left child's index for new parent
        left_child = 2 * parent + 1

# ------------------- BASIC TESTING -----------------------------------------


if __name__ == '__main__':

    print("\nPDF - add example 1")
    print("-------------------")
    h = MinHeap()
    print(h, h.is_empty())
    for value in range(300, 200, -15):
        h.add(value)
        print(h)

    print("\nPDF - add example 2")
    print("-------------------")
    h = MinHeap(['fish', 'bird'])
    print(h)
    for value in ['monkey', 'zebra', 'elephant', 'horse', 'bear']:
        h.add(value)
        print(h)

    print("\nPDF - is_empty example 1")
    print("-------------------")
    h = MinHeap([2, 4, 12, 56, 8, 34, 67])
    print(h.is_empty())

    print("\nPDF - is_empty example 2")
    print("-------------------")
    h = MinHeap()
    print(h.is_empty())

    print("\nPDF - get_min example 1")
    print("-----------------------")
    h = MinHeap(['fish', 'bird'])
    print(h)
    print(h.get_min(), h.get_min())

    print("\nPDF - remove_min example 1")
    print("--------------------------")
    h = MinHeap([1, 10, 2, 9, 3, 8, 4, 7, 5, 6])
    while not h.is_empty() and h.is_empty() is not None:
        print(h, end=' ')
        print(h.remove_min())

    print("\nPDF - build_heap example 1")
    print("--------------------------")
    da = DynamicArray([100, 20, 6, 200, 90, 150, 300])
    h = MinHeap(['zebra', 'apple'])
    print(h)
    h.build_heap(da)
    print(h)

    print("--------------------------")
    print("Inserting 500 into input DA:")
    da[0] = 500
    print(da)

    print("Your MinHeap:")
    print(h)
    if h.get_min() == 500:
        print("Error: input array and heap's underlying DA reference same object in memory")

    print("\nPDF - size example 1")
    print("--------------------")
    h = MinHeap([100, 20, 6, 200, 90, 150, 300])
    print(h.size())

    print("\nPDF - size example 2")
    print("--------------------")
    h = MinHeap([])
    print(h.size())

    print("\nPDF - clear example 1")
    print("---------------------")
    h = MinHeap(['monkey', 'zebra', 'elephant', 'horse', 'bear'])
    print(h)
    print(h.clear())
    print(h)

    print("\nPDF - heapsort example 1")
    print("------------------------")
    da = DynamicArray([100, 20, 6, 200, 90, 150, 300])
    print(f"Before: {da}")
    heapsort(da)
    print(f"After:  {da}")

    print("\nPDF - heapsort example 2")
    print("------------------------")
    da = DynamicArray(['monkey', 'zebra', 'elephant', 'horse', 'bear'])
    print(f"Before: {da}")
    heapsort(da)
    print(f"After:  {da}")
