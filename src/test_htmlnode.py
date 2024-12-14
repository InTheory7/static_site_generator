import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode, text_node_to_html_node, markdown_to_html_node
from textnode import TextNode

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

class TestParentNode(unittest.TestCase):
    # Test a ParentNode with one LeafNode:
    def test_singleParent(self):
        tag = "p"
        children = [LeafNode("a", "This is a link.", props={"href": "www.google.com"})]
        node = ParentNode(tag, children)
        print(f"ParentNode: {node}")
        # Test the props_to_html method:
        self.print_props_to_html_output(node)
        # Test the .to_html() method:
        print(f"ParentNode '.to_html' output: {node.to_html()}\n")

    # Test a ParentNode with another ParentNode inside which contains one LeafNode:
    def test_nestedParent(self):
        tag1 = "p"
        tag2 = "i"
        children = [LeafNode("a", "This is a link.", props={"href": "www.google.com"})]
        node2 = ParentNode(tag1, children) # Nested ParentNode
        node = ParentNode(tag2, [node2]) # Outer ParentNode
        print(f"ParentNode: {node}")
        # Test the props_to_html method:
        self.print_props_to_html_output(node)
        # Test the .to_html() method:
        print(f"ParentNode '.to_html' output: {node.to_html()}\n")

    # Test a ParentNode containing two ParentNodes at the same level, each with a LeafNode:
    def test_nestedDoubleParent(self):
        tag1 = "p"
        tag2 = "i"
        children1 = [
            LeafNode("a", "This is link No. 1", props={"href": "www.google.com"}),
            LeafNode("a", "This is link No. 2", props={"href": "www.dontDuplicate.org"}),
        ]
        children2 = [
            LeafNode("a", "This is also a link in a different Parent.", props={"href": "boot.dev", "target": "_All"})
        ]
        node2 = ParentNode(tag1, children1) # Nested ParentNode
        node1 = ParentNode(tag2, [node2]) # Outer ParentNode1
        node3 = ParentNode(tag1, children2) # Outer ParentNode2
        node = ParentNode(tag2, [node1, node3])
        print(f"ParentNode: {node}")
        # Test the props_to_html method:
        self.print_props_to_html_output(node)
        # Test the .to_html() method:
        print(f"ParentNode '.to_html' output: {node.to_html()}\n")

    # Test three LeafNodes in a single ParentNode without nesting:
    def test_multipleLeaves(self):
        parentTag = "p"
        children = [
            LeafNode("b", "Text 1"),
            LeafNode("i", "Text 2"),
            LeafNode("c", "Text 3"),
        ]
        node = ParentNode(parentTag, children)
        print(f"ParentNode: {node}")
        # Test the props_to_html method:
        self.print_props_to_html_output(node)
        # Test the .to_html() method:
        print(f"ParentNode '.to_html' output: {node.to_html()}\n")

    # Same as the last test but buried under one nested ParentNode:
    def test_multipleLeavesInOneNest(self):
        parentTag1 = "p"
        parentTag2 = "h1"
        children = [
            LeafNode("b", "Text 1"),
            LeafNode("i", "Text 2"),
            LeafNode("c", "Text 3"),
        ]
        node1 = ParentNode(parentTag1, children)
        node = ParentNode(parentTag2, [node1])
        print(f"ParentNode: {node}")
        # Test the props_to_html method:
        self.print_props_to_html_output(node)
        # Test the .to_html() method:
        print(f"ParentNode '.to_html' output: {node.to_html()}\n")

    # Test a ParentNode with no children (this should fail):
    ### def test_noChildren(self):
    ###     node = ParentNode("p", [])
    ###     print(f"ParentNode: {node}")
    ###     # Test the props_to_html method:
    ###     self.print_props_to_html_output(node)
    ###     # Test the .to_html() method:
    ###     print(f"ParentNode '.to_html' output: {node.to_html()}\n")
    # ^ The above test fails as expected.

    # Create a method to print the props_to_html output which is used in all of the above tests:
    def print_props_to_html_output(self, node):
        print(f"props_to_html output: {node.props_to_html()}\n")

class TestTextNodeToHTMLNodeFunc(unittest.TestCase):
    # Convert plain text:
    def test_plainText(self):
        node = text_node_to_html_node(TextNode(text="This should show as plain text.", text_type="normal"))
        print(f"TextNode to LeafNode: {node}")
        # Test the props_to_html method:
        self.print_props_to_html_output(node)
        # Test the .to_html() method:
        print(f"LeafNode '.to_html' output: {node.to_html()}\n")
    # Convert bold text:
    def test_boldText(self):
        node = text_node_to_html_node(TextNode(text="This should be bold text.", text_type="bold"))
        print(f"TextNode to LeafNode: {node}")
        # Test the props_to_html method:
        self.print_props_to_html_output(node)
        # Test the .to_html() method:
        print(f"LeafNode '.to_html' output: {node.to_html()}\n")
    # Convert italic text:
    def test_italicText(self):
        node = text_node_to_html_node(TextNode(text="This should be italic.", text_type="italic"))
        print(f"TextNode to LeafNode: {node}")
        # Test the props_to_html method:
        self.print_props_to_html_output(node)
        # Test the .to_html() method:
        print(f"LeafNode '.to_html' output: {node.to_html()}\n")
    # Convert code text:
    def test_codeText(self):
        node = text_node_to_html_node(TextNode(text="This should show as code.", text_type="code"))
        print(f"TextNode to LeafNode: {node}")
        # Test the props_to_html method:
        self.print_props_to_html_output(node)
        # Test the .to_html() method:
        print(f"LeafNode '.to_html' output: {node.to_html()}\n")
    # Convert link text:
    def test_linkText(self):
        node = text_node_to_html_node(TextNode(text="This is a link.", text_type="link", url="www.google.com"))
        print(f"TextNode to LeafNode: {node}")
        # Test the props_to_html method:
        self.print_props_to_html_output(node)
        # Test the .to_html() method:
        print(f"LeafNode '.to_html' output: {node.to_html()}\n")
    # Convert image text:
    def test_imageText(self):
        node = text_node_to_html_node(TextNode(text="This is alt text", text_type="image", url="public/test_image.jpg"))
        print(f"TextNode to LeafNode: {node}")
        # Test the props_to_html method:
        self.print_props_to_html_output(node)
        # Test the .to_html() method:
        print(f"LeafNode '.to_html' output: {node.to_html()}\n")

    def print_props_to_html_output(self, node):
        print(f"props_to_html output: {node.props_to_html()}")

class TestMarkdownToHTMLNodeFunc(unittest.TestCase):
    # Pass in an empty string:
    def test_01emptyString(self):
        markdown = ""
        print(f"\n\n\n\n--- markdown_to_html_node() output ---\n\n{markdown_to_html_node(markdown)}")

    # Pass in a single line:
    def test_02singleLine(self):
        markdown = "Here's an example line of plain text."
        print(markdown_to_html_node(markdown))

    # Pass in a multi-line paragraph:
    def test_03multiLine(self):
        markdown = """
This is the first line of a multi-line paragraph of plain text.
Here's the next line.
And the final line."""
        print(markdown_to_html_node(markdown))

    # Pass in a multi-line paragraph with inline markdown:
    def test_04multiLineWithMarkdown(self):
        markdown = """
The first line contains some *italics* and a **bold** bit of text.
The next line has some `code in it`.
And the final line has a [link](www.exampleLine.com) and an embedded image: ![Image alt text](imageURL.png)"""
        print(markdown_to_html_node(markdown))

    # Pass in a heading:
    def test05_heading(self):
        markdown = "# This is a level 1 heading"
        print(markdown_to_html_node(markdown))

    # Pass in a lower level heading:
    def test06_lowerHeading(self):
        markdown = "#### This is a level 4 heading"
        print(markdown_to_html_node(markdown))

    # Pass in an invalidly low heading:
    def test07_invalidHeading(self):
        markdown = "########## This is a level X? heading"
        print(markdown_to_html_node(markdown))

    # Pass in a code block:
    def test08_codeBlock(self):
        markdown = """```Here's a multi-line code block.
With this being the second line.
And this the third.```"""
        print(markdown_to_html_node(markdown))

    # Repeat the above but with indentation within the multi-line string:
    def test09_codeBlockWithIndents(self):
        markdown = """```Here's a multi-line code block.
        With this being the second line.
        And this the third.```"""
        print(markdown_to_html_node(markdown))
    # ^ This runs but doesn't format correctly without deleting whitespace at the start.

    # Pass in a quote:
    def test10_quoteBlock(self):
        markdown = """>Each line of this quote
>Starts with a '>' character.
>But who said it?"""
        print(markdown_to_html_node(markdown))

    # Pass in a quote with indents *before* the >:
    def test11_quoteBlockWithIndent(self):
        markdown = """>Each line of this quote
        >Starts with a '>' character.
        >But who said it?"""
        print(markdown_to_html_node(markdown))
        # ^ This runs but doesn't format correctly without deleting whitespace at the start.

    # Repeat the above but with spaces after the >:
    def test12_quoteBlockWithSpaces(self):
        markdown = """> Each line of this quote
> Starts with a '>' character.
> But who said it?"""
        print(markdown_to_html_node(markdown))
        # ^ This runs but doesn't format correctly without deleting whitespace at the start.

    # Pass in an unordered list:
    def test13_unorderedList(self):
        markdown = """- List item 1
- List item 2
- List item 3"""
        print(markdown_to_html_node(markdown))

    # Pass in an ordered list:
    def test14_orderedList(self):
        markdown = """1. List item 1
2. List item 2
3. List item 3
4. List item 4
5. 5
6. 6
7. 7
8. 8
9. 9
10. List item 10!"""
        print(markdown_to_html_node(markdown))

    # Pass in an incorrectly numbered ordered list:
    def test15_incorrectOrderedList(self):
        markdown = """1. List item 1
3. List item 2
4. List item 3"""
        print(markdown_to_html_node(markdown))

    def test_printNewLines(self):
        print("\n\n\n")

if __name__ == "__main__":
    unittest.main()