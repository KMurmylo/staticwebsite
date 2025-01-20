import re
from textnode import TextNode,TextType

def extract_markdown_images(text):
    finder=r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matches=re.findall(finder,text)
    return matches

def extract_markdown_links(text):
    finder=r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matches=re.findall(finder,text)
    return matches

#text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
