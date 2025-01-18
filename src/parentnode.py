
from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self,tag,children,props=None):
        super().__init__(tag,None,children,props)
    
    def to_html(self):
        if self.tag==None:
            raise ValueError("No tag")
        if self.children==None:
            raise ValueError("No children list")
        if not self.children:
            raise ValueError("Empty children list")
        child_string=""
        for child in self.children:
            child_string+=child.to_html()
        return f"<{self.tag}{self.props_to_html()}>{child_string}</{self.tag}>"

    
