import unittest
from splitnodesIL import split_nodes_image,split_nodes_link
from textnode import TextNode,TextType

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode(
         "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
        TextType.TEXT,
        )
        self.assertEqual(split_nodes_link([node]),[
            TextNode("This is text with a link ", TextType.TEXT),
            TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
            TextNode(" and ", TextType.TEXT),
            TextNode(
            "to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev"
                ),
             ])


if __name__ == "__main__":
    unittest.main()