import unittest

from htmlnode import HTMLNode

class TestTextNode(unittest.TestCase):

    def test_singleprop(self):
        html=HTMLNode(props={"href": "https://www.someweirdwebsite.com",})
        self.assertEqual(html.props_to_html()," href=\"https://www.someweirdwebsite.com\"")

    def test_noprops(self):
        html=HTMLNode()
        self.assertEqual(html.props_to_html(),"")

    def test_multipleprops(self):
        html=HTMLNode(props={"href": "https://www.google.com","target": "_blank",})
        self.assertEqual(html.props_to_html()," href=\"https://www.google.com\" target=\"_blank\"")
        
        
        

if __name__ == "__main__":
    unittest.main()