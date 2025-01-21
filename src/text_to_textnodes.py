from splitnodesdelimiter import split_nodes_delimiter
from textnode import TextType,TextNode
from splitnodesIL import split_nodes_image,split_nodes_link

def text_to_textnodes(text):

    result=split_nodes_delimiter([TextNode(text,TextType.TEXT)],"**",TextType.BOLD)
    result=split_nodes_delimiter(result,"*",TextType.ITALIC)
    result=split_nodes_delimiter(result,"`",TextType.CODE)
    result=split_nodes_image(result)
    result=split_nodes_link(result)
    return result