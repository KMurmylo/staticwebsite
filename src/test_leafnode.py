import unittest

from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_no_tags(self):
        node=LeafNode(None,"Hello World")
        self.assertEqual("Hello World",node.to_html())
    
    def test_for_error(self):
        self.assertRaises(ValueError,LeafNode,"Some Tag",None)

    def test_word_and_tag(self):
        node=LeafNode("p", "Hello World")
        self.assertEqual("<p>Hello World</p>",node.to_html())

    def test_tag_value_prop(self):
        node= LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual("<a href=\"https://www.google.com\">Click me!</a>",node.to_html())







if __name__ == "__main__":
    unittest.main()