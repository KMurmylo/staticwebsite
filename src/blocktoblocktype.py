import re

def block_to_block_type(block):
    if re.match(r"^#{1,6} .+", block):
        return "heading"
    if re.match(r"^```[\s\S]*```$",block):
        return "code"
    split_block=block.split("\n")
    quote_block=True
    for current_block in split_block:
        if not re.match(r"^> .+",current_block):
            quote_block=False
            break
    if quote_block:
        return "quote"
    unlist_block=True
    for current_block in split_block:
        if not re.match(r"^[*-] .+",current_block):
            unlist_block=False
            break
    if unlist_block:
        return "unordered_list"
    orlist_block=True
    i=1
    for current_block in split_block:
        
        if not re.match(fr"^{i}\. .+",current_block):
            orlist_block=False
            break
        i+=1
    if orlist_block:
        return "ordered_list"
    return "paragraph"

