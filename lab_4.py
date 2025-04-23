from collections import deque


class Node:
    def __init__(self, block):
        self.left = None
        self.right = None
        self.block = block

    def insert(self, new_block):
        if self.block is None:
            self.block = new_block
        elif new_block.value <= self.block.value:
            if self.left is None:
                self.left = Node(new_block)
            else:
                self.left.insert(new_block)
        else:
            if self.right is None:
                self.right = Node(new_block)
            else:
                self.right.insert(new_block)


class BinaryTree:
    def __init__(self, chain):
        self.root = None
        self.build_tree(chain)

        properties = (self.is_full(self.root), *self.is_complete_perfect())
        print(f"Is the tree full? {properties[0]}")
        print(f"Is the tree complete? {properties[1]}")
        print(f"Is the tree perfect? {properties[2]}")

        print('In order traversal:')
        self.in_order_traversal(self.root)
        print("Preorder traversal:")
        self.pre_order_traversal(self.root)
        print("Postorder traversal:")
        self.post_order_traversal(self.root)

    def insert(self, block):
        if self.root is None:
            self.root = Node(block)
        else:
            self.root.insert(block)

    def build_tree(self, chain):
        for block in chain:
            self.insert(block)

    def in_order_traversal(self, node):
        if node:
            self.in_order_traversal(node.left)
            print(node.block)
            self.in_order_traversal(node.right)

    def pre_order_traversal(self, node):
        if node:
            print(node.block)
            self.pre_order_traversal(node.left)
            self.pre_order_traversal(node.right)

    def post_order_traversal(self, node):
        if node:
            self.post_order_traversal(node.left)
            self.post_order_traversal(node.right)
            print(node.block)

    def is_complete_perfect(self):
        if not self.root:
            return True, True

        queue = deque([(self.root, 0)])
        
        max_depth = float('-inf')
        missing_child_level = float('inf')

        while queue:
            node, level = queue.popleft()

            if node.left:
                queue.append((node.left, level + 1))
                if level > missing_child_level:
                    return False, False
            else:
                missing_child_level = min(level, missing_child_level)
                max_depth = max(level, max_depth)

            if node.right:
                queue.append((node.right, level + 1))
                if level > missing_child_level:
                    return False, False
            else:
                missing_child_level = min(level, missing_child_level)
                max_depth = max(level, max_depth)

        return True, missing_child_level == max_depth
    
    def is_full(self, node):
        if node is None:
            return True

        if (node.left is None) != (node.right is None):
            return False

        return self.is_full(node.left) and self.is_full(node.right)