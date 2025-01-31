# Name:
# OSU Email: @oregonstate.edu
# Course: CS261 - Data Structures
# Assignment: 4 BST/AVL Tree Implementation
# Due Date: 7/29/2024
# Description: The AVL class is implemented by completing the skeleton code
# below. The implementation overrides the add() and remove() methods from
# BST.py such that the AVL tree remains balanced after each insertion or
# removal of a value. The AVL class also inherits the following methods:
# contains(), inorder_traversal(), find_min(), find_max(), is_empty(),
# and make_empty().


import random
from queue_and_stack import Queue, Stack
from bst import BSTNode, BST


class AVLNode(BSTNode):
    """
    AVL Tree Node class. Inherits from BSTNode
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    def __init__(self, value: object) -> None:
        """
        Initialize a new AVL node
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        # call __init__() from parent class
        super().__init__(value)

        # new variables needed for AVL
        self.parent = None
        self.height = 0

    def __str__(self) -> str:
        """
        Override string method
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return 'AVL Node: {}'.format(self.value)


class AVL(BST):
    """
    AVL Tree class. Inherits from BST
    """

    def __init__(self, start_tree=None) -> None:
        """
        Initialize a new AVL Tree
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        # call __init__() from parent class
        super().__init__(start_tree)

    def __str__(self) -> str:
        """
        Override string method
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        values = []
        super()._str_helper(self._root, values)
        return "AVL pre-order { " + ", ".join(values) + " }"

    def is_valid_avl(self) -> bool:
        """
        Perform pre-order traversal of the tree. Return False if there
        are any problems with attributes of any of the nodes in the tree.

        This is intended to be a troubleshooting 'helper' method to help
        find any inconsistencies in the tree after the add() or remove()
        operations. Review the code to understand what this method is
        checking and how it determines whether the AVL tree is correct.

        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        stack = Stack()
        stack.push(self._root)
        while not stack.is_empty():
            node = stack.pop()
            if node:
                # check for correct height (relative to children)
                left = node.left.height if node.left else -1
                right = node.right.height if node.right else -1
                if node.height != 1 + max(left, right):
                    return False

                if node.parent:
                    # parent and child pointers are in sync
                    if node.value < node.parent.value:
                        check_node = node.parent.left
                    else:
                        check_node = node.parent.right
                    if check_node != node:
                        return False
                else:
                    # NULL parent is only allowed on the root of the tree
                    if node != self._root:
                        return False
                stack.push(node.right)
                stack.push(node.left)
        return True

    # ------------------------------------------------------------------ #

    def add(self, value: object) -> None:
        """
        Adds a new value to the tree while maintaining its AVL property. Duplicate
        values are not allowed. If the value is already in the tree, it does not
        change the tree.
        """

        # if the tree is empty then the new value will become the root
        if not self._root:
            self._root = AVLNode(value)

        # calls helper method to add a value to non-empty tree in the right spot
        else:
            # recursively adds val to correct pos in tree & updates root
            self._root = self.recursive_add(self._root, value)

    def recursive_add(self, node: AVLNode, value: object) -> AVLNode:
        """
        Helper method to recursively add a value to the subtree rooted at node.
        """

        # if current node is none then this is the correct spot to insert the new value
        if node is None:
            return AVLNode(value)

        # if target val is less than current node's val, then recursively
        # add it into left subtree
        if value < node.value:
            node.left = self.recursive_add(node.left, value)
            if node.left:
                # links current node to be parent of newly inserted node
                node.left.parent = node

        # if target val is greater than current node's val, then recursively
        # add it into right subtree
        elif value > node.value:
            node.right = self.recursive_add(node.right, value)
            if node.right:
                # links current node to be parent of the new node
                node.right.parent = node

        self._update_height(node)
        rebalanced_node = self._rebalance(node)

        return rebalanced_node

    def remove(self, value: object) -> bool:
        """
        Removes the value from the AVL tree. Returns True if the value is removed.
        Otherwise, returns False.
        """

        # if tree is empty then target value can't be removed from tree
        if not self._root:
            return False

        # recursively remove target value and update root
        self._root, removed = self._remove(self._root, value)

        # if tree isn't emtpy, update height and rebalance tree from its root
        if self._root:
            self._update_height(self._root)
            self._rebalance(self._root)

        return removed

    def _remove(self, node: AVLNode, value: object) -> (AVLNode, bool):
        """
        Helper method to recursively remove target value.
        """

        # if current node is None this means target value isn't in tree
        if node is None:
            return None, False

        removed = False

        # if target val less than current node's val then use recursion
        # to go into left subtree
        if value < node.value:
            node.left, removed = self._remove(node.left, value)

        # if target val greater than current node's val then use recursion
        # to go into right subtree
        elif value > node.value:
            node.right, removed = self._remove(node.right, value)

        else:
            # node with target val has been found
            removed = True
            if node.left is None:
                return node.right, removed
            elif node.right is None:
                return node.left, removed
            else:
                # Node has two children. Look for the inorder successor
                min_larger_node = self._get_min(node.right)
                # replaces current node's val with inorder successor's val
                node.value = min_larger_node.value
                # Remove the inorder successor from right subtree
                node.right, _ = self._remove(node.right, min_larger_node.value)

        # once inorder successor has been removed, node's height is updated and
        # current node's subtree is rebalanced (tree containing current node and
        # all of its descendents)
        if node:
            self._update_height(node)
            node = self._rebalance(node)

        return node, removed

    def _balance_factor(self, node: AVLNode) -> int:
        """
        Calculates a node's balance factor.
        """
        return self._get_height(node.left) - self._get_height(node.right)

    def _get_height(self, node: AVLNode) -> int:
        """
        Returns a node's height.
        """

        if node is None:
            return -1
        else:
            return node.height

    def _find_max_height(self, height1: int, height2: int) -> int:
        """
        Returns the greater value of two heights.
        """

        if height1 > height2:
            return height1
        else:
            return height2


    def _rotate_left(self, node: AVLNode) -> AVLNode:
        """
        Performs a left rotation around a node.
        """

        # right child will become new root of subtree
        right_child = node.right
        # used to temporarily store node's right child's left child
        # right child's left subtree will become current node's right subtree
        storage = right_child.left
        right_child.left = node
        node.right = storage

        # Updates parent pointers
        if storage:
            storage.parent = node
        right_child.parent = node.parent
        node.parent = right_child

        # Updates heights of nodes that were rotated
        self._update_height(node)
        self._update_height(right_child)

        return right_child

    def _rotate_right(self, node: AVLNode) -> AVLNode:
        """
        Performs a right rotation around a node.
        """

        # left child will become new root of subtree
        left_child = node.left
        # left child's right subtree will become current node's left subtree
        storage = left_child.right
        left_child.right = node
        node.left = storage

        # Updates parent pointers
        if storage:
            storage.parent = node
        left_child.parent = node.parent
        node.parent = left_child

        # Update heights of nodes that were rotated
        self._update_height(node)
        self._update_height(left_child)

        return left_child

    def _update_height(self, node: AVLNode) -> None:
        """
        Updates the height of a node.
        """

        # Calculates height for current node using its children
        left_height = self._get_height(node.left)
        right_height = self._get_height(node.right)
        # node's height is the max height of either right or left subtree (whichever
        # of the two subtrees has the greater height) plus one
        node.height = 1 + self._find_max_height(left_height, right_height)

    def _rebalance(self, node: AVLNode) -> AVLNode:
        """
        Rebalances the AVL tree at the given node.
        """

        balance = self._balance_factor(node)

        # this means the node's left subtree is taller
        if balance > 1:
            # this means that right child of left subtree is taller,
            # so a left right rotation must be performed
            if self._balance_factor(node.left) < 0:
                node.left = self._rotate_left(node.left)
            return self._rotate_right(node)

        # this means the node's right subtree is taller
        if balance < -1:
            # this means that left child of right subtree is taller,
            # so a right left rotation must be performed
            if self._balance_factor(node.right) > 0:
                node.right = self._rotate_right(node.right)
            return self._rotate_left(node)

        return node

    def _get_min(self, node: AVLNode) -> AVLNode:
        """
        Returns the node with the smallest val in the subtree rooted at node.
        """
        if node is None:
            return None

        while node.left is not None:
            node = node.left

        return node
    
# ------------------- BASIC TESTING -----------------------------------------


if __name__ == '__main__':

    print("\nPDF - method add() example 1")
    print("----------------------------")
    test_cases = (
        (1, 2, 3),  # RR
        (3, 2, 1),  # LL
        (1, 3, 2),  # RL
        (3, 1, 2),  # LR
    )
    for case in test_cases:
        tree = AVL(case)
        print(tree)
        tree.print_tree()

    print("\nPDF - method add() example 2")
    print("----------------------------")
    test_cases = (
        (10, 20, 30, 40, 50),   # RR, RR
        (10, 20, 30, 50, 40),   # RR, RL
        (30, 20, 10, 5, 1),     # LL, LL
        (30, 20, 10, 1, 5),     # LL, LR
        (5, 4, 6, 3, 7, 2, 8),  # LL, RR
        (range(0, 30, 3)),
        (range(0, 31, 3)),
        (range(0, 34, 3)),
        (range(10, -10, -2)),
        ('A', 'B', 'C', 'D', 'E'),
        (1, 1, 1, 1),
    )
    for case in test_cases:
        tree = AVL(case)
        print('INPUT  :', case)
        print('RESULT :', tree)

    print("\nPDF - method add() example 3")
    print("----------------------------")
    for _ in range(100):
        case = list(set(random.randrange(1, 20000) for _ in range(900)))
        tree = AVL()
        for value in case:
            tree.add(value)
        if not tree.is_valid_avl():
            raise Exception("PROBLEM WITH ADD OPERATION")
    print('add() stress test finished')

    print("\nPDF - method remove() example 1")
    print("-------------------------------")
    test_cases = (
        ((1, 2, 3), 1),  # no AVL rotation
        ((1, 2, 3), 2),  # no AVL rotation
        ((1, 2, 3), 3),  # no AVL rotation
        ((50, 40, 60, 30, 70, 20, 80, 45), 0),
        ((50, 40, 60, 30, 70, 20, 80, 45), 45),  # no AVL rotation
        ((50, 40, 60, 30, 70, 20, 80, 45), 40),  # no AVL rotation
        ((50, 40, 60, 30, 70, 20, 80, 45), 30),  # no AVL rotation
    )
    for case, del_value in test_cases:
        tree = AVL(case)
        print('INPUT  :', tree, "DEL:", del_value)
        tree.remove(del_value)
        print('RESULT :', tree)

    print("\nPDF - method remove() example 2")
    print("-------------------------------")
    test_cases = (
        ((50, 40, 60, 30, 70, 20, 80, 45), 20),  # RR
        ((50, 40, 60, 30, 70, 20, 80, 15), 40),  # LL
        ((50, 40, 60, 30, 70, 20, 80, 35), 20),  # RL
        ((50, 40, 60, 30, 70, 20, 80, 25), 40),  # LR
    )
    for case, del_value in test_cases:
        tree = AVL(case)
        print('INPUT  :', tree, "DEL:", del_value)
        tree.print_tree()
        tree.remove(del_value)
        print('RESULT :', tree)
        tree.print_tree()
        print('')

    print("\nPDF - method remove() example 3")
    print("-------------------------------")
    case = range(-9, 16, 2)
    tree = AVL(case)
    for del_value in case:
        print('INPUT  :', tree, del_value)
        tree.remove(del_value)
        print('RESULT :', tree)

    print("\nPDF - method remove() example 4")
    print("-------------------------------")
    case = range(0, 34, 3)
    tree = AVL(case)
    for _ in case[:-2]:
        root_value = tree.get_root().value
        print('INPUT  :', tree, root_value)
        tree.remove(root_value)
        print('RESULT :', tree)

    print("\nPDF - method remove() example 5")
    print("-------------------------------")
    for _ in range(100):
        case = list(set(random.randrange(1, 20000) for _ in range(900)))
        tree = AVL(case)
        for value in case[::2]:
            tree.remove(value)
        if not tree.is_valid_avl():
            raise Exception("PROBLEM WITH REMOVE OPERATION")
    print('remove() stress test finished')

    print("\nPDF - method contains() example 1")
    print("---------------------------------")
    tree = AVL([10, 5, 15])
    print(tree.contains(15))
    print(tree.contains(-10))
    print(tree.contains(15))

    print("\nPDF - method contains() example 2")
    print("---------------------------------")
    tree = AVL()
    print(tree.contains(0))

    print("\nPDF - method inorder_traversal() example 1")
    print("---------------------------------")
    tree = AVL([10, 20, 5, 15, 17, 7, 12])
    print(tree.inorder_traversal())

    print("\nPDF - method inorder_traversal() example 2")
    print("---------------------------------")
    tree = AVL([8, 10, -4, 5, -1])
    print(tree.inorder_traversal())

    print("\nPDF - method find_min() example 1")
    print("---------------------------------")
    tree = AVL([10, 20, 5, 15, 17, 7, 12])
    print(tree)
    print("Minimum value is:", tree.find_min())

    print("\nPDF - method find_min() example 2")
    print("---------------------------------")
    tree = AVL([8, 10, -4, 5, -1])
    print(tree)
    print("Minimum value is:", tree.find_min())

    print("\nPDF - method find_max() example 1")
    print("---------------------------------")
    tree = AVL([10, 20, 5, 15, 17, 7, 12])
    print(tree)
    print("Maximum value is:", tree.find_max())

    print("\nPDF - method find_max() example 2")
    print("---------------------------------")
    tree = AVL([8, 10, -4, 5, -1])
    print(tree)
    print("Maximum value is:", tree.find_max())

    print("\nPDF - method is_empty() example 1")
    print("---------------------------------")
    tree = AVL([10, 20, 5, 15, 17, 7, 12])
    print("Tree is empty:", tree.is_empty())

    print("\nPDF - method is_empty() example 2")
    print("---------------------------------")
    tree = AVL()
    print("Tree is empty:", tree.is_empty())

    print("\nPDF - method make_empty() example 1")
    print("---------------------------------")
    tree = AVL([10, 20, 5, 15, 17, 7, 12])
    print("Tree before make_empty():", tree)
    tree.make_empty()
    print("Tree after make_empty(): ", tree)

    print("\nPDF - method make_empty() example 2")
    print("---------------------------------")
    tree = AVL()
    print("Tree before make_empty():", tree)
    tree.make_empty()
    print("Tree after make_empty(): ", tree)
