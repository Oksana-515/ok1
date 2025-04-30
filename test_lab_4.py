import unittest
from lab_4 import BinaryTree
from dataclasses import dataclass

@dataclass
class Block:
    value: int

class TestBinaryTree(unittest.TestCase):
    def test_full_tree(self):
        chain = [Block(10), Block(5), Block(15), Block(3), Block(7), Block(12), Block(18)]
        tree = BinaryTree(chain)
        self.assertTrue(tree.is_full(tree.root))

    def test_not_full_tree(self):
        chain = [Block(10), Block(5), Block(15), Block(3), Block(7), Block(12)]
        tree = BinaryTree(chain)
        self.assertFalse(tree.is_full(tree.root))

    def test_complete_and_perfect_tree(self):
        chain = [Block(10), Block(5), Block(15), Block(3), Block(7), Block(12), Block(18)]
        tree = BinaryTree(chain)
        is_complete, is_perfect = tree.is_complete_perfect()
        self.assertTrue(is_complete)
        self.assertTrue(is_perfect)

    def test_complete_but_not_perfect_tree(self):
        chain = [Block(10), Block(5), Block(15), Block(3), Block(7), Block(12)]
        tree = BinaryTree(chain)
        is_complete, is_perfect = tree.is_complete_perfect()
        self.assertTrue(is_complete)
        self.assertFalse(is_perfect)

    def test_not_complete_and_not_perfect_tree(self):
        chain = [Block(10), Block(5), Block(7)]
        tree = BinaryTree(chain)
        is_complete, is_perfect = tree.is_complete_perfect()
        self.assertFalse(is_complete)
        self.assertFalse(is_perfect)

if __name__ == '__main__':
    unittest.main()