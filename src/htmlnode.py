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