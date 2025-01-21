import unittest
from markdowntoblocks import markdown_to_blocks


class TestMarkdownToBlock(unittest.TestCase):
    def test_eachline(self):
        markdown = """# This is a heading

        This is a paragraph of text. It has some **bold** and *italic* words inside of it.

* This is the first list item in a list block
* This is a list item
* This is another list item"""

        blocks = markdown_to_blocks(markdown)
    
        # Test   first block (heading)
        assert blocks[0] == "# This is a heading"
        
        # Test second block (paragraph)
        assert blocks[1] == "This is a paragraph of text. It has some **bold** and *italic* words inside of it."
        
        # Test third block (list)
        assert blocks[2] == """* This is the first list item in a list block
* This is a list item
* This is another list item"""

        # Test the number of blocks
        assert len(blocks) == 3

    def test_example(self):
        input="""# This is a heading

This is a paragraph of text. It has some **bold** and *italic* words inside of it.

* This is the first list item in a list block
* This is a list item
* This is another list item"""
        self.assertEqual(markdown_to_blocks(input),["# This is a heading",
"This is a paragraph of text. It has some **bold** and *italic* words inside of it."
,
"""* This is the first list item in a list block
* This is a list item
* This is another list item"""])


if __name__ == "__main__":
    unittest.main()