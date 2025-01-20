from splitnodesdelimiter import split_nodes_delimiter
from textnode import TextType,TextNode
from splitnodesIL import split_nodes_image,split_nodes_link

def text_to_textnodes(text):
    print(text)
    print("-----")
    result=split_nodes_delimiter([TextNode(text,TextType.TEXT)],"**",TextType.BOLD)
    print(result)
    print("-----")
    result=split_nodes_delimiter(result,"*",TextType.ITALIC)
    print(result)
    print("-----")
    result=split_nodes_delimiter(result,"`",TextType.CODE)
    print(result)
    print("-----")
    result=split_nodes_image(result)
    print(result)
    
    
    print("-----")
    result=split_nodes_link(result)
    print(result)
    print("-----")
    return result