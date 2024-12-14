# from textnode import TextNode
from copydir import copy_source_to_dest
from generatepage import generate_page

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

    # Generate the HTML page from the markdown source file:
    generate_page("content/index.md", "template.html", "public/index.html")

main()