from textnode import TextType

class HTMLNode:
    # All data member is optional (no tag means just render as text, no 'value' will be
    # assumed to have children, no children will be assumed to have a 'value', no props
    # simply won't have any attributes
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag # HTML tag string
        self.value = value # Contents of HTML tag (like text in paragraph)
        self.children = children # List of HTMLNode objects representing the children of this node
        self.props = props # Dictionary of the attributes of the HTML tag (e.g. {"href": "google.com"})

    # Child classes will override this method to render themselves as HTML:
    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        str_to_return = ""
        if isinstance(self.props, dict):
            # For each key-value pair in the properties data member, add to the HTML tag attributes string:
            for k in self.props:
                # Not sure if you can add an f-string to a string:
                str_to_return += f" {k}=\"{self.props[k]}\""
        return str_to_return
    
    def __repr__(self):
        # The string representation of some of these (like the dictionary) might need to be changed:
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"
    
class LeafNode(HTMLNode):
    def __init__(self, tag, value, children=None, props=None):
        if children != None:
            raise Exception("LeafNode cannot have any children.")
        super().__init__(tag, value, children, props)

    def to_html(self):
        if self.value == None:
            raise ValueError("LeafNode is mmissing a 'value'")
        output_str = ""
        if self.tag == None:
            # Return value as raw text
            output_str += str(self.value)
        else:
            output_str += f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
        return output_str
    
class ParentNode(HTMLNode):
    # tag and children are non-optional and it doesn't take a 'value':
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)
        if self.value != None:
            raise Exception("ParentNode cannot have a 'value'")
        
    def to_html(self):
        if self.tag == None:
            raise ValueError("ParentNode is missing a tag")
        elif len(self.children) == 0:
            raise ValueError("ParentNode is missing children")
        
        def create_ParentNode_string(current_node, current_string=""):
            # If the current node is a LeafNode:
            if isinstance(current_node, LeafNode):
                # Use the LeafNode's own to_html method to get its string:
                return current_node.to_html()

            # If the current node is a ParentNode:
            elif isinstance(current_node, ParentNode):
                current_string = ""
                # Loop through each of the ParentNode's children and call the
                # function again on each. Add the strings together:
                for child_node in current_node.children:
                    current_string += create_ParentNode_string(child_node, current_string)
                # Encapsulate the returned string in the ParentNode's data in the
                # same way a LeafNode works with the 'value' replaced with the
                # current string:
                return f"<{current_node.tag}{current_node.props_to_html()}>{current_string}</{current_node.tag}>"

        return create_ParentNode_string(self)

def text_node_to_html_node(text_node):
    match text_node.text_type:
        case TextType.NORMAL:
            return LeafNode(tag=None, value=text_node.text)
        case TextType.BOLD:
            return LeafNode(tag="b", value=text_node.text)
        case TextType.ITALIC:
            return LeafNode(tag="i", value=text_node.text)
        case TextType.CODE:
            return LeafNode(tag="code", value=text_node.text)
        case TextType.LINK:
            return LeafNode(tag="a", value=text_node.text, children=None, props={"href": text_node.url})
        case TextType.IMAGE:
            return LeafNode(tag="img", value="", children=None, props={"src": text_node.url, "alt": text_node.text})
        
from splitblocks import markdown_to_blocks, block_to_block_type
from texttotextnode import text_to_textnode

def markdown_to_html_node(markdown):
    # Convert from a block of text to children HTMLNodes based
    # on the inline text contained within:
    def text_to_children(block):
        # Create TextNodes from a single block of text:
        block_TextNodes = text_to_textnode(block)
        # Convert TextNodes to HTMLNodes:
        block_HTMLNodes = []
        for node in block_TextNodes:
            block_HTMLNodes.append(text_node_to_html_node(node))
        # Return a list of HTMLNodes:
        return block_HTMLNodes
    
    # Format heading text and level:
    def format_heading(block):
        # Count the heading level from the number of '#' at the start
        heading_level = 0
        for char in block:
            if char == "#":
                heading_level += 1
            else:
                break
        # Remove the '#' and return the heading string
        return heading_level, block[(heading_level+1):]
    
    # Format code blocks:
    def format_code(block):
        # Remove the three start and end backticks (which, if this is
        # already formatted as valid code, will be the first and last
        # characters in the string:
        new_block = block[3:]
        return new_block[:-3]
    
    # Format quote blocks:
    def format_quote(block):
        # Remove the > from each line within the block
        # Split the block at newlines:
        lines = block.split("\n")
        new_lines = []
        for line in lines:
            new_lines.append(line[1:])
        return "\n".join(new_lines)
    
    # Format unordered lists and convert to child HTMLNodes for each line
    def format_unordered_list(block):
        # Remove the first two characters from each line:
        lines = block.split("\n")
        new_lines = []
        for line in lines:
            new_lines.append(line[2:])
        # Now create a list of HTMLNodes, one for each line:
        child_nodes = []
        for line in new_lines:
            child_nodes.append(HTMLNode(tag="li", value=line))
        return child_nodes
    
    # Format ordered lists and convert to child HTMLNodes for each line:
    def format_ordered_list(block):
        # Remove a variable number of characters from the start of each line:
        lines = block.split("\n")
        new_lines = []
        line_count = 0
        for line in lines:
            line_count += 1
            line_count_length = int(line_count/10) + 1 + 2
            new_lines.append(line[line_count_length:])
        # Create a list of HTMLNodes, one for each line:
        child_nodes = []
        for line in new_lines:
            child_nodes.append(HTMLNode(tag="li", value=line))
        return child_nodes




    # Check that the input markdown is a string:
    if not isinstance(markdown, str):
        raise Exception("Input must be a string")

    # Split the input markdown into blocks, using the
    # function already created for that:
    blocks = markdown_to_blocks(markdown)

    # Initialise the nodes for each block:
    block_nodes = []
    # Loop over each block and create a HTMLNode for each:
    for block in blocks:
        # Determine the type of block (options are normal, heading, code,
        # quote, unordered_list, ordered_list):
        block_type = block_to_block_type(block)

        # Depending on the block type, create ParentNodes:
        block_children = text_to_children(block)
        match block_type:
            case "normal":
                block_node = HTMLNode(tag="p", children=block_children)
            case "heading":
                heading_level, heading_text = format_heading(block)
                block_node = HTMLNode(tag=f"h{heading_level}", value=heading_text)
            case "code":
                code_text = format_code(block)
                block_node = HTMLNode(tag="pre", children=HTMLNode(tag="code",value=code_text))
            case "quote":
                quote_text = format_quote(block)
                block_node = HTMLNode(tag="blockquote", value=quote_text)
            case "unordered_list":
                child_nodes = format_unordered_list(block)
                block_node = HTMLNode(tag="ul", children=child_nodes)
            case "ordered_list":
                child_nodes = format_ordered_list(block)
                block_node = HTMLNode(tag="ol", children=child_nodes)

        # Add each block's node to the list of nodes for all blocks:
        block_nodes.append([block_node])

    # Surround the block_nodes in a 'div' HTMLNode:
    return HTMLNode(tag="div", children=block_nodes)

    