import unittest
from htmlnode import HTMLNode

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
        
    # Create a method to print the props_to_html output which is used in all of the above tests:
    def print_props_to_html_output(self, node):
        print(f"props_to_html output: {node.props_to_html()}\n")

        
if __name__ == "__main__":
    unittest.main()