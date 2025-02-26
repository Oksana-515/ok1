import unittest

from lab_1 import create_block, can_add_to_chain

class TestBlockchainFunctions(unittest.TestCase):

    def test_create_block(self):
        block = create_block('0x1', 0)
        self.assertEqual(block, {'id': '0x1', 'view': 0})
        
    def test_can_add_to_chain(self):
        chain = [{'id': '0x1', 'view': 0}]
        block = create_block('0x2', 1)
        votes = {'0x2'}
        self.assertTrue(can_add_to_chain(chain, block, votes))
        block_invalid_view = create_block('0x2', 2)
        self.assertFalse(can_add_to_chain(chain, block_invalid_view, votes))
        block_no_vote = create_block('0x3', 1)
        self.assertFalse(can_add_to_chain(chain, block_no_vote, votes))

if __name__ == '__main__':
    unittest.main()
