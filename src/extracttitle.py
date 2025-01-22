import re

def extract_title(markdown):
    for line in markdown.split("\n"):
        match=re.match(r"^# (.*)",markdown)
        if match:
            return match.group(1).strip()    
    raise Exception("No header found")
    
