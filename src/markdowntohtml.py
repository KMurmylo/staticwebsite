from markdowntoblocks import markdown_to_blocks
from parentnode import ParentNode
from text_to_textnodes import text_to_textnodes
from blocktoblocktype import block_to_block_type
from htmlnode import HTMLNode
from textnode import TextType
import re
from conversion import text_node_to_html_node
from leafnode import LeafNode

def markdown_to_html_node(markdown):
    children=[]
    result=ParentNode("div",children)

    blocks=markdown_to_blocks(markdown)
    for block in blocks:  
        children.append(process_block(block,block_to_block_type(block)))
        
    return result

def process_block(block,blocktype):
    print(f"Block content: '{block}'\nBlock lines: {repr(block)}")
    match blocktype:
        case "heading":
            level=len(re.match(r"^([#]+)",block).group(1))
            tag = f"h{level}"
            clean_block = block.lstrip('#').strip()
            #return f"<{tag}>{text_to_children(clean_block)}</{tag}>"
            return HTMLNode(tag, text_to_children(clean_block))
        case "code":
            #code_text = re.sub(r'^```[\w]*\n|```$', '', block)
            code_text = re.sub(r'^```|```$', '', block).strip()
            code_node = HTMLNode("code", [LeafNode(None, code_text)])
            return HTMLNode("pre", [code_node])
        case "quote":
            clean_block=block.lstrip('>').strip()
            return HTMLNode("blockquote", text_to_children(clean_block))
        case "paragraph":
            return HTMLNode("p", text_to_children(block))
        case "unordered_list":

            items = block.split('\n')
            list_items=[]
            for item in items:
                item=item.lstrip('-*').strip()
                list_items.append(HTMLNode("li", text_to_children(item)))
            
            return HTMLNode("ul", list_items)
        case "ordered_list":
            items = block.split('\n')
            list_items=[]
            for item in items:
                item = re.sub(r'^\d+\.\s*', '', item.strip())
                list_items.append(HTMLNode("li", text_to_children(item)))
            return HTMLNode("ol",list_items)



def text_to_children(text):
    text_nodes = text_to_textnodes(text)  # This converts text to TextNodes
    for node in text_nodes:# Now convert each TextNode to an HTMLNode
        pass
    return [text_node_to_html_node(node) for node in text_nodes]

