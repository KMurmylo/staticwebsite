import re
from textnode import TextType,TextNode
images_pattern=r"(!\[[^\[\]]*\]\([^\(\)]*\))"
link_pattern=r"((?<!!)\[[^\[\]]*\]\([^\(\)]*\))"

def split_nodes_image(old_nodes):
    return split_node_internal(old_nodes,images_pattern,TextType.IMAGE)

def split_nodes_link(old_nodes):
    return split_node_internal(old_nodes,link_pattern,TextType.LINK)

def split_node_internal(old_nodes,pattern,text_type):
    result=[]   

    for node in old_nodes:
        if node.text_type==TextType.TEXT:
            split_result=re.split(pattern,node.text)
            for split_line in split_result:
                if len(split_line)>0:
                    if re.match(pattern,split_line)!=None:

                        split_node=re.findall( r"\[([^\[\]]*)\]\(([^\(\)]*)\)",split_line)
                        first_match = split_node[0]  # First tuple
                        result.append(TextNode(first_match[0], text_type, first_match[1]))
                    else:
                        result.append(TextNode(split_line,node.text_type))
        else:
            result.append(node)
    return result

