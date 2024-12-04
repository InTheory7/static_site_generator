from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    # For each node in the list of old_nodes:
    for node in old_nodes:
        # Check that the node is actually a TextNode:
        if not isinstance(node, TextNode):
            raise Exception("Input node is not a TextNode")
        
        match node.text_type:
            # Only attempt splits on NORMAL type TextNodes:
            case TextType.NORMAL:
                split_node = []
                # Split the text data using the delimiter:
                split_str = node.text.split(delimiter)
                # If there's an even number of strings, there can't
                # be a closing delimiter, so raise an error:
                if len(split_str) % 2 == 0:
                    raise Exception("Invalid Markdown syntax: missing closing delimiter")
                # Create a TextNode for each block (The first split string is
                # always plain text, the next is always the one to apply text_type
                # to, and the third is always regular text, etc.):
                for string_num in range(0,len(split_str)):
                    if string_num % 2 == 0: # If this is an even numbered split string:
                        split_node.extend([TextNode(split_str[string_num], TextType.NORMAL)])
                    elif string_num % 2 == 1: # If it's an odd numbered split string:
                        split_node.extend([TextNode(split_str[string_num], text_type)])
                new_nodes.extend(split_node) # Should this be [split_node] or split_node

            # Otherwise, pass the old node into the new node list:
            case _:
                new_nodes.extend([node]) # Should this be [node] or just node?
                
    return new_nodes