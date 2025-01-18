import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_eq2(self):
        node1 = TextNode("Testing",TextType.NORMAL)
        node2 = TextNode("Testing",TextType.NORMAL)
        self.assertEqual(node1,node2)
    
    def test_url(self):
        node=TextNode("Testing",TextType.LINK,"My URL")
        self.assertEqual("TextNode(Testing, link, My URL)",str(node))

    def test_neq(self):
        node1 = TextNode("Testing",TextType.BOLD)
        node2 = TextNode("Testing",TextType.NORMAL)
        self.assertNotEqual(node1,node2)
    
    


if __name__ == "__main__":
    unittest.main()