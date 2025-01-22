from textnode import TextNode,TextType
import os
import shutil
from generatepage import generate_page
from extracttitle import extract_title

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    for file in os.listdir(dir_path_content):
        
        if os.path.isdir(os.path.join(dir_path_content,file)):
                os.makedirs(os.path.join(dest_dir_path,file),exist_ok=True)
                generate_pages_recursive(os.path.join(dir_path_content,file),template_path, os.path.join(dest_dir_path,file))
        if os.path.isfile(os.path.join(dir_path_content,file)):
            if file.endswith(".md"):
                generate_page(os.path.join(dir_path_content,file), template_path, os.path.join(dest_dir_path,file).rstrip("md")+"html")

    
def copyall(src,dst):
    for file in os.listdir(src):
        if os.path.isdir(os.path.join(src,file)):
                os.makedirs(os.path.join(dst,file))
                copyall(os.path.join(src,file),os.path.join(dst,file))
        if os.path.isfile(os.path.join(src,file)):
            shutil.copy(os.path.join(src,file),(os.path.join(dst,file)))

def main():
    textnode=TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev")
    print(textnode)
    
    if os.path.exists("public"):
        shutil.rmtree("public")
    os.mkdir("public")

    copyall("static","public")
    generate_pages_recursive("content","template.html","public")
    #generate_page("content/index.md","template.html","public/index.html")
    return

main()

