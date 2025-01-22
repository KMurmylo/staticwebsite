import unittest
from blocktoblocktype import block_to_block_type

class TestblockgoBlocktype(unittest.TestCase):

    def test_Head1(self):
        input="# Main Title"
        self.assertEqual(block_to_block_type(input),"heading")
    def test_Head2(self):
        input="### Third level heading"
        self.assertEqual(block_to_block_type(input),"heading")

    def test_code(self):
        input="``` \nPrint.('hello')```"
        self.assertEqual(block_to_block_type(input),"code")

    def test_quote(self):
        input="> First line\n> Second line"
        self.assertEqual(block_to_block_type(input),"quote")

    def test_ulist(self):
        input="* Item one\n* Item two"
        self.assertEqual(block_to_block_type(input),"unordered_list")
    def test_ulist2(self):
        input="- Item one\n- Item two"
        self.assertEqual(block_to_block_type(input),"unordered_list")

    def test_olist(self):
        input="1. First\n2. Second\n3. Third"
        self.assertEqual(block_to_block_type(input),"ordered_list")
    def test_invaliolist(self):
        input="1. First\n3. Second\n5. Third"
        self.assertEqual(block_to_block_type(input),"paragraph")
    def test_parahraph(self):
        input="Just a regular paragraph"
        self.assertEqual(block_to_block_type(input),"paragraph")

    def test_multiline_code(self):
        input = "```\nline 1\nline 2\n```"
        self.assertEqual(block_to_block_type(input), "code")

    def test_invalid_quote(self):
        input = ">no space after arrow"
        self.assertEqual(block_to_block_type(input), "paragraph")

    def test_invalid_unordered(self):
        input = "*no space after asterisk"
        self.assertEqual(block_to_block_type(input), "paragraph")

if __name__ == "__main__":
    unittest.main()