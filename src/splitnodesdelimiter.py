from textnode import TextNode,TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    result=[]
    for node in old_nodes:
        if node.text_type==TextType.TEXT:
            split_nodes=node.text.split(delimiter)
            if len(split_nodes)>1:
                even=True
                for new_node in split_nodes:
                    if even:
                        result.append(TextNode(new_node,TextType.TEXT))
                        even=not even
                    else:
                        result.append(TextNode(new_node,text_type))
                        even= not even
            else:
                result.append(TextNode(split_nodes[0],TextType.TEXT))
        else:
            result.append(node)
    
    return result
