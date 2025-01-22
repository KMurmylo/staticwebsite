import os
from markdowntohtml import markdown_to_html_node
from extracttitle import extract_title

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    with open(from_path, 'r',encoding="utf-8") as f:
        source=f.read()

    with open(template_path,'r', encoding="utf-8") as f:
        template=f.read()

    page=markdown_to_html_node(source)
    title=extract_title(source)
    result=template.replace("{{ Title }}",title)
    result=result.replace("{{ Content }}",page.to_html())
    with open(dest_path, 'w',encoding="utf-8") as f:
        f.write(result)
