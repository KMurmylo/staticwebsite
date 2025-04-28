from textnode import TextNode,TextType
import os
import shutil
import sys
from generatepage import generate_page
from extracttitle import extract_title

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath="/"):
    for file in os.listdir(dir_path_content):
        
        if os.path.isdir(os.path.join(dir_path_content,file)):
                os.makedirs(os.path.join(dest_dir_path,file),exist_ok=True)
                generate_pages_recursive(os.path.join(dir_path_content,file),template_path, os.path.join(dest_dir_path,file),basepath)
        if os.path.isfile(os.path.join(dir_path_content,file)):
            if file.endswith(".md"):
                generate_page(os.path.join(dir_path_content,file), template_path, os.path.join(dest_dir_path,file).rstrip("md")+"html",basepath)

    
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
    
    if os.path.exists("docs"):
        shutil.rmtree("docs")
    os.mkdir("docs")

    copyall("static","docs")
    
    if len(sys.argv) >= 2:
     basepath = sys.argv[1]
    else:
        basepath = "/"

    generate_pages_recursive("content", "template.html", "docs", basepath)
    #generate_page("content/index.md","template.html","public/index.html")
    return

main()

