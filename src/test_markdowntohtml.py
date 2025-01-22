import unittest

from markdowntoblocks import markdown_to_blocks
from markdowntohtml import markdown_to_html_node

class MarkdownTest(unittest.TestCase):
    def test_eq1(self):
        input="""# Welcome to My Page

This is a paragraph describing my **awesome** page. Here's a list of what you'll find:

## Table of Contents
1. Introduction
2. Features
3. Conclusion

### Features
- **Bold** text
- *Italic* text
- `Code snippets`
- A [link](https://boot.dev)

> "Knowledge is power." - Bacon

#### Code Block Example"""
        #markdown_to_html_node(input)
        self.assertEqual(1,1)
    def test_2(self):
        input="""# A Heading
A paragraph."""
        #print(markdown_to_html_node(input))

    def test_3(self):
        #input="This is a paragraph with **bold** and *italic* text."
        input="""# Main heading

This is a paragraph with **bold** text.

> A quote with *italic* text

- List item 1
- List item 2 with **bold**

```
def hello():
    print("Hi!")```"""
        input2="""1. First item
2. Second item with **bold**"""
        print(markdown_to_html_node(input2))



if __name__ == "__main__":
    unittest.main()