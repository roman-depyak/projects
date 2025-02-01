# Name: Roman Depyak
# OSU Email: depyakr@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment: 4 BST/AVL Tree Implementation 
# Due Date: 7/29/2024
# Description: The BST class is implemented by using instances of the provided BSTNode
# class and completing the skeleton code below.
# The BST class includes the following methods: add(), remove(), contains(), 
# inorder_traversal(), find_min(), find_max(), is_empty(), and make_empty().


import random
from queue_and_stack import Queue, Stack


class BSTNode:
    """
    Binary Search Tree Node class
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """

    def __init__(self, value: object) -> None:
        """
        Initialize a new BST node
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.value = value   # to store node's data
        self.left = None     # pointer to root of left subtree
        self.right = None    # pointer to root of right subtree

    def __str__(self) -> str:
        """
        Override string method
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return 'BST Node: {}'.format(self.value)


class BST:
    """
    Binary Search Tree class
    """

    def __init__(self, start_tree=None) -> None:
        """
        Initialize new Binary Search Tree
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self._root = None

        # populate BST with initial values (if provided)
        # before using this feature, implement add() method
        if start_tree is not None:
            for value in start_tree:
                self.add(value)

    def __str__(self) -> str:
        """
        Override string method; display in pre-order
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        values = []
        self._str_helper(self._root, values)
        return "BST pre-order { " + ", ".join(values) + " }"

    def _str_helper(self, node: BSTNode, values: []) -> None:
        """
        Helper method for __str__. Does pre-order tree traversal
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        if not node:
            return
        values.append(str(node.value))
        self._str_helper(node.left, values)
        self._str_helper(node.right, values)

    def get_root(self) -> BSTNode:
        """
        Return root of tree, or None if empty
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self._root

    def is_valid_bst(self) -> bool:
        """
        Perform pre-order traversal of the tree.
        Return False if nodes don't adhere to the bst ordering property.

        This is intended to be a troubleshooting method to help find any
        inconsistencies in the tree after the add() or remove() operations.
        A return of True from this method doesn't guarantee that your tree
        is the 'correct' result, just that it satisfies bst ordering.

        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        stack = Stack()
        stack.push(self._root)
        while not stack.is_empty():
            node = stack.pop()
            if node:
                if node.left and node.left.value >= node.value:
                    return False
                if node.right and node.right.value < node.value:
                    return False
                stack.push(node.right)
                stack.push(node.left)
        return True

    def print_tree(self):
        """
        Prints the tree using the print_subtree function.

        This method is intended to assist in visualizing the structure of the
        tree. You are encouraged to add this method to the tests in the Basic
        Testing section of the starter code or your own tests as needed.

        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        if self.get_root():
            self._print_subtree(self.get_root())
        else:
            print('(empty tree)')

    def _print_subtree(self, node, prefix: str = '', branch: str = ''):
        """
        Recursively prints the subtree rooted at this node.

        This is intended as a 'helper' method to assist in visualizing the
        structure of the tree.

        DO NOT CHANGE THIS METHOD IN ANY WAY
        """

        def add_junction(string):
            if len(string) < 2 or branch == '':
                return string
            junction = '|' if string[-2] == '|' else '`'
            return string[:-2] + junction + '-'

        if not node:
            print(add_junction(prefix) + branch + "None")
            return

        if len(prefix) > 2 * 16:
            print(add_junction(prefix) + branch + "(tree continues)")
            return

        if node.left or node.right:
            postfix = ' (root)' if branch == '' else ''
            print(add_junction(prefix) + branch + str(node.value) + postfix)
            self._print_subtree(node.right, prefix + '| ', 'R: ')
            self._print_subtree(node.left, prefix + '  ', 'L: ')
        else:
            print(add_junction(prefix) + branch + str(node.value) + ' (leaf)')

    # ------------------------------------------------------------------ #

    def add(self, value: object) -> None:
        """
        Adds a new value to the tree. Duplicate values are allowed. If a node with
        that value is already in the tree, the new value is added to the right
        subtree of that node.
        """

        new_node = BSTNode(value)

        # if tree is empty, then new node is added
        # and the new node becomes the root
        if self._root is None:
            self._root = new_node
            return

        node = self._root

        # traverse BST to find correct place to add new node
        while node is not None:
            if value < node.value:
                # if there's no left child then new node is added as left child
                if node.left is None:
                    node.left = new_node
                    return
                # if there is a left child, then go to that left child
                node = node.left

            # if new val greater than or equal to val of current node, go right
            else:
                # if there's no right child then new node is added as right child
                if node.right is None:
                    node.right = new_node
                    return
                # if there is a right child, then go to that right child
                node = node.right


    def remove(self, value: object) -> bool:
        """
        Removes a value from the tree. Returns True if the value is removed.
        Otherwise, returns False.
        """

        def find_node_and_parent(root, value):
            """
            Helper method that finds the node that will be removed and its parent.
            """

            parent = None
            current = root

            while current is not None:
                # if node's val equals target val, then this is the node you're looking for
                # return the target node to be removed and its parent
                if value == current.value:
                    return parent, current

                elif value < current.value:
                    parent = current
                    current = current.left

                else:
                    parent = current
                    current = current.right

            # if the value was not found, then return None
            return parent, None

        parent, node_to_remove = find_node_and_parent(self._root, value)

        # target value was not in BST
        if node_to_remove is None:
            return False

        # if the node being removed is a leaf
        if node_to_remove.left is None and node_to_remove.right is None:
            self._remove_no_subtrees(parent, node_to_remove)

        # if the node being removed has one child
        elif node_to_remove.left is None or node_to_remove.right is None:
            self._remove_one_subtree(parent, node_to_remove)

        # if the node being removed has two children
        else:
            self._remove_two_subtrees(parent, node_to_remove)

        # target node was removed
        return True

    def _remove_no_subtrees(self, remove_parent: BSTNode, remove_node: BSTNode) -> None:
        """
        Removes a node that has no subtrees (node being removed
        has no left child and no right child).
        """

        # if the node doesn't have a parent then it's the root of the tree
        if remove_parent is None:
            self._root = None

        # removes node from left of parent node
        elif remove_node.value < remove_parent.value:
            remove_parent.left = None

        # removes node from right of parent node
        else:
            remove_parent.right = None

    def _remove_one_subtree(self, remove_parent: BSTNode, remove_node: BSTNode) -> None:
        """
        Removes a node that has one subtree (node being removed either has a left child
        or a right child, but not both).
        """

        # used to reassign all of the descendents of the target node when removing target
        if remove_node.left:
            subtree = remove_node.left
        else:
            subtree = remove_node.right

        if remove_parent is None:
            self._root = subtree

        elif remove_node.value < remove_parent.value:
            remove_parent.left = subtree

        else:
            remove_parent.right = subtree

    def _remove_two_subtrees(self, remove_parent: BSTNode, remove_node: BSTNode) -> None:
        """
        Used to remove a node that has two children, both a left and a right child.
        """

        parent_of_successor = remove_node
        successor = remove_node.right

        # after the while loop finishes, successor is the inorder successor
        while successor.left is not None:
            parent_of_successor = successor
            successor = successor.left

        # links the parent of node to be removed with successor
        if remove_parent is None:
            self._root = successor

        # if node's val < parent's val, left child of parent becomes successor
        elif remove_node.value < remove_parent.value:
            remove_parent.left = successor

        # if node's val >= parent's val, right child of parent becomes successor
        else:
            remove_parent.right = successor

        # check if successor is directly linked to remove_node
        # if it's not then remove node's right subtree is linked to successor
        if parent_of_successor != remove_node:
            parent_of_successor.left = successor.right
            successor.right = remove_node.right

        # link remove node's left subtree to successor
        successor.left = remove_node.left

        # update children of remove node so remove node is no longer linked to AVL tree
        remove_node.left = None
        remove_node.right = None

    def contains(self, value: object) -> bool:
        """
        Returns True if the value is in the tree. Otherwise, it returns False.
        If the tree is empty, returns False.
        """

        # if BST is empty return False
        if self._root is None:
            return False

        # if BST is not empty start at root
        node = self._root

        # traverse BST and search for target value
        while node is not None:
            if value == node.value:
                return True

            # if target val is less than current node's val move to current node's left child
            elif value < node.value:
                node = node.left

            # if target val >= current node's val, move to current node's right child
            else:
                node = node.right

        return False

    def inorder_traversal(self) -> Queue:
        """
        Performs an inorder traversal of the tree and returns a Queue object that
        contains the values of the visited nodes, in the order they were visited.
        """

        queue = Queue()
        # used to store nodes visited and add nodes to Queue inorder
        stack = Stack()
        node = self._root

        # traverse through BST until all nodes have been added inorder
        # to queue and stack is empty
        while node is not None or not stack.is_empty():
            # traverse down every left child in subtree
            while node is not None:
                # push current node onto stack so it can be added to queue later in
                # the correct order
                stack.push(node)
                node = node.left

            # when you hit a node without a child it means that this is the end of
            # the left subtree, so pop the top of the stack
            node = stack.pop()
            # popped val is added to queue
            queue.enqueue(node.value)
            # move onto right subtree
            node = node.right

        return queue

    def find_min(self) -> object:
        """
        Returns the lowest value in the tree. If the tree is empty, returns None.
        """

        if self._root is None:
            return None

        node = self._root

        # traverses down leftmost subtree as in a BST the lowest val will
        # be the left leaf of the leftmost subtree
        while node.left is not None:
            node = node.left

        return node.value

    def find_max(self) -> object:
        """
        Returns the highest value in the tree. If the tree is empty, returns None.
        """

        if self._root is None:
            return None

        node = self._root

        # traverse down rightmost subtree as that's where the highest value will be
        # highest val will be the right leaf of the rightmost subtree
        while node.right is not None:
            node = node.right

        return node.value

    def is_empty(self) -> bool:
        """
        Returns True if the tree is empty. Otherwise, it returns False
        """

        # if a BST has no root then it's empty
        # if it does have a root then it can't be empty
        if self._root is None:
            return True

        return False

    def make_empty(self) -> None:
        """
        Removes all of the nodes from the tree.
        """

        self._root = None

# ------------------- BASIC TESTING -----------------------------------------

if __name__ == '__main__':

    print("\nPDF - method add() example 1")
    print("----------------------------")
    test_cases = (
        (1, 2, 3),
        (3, 2, 1),
        (1, 3, 2),
        (3, 1, 2),
    )
    for case in test_cases:
        tree = BST(case)
        print(tree)
        tree.print_tree()

    print("\nPDF - method add() example 2")
    print("----------------------------")
    test_cases = (
        (10, 20, 30, 40, 50),
        (10, 20, 30, 50, 40),
        (30, 20, 10, 5, 1),
        (30, 20, 10, 1, 5),
        (5, 4, 6, 3, 7, 2, 8),
        (range(0, 30, 3)),
        (range(0, 31, 3)),
        (range(0, 34, 3)),
        (range(10, -10, -2)),
        ('A', 'B', 'C', 'D', 'E'),
        (1, 1, 1, 1),
    )
    for case in test_cases:
        tree = BST(case)
        print('INPUT  :', case)
        print('RESULT :', tree)

    print("\nPDF - method add() example 3")
    print("----------------------------")
    for _ in range(100):
        case = list(set(random.randrange(1, 20000) for _ in range(900)))
        tree = BST()
        for value in case:
            tree.add(value)
        if not tree.is_valid_bst():
            raise Exception("PROBLEM WITH ADD OPERATION")
    print('add() stress test finished')

    print("\nPDF - method remove() example 1")
    print("-------------------------------")
    test_cases = (
        ((1, 2, 3), 1),
        ((1, 2, 3), 2),
        ((1, 2, 3), 3),
        ((50, 40, 60, 30, 70, 20, 80, 45), 0),
        ((50, 40, 60, 30, 70, 20, 80, 45), 45),
        ((50, 40, 60, 30, 70, 20, 80, 45), 40),
        ((50, 40, 60, 30, 70, 20, 80, 45), 30),
    )
    for case, del_value in test_cases:
        tree = BST(case)
        print('INPUT  :', tree, "DEL:", del_value)
        tree.remove(del_value)
        print('RESULT :', tree)

    print("\nPDF - method remove() example 2")
    print("-------------------------------")
    test_cases = (
        ((50, 40, 60, 30, 70, 20, 80, 45), 20),
        ((50, 40, 60, 30, 70, 20, 80, 15), 40),
        ((50, 40, 60, 30, 70, 20, 80, 35), 20),
        ((50, 40, 60, 30, 70, 20, 80, 25), 40),
    )
    for case, del_value in test_cases:
        tree = BST(case)
        print('INPUT  :', tree, "DEL:", del_value)
        tree.print_tree()
        tree.remove(del_value)
        print('RESULT :', tree)
        tree.print_tree()
        print('')

    print("\nPDF - method remove() example 3")
    print("-------------------------------")
    case = range(-9, 16, 2)
    tree = BST(case)
    for del_value in case:
        print('INPUT  :', tree, del_value)
        tree.remove(del_value)
        print('RESULT :', tree)

    print("\nPDF - method remove() example 4")
    print("-------------------------------")
    case = range(0, 34, 3)
    tree = BST(case)
    for _ in case[:-2]:
        root_value = tree.get_root().value
        print('INPUT  :', tree, root_value)
        tree.remove(root_value)
        if not tree.is_valid_bst():
            raise Exception("PROBLEM WITH REMOVE OPERATION")
        print('RESULT :', tree)

    print("\nPDF - method contains() example 1")
    print("---------------------------------")
    tree = BST([10, 5, 15])
    print(tree.contains(15))
    print(tree.contains(-10))
    print(tree.contains(15))

    print("\nPDF - method contains() example 2")
    print("---------------------------------")
    tree = BST()
    print(tree.contains(0))

    print("\nPDF - method inorder_traversal() example 1")
    print("---------------------------------")
    tree = BST([10, 20, 5, 15, 17, 7, 12])
    print(tree.inorder_traversal())

    print("\nPDF - method inorder_traversal() example 2")
    print("---------------------------------")
    tree = BST([8, 10, -4, 5, -1])
    print(tree.inorder_traversal())

    print("\nPDF - method find_min() example 1")
    print("---------------------------------")
    tree = BST([10, 20, 5, 15, 17, 7, 12])
    print(tree)
    print("Minimum value is:", tree.find_min())

    print("\nPDF - method find_min() example 2")
    print("---------------------------------")
    tree = BST([8, 10, -4, 5, -1])
    print(tree)
    print("Minimum value is:", tree.find_min())

    print("\nPDF - method find_max() example 1")
    print("---------------------------------")
    tree = BST([10, 20, 5, 15, 17, 7, 12])
    print(tree)
    print("Maximum value is:", tree.find_max())

    print("\nPDF - method find_max() example 2")
    print("---------------------------------")
    tree = BST([8, 10, -4, 5, -1])
    print(tree)
    print("Maximum value is:", tree.find_max())

    print("\nPDF - method is_empty() example 1")
    print("---------------------------------")
    tree = BST([10, 20, 5, 15, 17, 7, 12])
    print("Tree is empty:", tree.is_empty())

    print("\nPDF - method is_empty() example 2")
    print("---------------------------------")
    tree = BST()
    print("Tree is empty:", tree.is_empty())

    print("\nPDF - method make_empty() example 1")
    print("---------------------------------")
    tree = BST([10, 20, 5, 15, 17, 7, 12])
    print("Tree before make_empty():", tree)
    tree.make_empty()
    print("Tree after make_empty(): ", tree)

    print("\nPDF - method make_empty() example 2")
    print("---------------------------------")
    tree = BST()
    print("Tree before make_empty():", tree)
    tree.make_empty()
    print("Tree after make_empty(): ", tree)
