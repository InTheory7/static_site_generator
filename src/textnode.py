from enum import Enum

# TextType enum which is used in the TextNode class
class TextType(Enum):
    NORMAL = "normal"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"

# TextNode class which contains information about inline text
class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text # The actual body of the text itself
        self.text_type = TextType(text_type) # What format (TextType enum) it should be in
        self.url = url # A link for regular links or images

    # Check that two TextNodes are equal by seeing if all of their properties are equal
    # (this might not work yet)
    def __eq__(self, other_TextNode):
        if self == other_TextNode:
            return True
        else:
            return False
    
    # Create the string representation of this TextNode class, so it displays correctly
    # when print() is used elsewhere
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"