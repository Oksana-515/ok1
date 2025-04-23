import unittest
from lab_4 import BinaryTree

class TestBinaryTree(unittest.TestCase):
    def test_empty_tree(self):
        tree = BinaryTree()
        properties = tree.check_properties()
        self.assertTrue(properties["is_full"])
        self.assertTrue(properties["is_complete"])
        self.assertTrue(properties["is_perfect"])

    def test_single_node_tree(self):
        tree = BinaryTree()
        tree.insert({"value": 10})
        properties = tree.check_properties()
        self.assertTrue(properties["is_full"])
        self.assertTrue(properties["is_complete"])
        self.assertTrue(properties["is_perfect"])

    def test_full_tree(self):
        tree = BinaryTree()
        tree.insert({"value": 10})
        tree.insert({"value": 5})
        tree.insert({"value": 15})
        properties = tree.check_properties()
        self.assertTrue(properties["is_full"])
        self.assertTrue(properties["is_complete"])
        self.assertTrue(properties["is_perfect"])

    def test_complete_but_not_full_tree(self):
        tree = BinaryTree()
        tree.insert({"value": 10})
        tree.insert({"value": 5})
        tree.insert({"value": 15})
        tree.insert({"value": 3})
        properties = tree.check_properties()
        self.assertFalse(properties["is_full"])
        self.assertTrue(properties["is_complete"])
        self.assertFalse(properties["is_perfect"])

    def test_perfect_tree(self):
        tree = BinaryTree()
        tree.insert({"value": 10})
        tree.insert({"value": 5})
        tree.insert({"value": 15})
        tree.insert({"value": 3})
        tree.insert({"value": 7})
        tree.insert({"value": 13})
        tree.insert({"value": 17})
        properties = tree.check_properties()
        self.assertTrue(properties["is_full"])
        self.assertTrue(properties["is_complete"])
        self.assertTrue(properties["is_perfect"])

    def test_incomplete_tree(self):
        tree = BinaryTree()
        tree.insert({"value": 10})
        tree.insert({"value": 5})
        tree.insert({"value": 15})
        tree.insert({"value": 3})
        tree.insert({"value": 7})
        tree.insert({"value": 1})
        tree.insert({"value": 4})
        properties = tree.check_properties()
        self.assertTrue(properties["is_full"])
        self.assertFalse(properties["is_complete"])
        self.assertFalse(properties["is_perfect"])


if __name__ == "__main__":
    unittest.main()