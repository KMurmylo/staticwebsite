import unittest

from parentnode import ParentNode
from leafnode import LeafNode 

class TestParentNode(unittest.TestCase):
    def test_basic(self):
        node = ParentNode(
                            "p",
                [
                    LeafNode("b", "Bold text"),
                    LeafNode(None, "Normal text"),
                    LeafNode("i", "italic text"),
                    LeafNode(None, "Normal text"),
                ],)
        self.assertEqual(node.to_html(),"<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>")

    def test_no_Children(self):
        with self.assertRaises(ValueError):
            node=ParentNode("p",None).to_html()

    def test_empty_children(self):
        with self.assertRaises(ValueError):
            node=ParentNode("p",[]).to_html()




if __name__ == "__main__":
    unittest.main()