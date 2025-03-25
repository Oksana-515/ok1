import unittest
from task1 import *

class TestChickenRegex(unittest.TestCase):
    
    def test_remove_special_chars(self):
        self.assertEqual(remove_special_chars("Chickens! peck, corn."), "Chickenspeckcorn")
        self.assertEqual(remove_special_chars("Rooster 123@#"), "Rooster123")
        self.assertEqual(remove_special_chars(""), "")
    
    def test_words_with_char(self):
        text = "Chickens peck corn from feeder"
        self.assertEqual(words_with_char(text, "e"), ['Chickens', 'peck', 'feeder'])
        self.assertEqual(words_with_char(text, "c"), ['Chickens', 'peck', 'corn'])
        self.assertEqual(words_with_char("Hen lays eggs", "y"), ['lays'])
    
    def test_words_of_length(self):
        text = "Hen sits on the nest"
        self.assertEqual(words_of_length(text, 3), ['Hen', 'the'])
        self.assertEqual(words_of_length(text, 4), ['sits', 'nest'])
        self.assertEqual(words_of_length("Big chicken runs", 5), [])
    
    def test_words_a_b_ends_s(self):
        text = "Birds eat grains as chickens bask"
        self.assertEqual(words_a_b_ends_s(text), ['Birds', 'as'])
        self.assertEqual(words_a_b_ends_s("A hen sits on eggs"), [])
        self.assertEqual(words_a_b_ends_s("Best birds nests"), ['birds'])

if __name__ == '__main__':
    unittest.main()