import unittest
from splitnodesdelimiter import split_nodes_delimiter
from textnode import TextNode,TextType

class TestParentNode(unittest.TestCase):

    def test_basic(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        test_result=[
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("code block", TextType.CODE),
                TextNode(" word", TextType.TEXT),
                ]
        self.assertEqual(new_nodes,test_result)

    def test_bold(self):
        node = TextNode("This is text with a **bold block** word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        test_result=[
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("bold block", TextType.BOLD),
                TextNode(" word", TextType.TEXT),
                ]
        self.assertEqual(new_nodes,test_result)
    
    def test_itallic(self):
        node = TextNode("This is text with a *bold block* word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "*", TextType.ITALIC)
        test_result=[
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("bold block", TextType.ITALIC),
                TextNode(" word", TextType.TEXT),
                ]
        self.assertEqual(new_nodes,test_result)

    def test_no_delimiters(self):
        node = TextNode("This is plain text", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        test_result = [node]  # Should return original node
        self.assertEqual(new_nodes, test_result)

    def test_non_text_node(self):
        node = TextNode("Already bold", TextType.BOLD)
        new_nodes = split_nodes_delimiter([node], "*", TextType.ITALIC)
        test_result = [node]  # Should return original node unchanged
        self.assertEqual(new_nodes, test_result)

    def test_multiple(self):
        node = TextNode("This *is text* with a *bold block* word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "*", TextType.ITALIC)
        test_result=[
                TextNode("This ", TextType.TEXT),
                TextNode("is text", TextType.ITALIC),
                TextNode(" with a ", TextType.TEXT),
                TextNode("bold block", TextType.ITALIC),
                TextNode(" word", TextType.TEXT),
                ]
        self.assertEqual(new_nodes,test_result)




if __name__ == "__main__":
    unittest.main()