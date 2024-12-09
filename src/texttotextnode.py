from textnode import TextNode
from splitbydelimiter import split_nodes_delimiter, split_nodes_image, split_nodes_link

def text_to_textnode(text):
    # Make sure the input is a string:
    if isinstance(text, TextNode):
        raise Exception("Input should be a string, not a TextNode")
    if isinstance(text, list):
        raise Exception("Input should be a string not a list")
    if not isinstance(text, str):
        raise Exception("Input must be a string")
    # Create old_node list from Markdown text:
    old_node = [
        TextNode(text, "normal")
    ]

    # Check bold before italic (same delimiter)
    bold_nodes = split_nodes_delimiter(old_node, "**", "bold")
    # Check italic next
    it_nodes = split_nodes_delimiter(bold_nodes, "*", "italic")
    # Check code next
    code_nodes = split_nodes_delimiter(it_nodes, "`", "code")
    # Check link next
    link_nodes = split_nodes_link(code_nodes)
    # Check image last:
    final_nodes = split_nodes_image(link_nodes)

    return final_nodes