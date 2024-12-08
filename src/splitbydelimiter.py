from textnode import TextNode, TextType
from extractlinks import extract_markdown_images, extract_markdown_links
from math import floor

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

def split_nodes_image(old_nodes):
    new_nodes = []
    # For each node in the list of old_nodes:
    for node in old_nodes:
        # Check that the node is actually a TextNode:
        if not isinstance(node, TextNode):
            raise Exception("Input node is not a TextNode")
        
        match node.text_type:
            # Only attempt splits on NORMAL type TextNodes:
            case TextType.NORMAL:
                # Use the extraction function to pull out the image text:
                md_image_data = extract_markdown_images(node.text)
                # If there are no images:
                if len(md_image_data) == 0:
                    new_nodes.extend([node])
                # If there is atleast one image:
                else:
                    split_node = []
                    # For the first image, split into 'before' and 'after' the image,
                    # then for the second, do the same split on the 'after' text
                    # section of the first image, and repeat for however many images
                    # there are, appending the new 'before' and after' to the list
                    # each time:
                    text_sections = []
                    for image_index in range(0,len(md_image_data)):
                        image = md_image_data[image_index]
                        alt_text = image[0]
                        url = image[1]
                        # If this is the first image, split the entire string, otherwise,
                        # split the part after the last image:
                        if image_index == 0:
                            text_to_split = node.text
                        else:
                            text_to_split = text_sections[-1]
                        per_image_text_sections = text_to_split.split(f"![{alt_text}]({url})", 1)
                        # Add the first section to text_sections, or overwrite if this isn't
                        # the first image (nor sure I need the if-else-statement for this):
                        if image_index == 0:
                            text_sections.extend([per_image_text_sections[0]])
                        else:
                            text_sections[-1] = per_image_text_sections[0]
                        # Add the image text to text_sections:
                        text_sections.extend([f"![{alt_text}]({url})"])
                        # Add the final section to text_sections:
                        text_sections.extend([per_image_text_sections[1]])

                    # Now use text_sections to create the TextNodes:
                    for section_index in range(0,len(text_sections)):
                        # If the section index is even (0, 2, 4, etc), then it is plain text:
                        if not (section_index % 2):
                            # Only append if the text string isn't empty:
                            if text_sections[section_index]:
                                split_node.extend([TextNode(text_sections[section_index], TextType.NORMAL)])
                        # If the section index is odd (1, 3, 5, etc), then it is an image:
                        else:
                            image_index = int(floor(section_index/2))
                            alt_text = md_image_data[image_index][0]
                            url = md_image_data[image_index][1]
                            split_node.extend([TextNode(alt_text, TextType.IMAGE, url)])
                    
                    new_nodes.extend(split_node)

            case _:
                new_nodes.extend([node])

    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
    # For each node in the list of old_nodes:
    for node in old_nodes:
        # Check that the node is actually a TextNode:
        if not isinstance(node, TextNode):
            raise Exception("Input node is not a TextNode")
        
        match node.text_type:
            # Only attempt splits on NORMAL type TextNodes:
            case TextType.NORMAL:
                # Use the extraction function to pull out the link text:
                md_link_data = extract_markdown_links(node.text)
                # If there are no links:
                if len(md_link_data) == 0:
                    new_nodes.extend([node])
                # If there is atleast one link:
                else:
                    split_node = []
                    # For the first link, split into 'before' and 'after' the link,
                    # then for the second, do the same split on the 'after' text
                    # section of the first link, and repeat for however many links
                    # there are, appending the new 'before' and after' to the list
                    # each time:
                    text_sections = []
                    for link_index in range(0,len(md_link_data)):
                        link = md_link_data[link_index]
                        anchor_text = link[0]
                        url = link[1]
                        # If this is the first link, split the entire string, otherwise,
                        # split the part after the last link:
                        if link_index == 0:
                            text_to_split = node.text
                        else:
                            text_to_split = text_sections[-1]
                        per_link_text_sections = text_to_split.split(f"[{anchor_text}]({url})", 1)
                        # Add the first section to text_sections, or overwrite if this isn't
                        # the first link (nor sure I need the if-else-statement for this):
                        if link_index == 0:
                            text_sections.extend([per_link_text_sections[0]])
                        else:
                            text_sections[2*link_index] = per_link_text_sections[0]
                        # Add the link text to text_sections:
                        text_sections.extend([f"[{anchor_text}]({url})"])
                        # Add the final section to text_sections:
                        text_sections.extend([per_link_text_sections[1]])
                    
                    # Now use text_sections to create the TextNodes:
                    for section_index in range(0,len(text_sections)):
                        # If the section index is even (0, 2, 4, etc), then it is plain text:
                        if not (section_index % 2):
                            # Only append if the text string isn't empty:
                            if text_sections[section_index]:
                                split_node.extend([TextNode(text_sections[section_index], TextType.NORMAL)])
                        # If the section index is odd (1, 3, 5, etc), then it is an image:
                        else:
                            link_index = int(floor(section_index/2))
                            anchor_text = md_link_data[link_index][0]
                            url = md_link_data[link_index][1]
                            split_node.extend([TextNode(anchor_text, TextType.LINK, url)])
                    
                    new_nodes.extend(split_node)

            case _:
                new_nodes.extend([node])
                
    return new_nodes