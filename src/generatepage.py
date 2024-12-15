from htmlnode import markdown_to_html_node
from extracttitle import extract_title
from os import path, mkdir, listdir
from shutil import rmtree
from pathlib import Path

def generate_page(from_path, template_path, dest_path):
    # Print a message while the function works:
    print(f"Generating page from {from_path} to {dest_path} using {template_path}.")

    # Read the markdown file at from_path:
    f = open(from_path)
    markdown = f.read()
    f.close()

    # Read the template file at template_path:
    f = open(template_path)
    template = f.read()
    f.close()

    # Convert the markdown file to an HTML string:
    html_string = markdown_to_html_node(markdown).to_html()

    # Extract the title from the markdown file:
    title = extract_title(markdown)

    # Replace the Title and Content placeholders in the template with the title and HTML string:
    # Title first:
    html_page = template.replace("{{ Title }}", title)
    # Content second:
    html_page = html_page.replace("{{ Content }}", html_string)

    # Save the new HTML page to a file at dest_path (creating directories if required):
    # Check if the dest_path already exists, if not, create it:
    if not path.exists(path.dirname(dest_path)):
        mkdir(path.dirname(dest_path))

    # Check if the dest_path file already exists, if it does, delete it:
    if path.exists(f"{dest_path[0:-3]}.html"):
        rmtree(f"{dest_path[0:-3]}.html")

    # Save html_page to a file with dest_path as the file name:
    f = open(f"{dest_path[0:-3]}.html", "x")
    f.write(html_page)
    f.close()

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    # Use listdir to find the files and folders in the content directory:
    content_dir = listdir(dir_path_content)
    # For each item:
    for object in content_dir:
        # Check the object type (file or dir):
        is_file = path.isfile(path.join(dir_path_content, object))
        # If the item is a markdown file, generate a HTML page from it and write to the dest
        # version of the current directory using genereate_page():
        if is_file:
            # Check the file is a markdown file:
            if object[-3:] != ".md":
                raise Exception("Input file is not .md markdown")
            # Generate a HTML page:
            generate_page(path.join(dir_path_content, object), template_path, path.join(dest_dir_path, object))
        # If the item is a folder, check whether the folder exists, if it doesn't create it 
        # with the same name in the dest path and recursively call this function again:
        else:
            # Make the directory:
            mkdir(path.join(dest_dir_path, object))
            # Recursively call the function again:
            generate_pages_recursive(path.join(dir_path_content, object), template_path, path.join(dest_dir_path, object))