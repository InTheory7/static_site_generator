# from textnode import TextNode
from copydir import copy_source_to_dest

def main():
    ### # Create an example TextNode:
    ### example_textNode = TextNode("Here's some text", "bold", "https://www.boot.dev")
    ### # Print the example:
    ### print(example_textNode)

    source = "static"
    dest = "public"

    dest_objects = copy_source_to_dest(source, dest, live_print=False)
    # print(dest_objects)

main()