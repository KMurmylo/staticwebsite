


def markdown_to_blocks(markdown):
    result=[]
    block=""
    for line in markdown.split("\n"):
        line=line.strip()
        if len(line)==0:
            if len(block)>0:
                result.append(block)
            block=""
        else:
            if len(block)>0:
                block+="\n"
            block+=line
            
    if len(block)>0:
                result.append(block)

    return result