import unittest
from task3 import clean_python_code  # Замініть на ім'я вашого модуля

class TestCleanPythonCode(unittest.TestCase):

    def test_single_line_comments(self):
        code = """# Comment at start
def func():
    pass  # Inline comment"""
        
        expected = """def func():
    pass"""
        self.assertEqual(clean_python_code(code), expected)

    def test_multi_line_comments(self):
        code = '''"""
Multi-line
comment
"""
def test():
    \'\'\'Docstring\'\'\'
    return True'''
        
        expected = '''def test():
    return True'''
        self.assertEqual(clean_python_code(code), expected)

    def test_blank_lines(self):
        code = """def foo():
    
    print("Hello")
    
    
    return 0"""
        
        expected = """def foo():
    print("Hello")
    return 0"""
        self.assertEqual(clean_python_code(code), expected)

    def test_mixed_content(self):
        code = """# Imports
import os

'''
Config section
'''
def main():
    \'\'\'Main function\'\'\'
    print("Running...")  # Debug
    
    return 0"""
        
        expected = """import os
def main():
    print("Running...")
    return 0"""
        self.assertEqual(clean_python_code(code), expected)

    def test_empty_input(self):
        self.assertEqual(clean_python_code(""), "")
        self.assertEqual(clean_python_code("\n\n   \n"), "")

    def test_preserve_indentation(self):
        code = """if True:
    # Comment
        print("Indented")"""
        
        expected = """if True:
        print("Indented")"""
        self.assertEqual(clean_python_code(code), expected)



if __name__ == '__main__':
    unittest.main()