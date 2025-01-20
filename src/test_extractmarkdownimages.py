import unittest
from extractmarkdown import extract_markdown_images,extract_markdown_links

class TestParentNode(unittest.TestCase):

    def test_basic_images(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        self.assertEqual(extract_markdown_images(text),[("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")])

    def test_basic_links(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        self.assertEqual(extract_markdown_links(text), [("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")])
    def test_links_not_images(self):
        text = "This has no links, but it does have images: ![alt](https://image.com)."
        self.assertEqual(extract_markdown_links(text),[])
    def test_extra_spaces(self):
        text = "Here's a sloppy link [ extra spaces ](  https://url-with-spaces.com  )."
        self.assertEqual(extract_markdown_links(text),[(' extra spaces ', '  https://url-with-spaces.com  ')])

    
if __name__ == "__main__":
    unittest.main()