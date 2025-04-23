from collections import deque


class Node:
    def __init__(self, block):
        self.left = None
        self.right = None
        self.block = block

    def insert(self, new_block):
        if self.block is None:
            self.block = new_block
        elif new_block['value'] <= self.block['value']:
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
    def __init__(self):
        self.root = None

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

    def check_properties(self):
        if not self.root:
            return {"is_full": True, "is_complete": True, "is_perfect": True}

        queue = deque([(self.root, 0)])
        is_full = True
        is_complete = True
        found_gap = False
        min_depth = float('inf')
        max_depth = float('-inf')

        while queue:
            node, level = queue.popleft()

            if not node.left and not node.right:
                min_depth = min(min_depth, level)
                max_depth = max(max_depth, level)

            if node.left:
                if found_gap:
                    is_complete = False
                queue.append((node.left, level + 1))
            else:
                found_gap = True

            if node.right:
                if found_gap:
                    is_complete = False
                queue.append((node.right, level + 1))
            else:
                found_gap = True

            if (node.left and not node.right) or (not node.left and node.right):
                is_full = False

        is_perfect = is_full and is_complete and min_depth == max_depth

        return {
            "is_full": is_full,
            "is_complete": is_complete,
            "is_perfect": is_perfect
        }