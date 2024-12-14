from htmlnode import markdown_to_html_node
from extracttitle import extract_title
from os import path, mkdir
from shutil import rmtree

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
    if path.exists(dest_path):
        rmtree(dest_path)

    # Save html_page to a file with dest_path as the file name:
    f = open(dest_path, "x")
    f.write(html_page)
    f.close()
