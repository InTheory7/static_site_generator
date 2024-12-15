# from textnode import TextNode
from copydir import copy_source_to_dest
from generatepage import generate_pages_recursive

def main():
    ### # Create an example TextNode:
    ### example_textNode = TextNode("Here's some text", "bold", "https://www.boot.dev")
    ### # Print the example:
    ### print(example_textNode)

    # Source and destination of the generated webpage content:
    source = "static"
    dest = "public"
    # Copy the content to public:
    dest_objects = copy_source_to_dest(source, dest, live_print=False)
    # print(dest_objects)

    # Generate the HTML pages from the markdown source folder:
    content_dir = "content"
    template_path = "template.html"
    dest_dir = "public"
    generate_pages_recursive(content_dir, template_path, dest_dir)

main()