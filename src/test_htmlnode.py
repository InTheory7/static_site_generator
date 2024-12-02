import unittest
from htmlnode import HTMLNode, LeafNode

class TestHTMLNode(unittest.TestCase):
    # Create an HTML node with no input attributes and print the string repr:
    def test_noInputs(self):
        node = HTMLNode()
        print(node)
        # Test the props_to_html method:
        self.print_props_to_html_output(node)

    # Create an HTML node with tag and value only and print the string repr:
    def test_tagAndValueOnly(self):
        tag = "p"
        value = "Here's an example paragraph, though it's very short. Just a couple of sentences really."
        node = HTMLNode(tag, value)
        print(node)
        # Test the props_to_html method:
        self.print_props_to_html_output(node)

    # Create two HTML nodes, one to be the child of another and print the string repr:
    def test_children(self):
        tag1 = "p"
        value1 = "Here's an example paragraph, though it's very short. Just a couple of sentences really."
        node1 = HTMLNode(tag1, value1)
        tag2 = "h1"
        value2 = "This will be a heading!"
        node2 = HTMLNode(tag2, value2, [node1])
        print(node2)
        # Test the props_to_html method:
        self.print_props_to_html_output(node2)

    # Create an HTML node with props and print the string repr:
    def test_props(self):
        tag = "p"
        value = "Here's an example paragraph, though it's very short. Just a couple of sentences really."
        props = {"href": "www.google.com", "targets": "_blank"}
        kwargs = {'tag': tag, 'value': value, 'props': props}
        node = HTMLNode(**kwargs)
        print(node)
        # Test the props_to_html method:
        self.print_props_to_html_output(node)

    # Create 4 nodes, two to be double-nested children, and another to be a lone child:
    def test_children2(self):
        tag1 = "p"
        value1 = "Here's an example paragraph, though it's very short. Just a couple of sentences really."
        node1 = HTMLNode(tag1, value1, None, {"href": "www.ihopethisworks.org"})
        tag2 = "h1"
        value2 = "This will be a heading!"
        node2 = HTMLNode(tag2, value2, None, {"href": "this.betterwork.com"})
        tag3 = "p"
        value3 = "Another paragraph"
        node3 = HTMLNode(tag3, value3, [node2])
        tag4 = "p"
        value4 = "It's december now"
        node4 = HTMLNode(tag4, value4, [node1, node3])
        print(node4)
        # Test the props_to_html method:
        self.print_props_to_html_output(node4)

    # Create a node with no tag but some 'value' to print as raw text::
    def test_valueOnly(self):
        value = "This should display as plain text."
        node = HTMLNode(tag=None, value=value)
        print(node)
        # Test the props_to_html method:
        self.print_props_to_html_output(node)
        
    # Create a method to print the props_to_html output which is used in all of the above tests:
    def print_props_to_html_output(self, node):
        print(f"props_to_html output: {node.props_to_html()}\n")
        
class TestLeafNode(unittest.TestCase):
    # Test tag and value:
    def test_tagAndValue(self):
        tag = "p"
        value = "Text example"
        node = LeafNode(tag, value)
        print(f"LeafNode: {node}")
        # Test the props_to_html method:
        self.print_props_to_html_output(node)
        # Test the .to_html() method:
        print(f"LeafNode '.to_html' output: {node.to_html()}")

    # Test value with None tag (should print as plain text with .to_html()):
    def test_tagAndValue(self):
        tag = None
        value = "This should be plain text with no HTML tags!"
        node = LeafNode(tag, value)
        print(f"LeafNode: {node}")
        # Test the props_to_html method:
        self.print_props_to_html_output(node)
        # Test the .to_html() method:
        print(f"LeafNode '.to_html' output: {node.to_html()}")

    # Try to create a node with children:
    ### def test_tagAndValue(self):
    ###     tag = "p"
    ###     value = "This should be plain text with no HTML tags!"
    ###     node = LeafNode(tag, value)
    ###     node2 = LeafNode(tag, value, [node])
    ###     print(f"LeafNode: {node2}")
    ###     # Test the props_to_html method:
    ###     self.print_props_to_html_output(node2)
    ###     # Test the .to_html() method:
    ###     print(f"LeafNode '.to_html' output: {node2.to_html()}")
    # ^ This does indeed produce an error as we want.
        
    # Create a LeafNode with extra parameters:
    def test_tagAndValue(self):
        tag = "a"
        value = "This is a URL link."
        props = {"href": "example.link.com"}
        node = LeafNode(tag, value, props=props)
        print(f"LeafNode: {node}")
        # Test the props_to_html method:
        self.print_props_to_html_output(node)
        # Test the .to_html() method:
        print(f"LeafNode '.to_html' output: {node.to_html()}")

    # Create a LeafNode with two parameters:
    def test_tagAndValue(self):
        tag = "a"
        value = "This is also a URL link."
        props = {"href": "example.link.com", "target": "_all"}
        node = LeafNode(tag, value, props=props)
        print(f"LeafNode: {node}")
        # Test the props_to_html method:
        self.print_props_to_html_output(node)
        # Test the .to_html() method:
        print(f"LeafNode '.to_html' output: {node.to_html()}")

    # Create a method to print the props_to_html output which is used in all of the above tests:
    def print_props_to_html_output(self, node):
        print(f"props_to_html output: {node.props_to_html()}\n")

if __name__ == "__main__":
    unittest.main()