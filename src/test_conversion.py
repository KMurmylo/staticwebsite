import unittest
from textnode import TextNode,TextType
from conversion import text_node_to_html_node

class TestTextNode(unittest.TestCase):

    def test_text(self):
        node=TextNode("Testing",TextType.TEXT)
        self.assertEqual(text_node_to_html_node(node).to_html(),"Testing")

    def test_bold(self):
        node=TextNode("Testing",TextType.BOLD)
        self.assertEqual(text_node_to_html_node(node).to_html(),"<b>Testing</b>")
 
    def test_italic(self):
        node=TextNode("Testing",TextType.ITALIC)
        self.assertEqual(text_node_to_html_node(node).to_html(),"<i>Testing</i>")
 

    def test_code(self):
        node=TextNode("Testing",TextType.CODE)
        self.assertEqual(text_node_to_html_node(node).to_html(),"<code>Testing</code>")

    def test_link(self):
        node=TextNode("Testing",TextType.LINK,"www.google.com")
        self.assertEqual(text_node_to_html_node(node).to_html(),"<a href=\"www.google.com\">Testing</a>")

    def test_image(self):
        node=TextNode("Testing",TextType.IMAGE,"LinkToImage")
        self.assertEqual(text_node_to_html_node(node).to_html(),"<img src=\"LinkToImage\" alt=\"Testing\">")

    def test_error(self):
        node=TextNode("Testing","Wrong")
        self.assertRaises(ValueError,text_node_to_html_node,node)



if __name__ == "__main__":
    unittest.main()