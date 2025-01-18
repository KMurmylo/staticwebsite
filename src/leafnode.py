from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag, value,  input_props=None ):
        super().__init__(tag,value,props=input_props)
        if value==None:
            raise ValueError



    def to_html(self):
        if self.tag==None:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"