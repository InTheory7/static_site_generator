import unittest
from splitbydelimiter import split_nodes_delimiter
from textnode import TextNode, TextType

class TestDelimiterSplit(unittest.TestCase):
    # Pass in a string with no delimiters to check:
    def test_plainText(self):
        old_nodes = [
            TextNode("No delimiters here", "normal"),
        ]
        delimiter = "*"
        text_type = "italic"
        print(split_nodes_delimiter(old_nodes, delimiter, text_type))

    # Pass in a string with a different delimiter than provided:
    def test_wrongDelimiter(self):
        old_nodes = [
            TextNode("Some of this text should be *italic* but they will provide the wrong delimiter", "normal"),
        ]
        delimiter = "`"
        text_type = "code"
        print(split_nodes_delimiter(old_nodes, delimiter, text_type))

    # Pass in a string with a pair of delimiters for italics:
    def test_italic(self):
        old_nodes = [
            TextNode("Some of this text should be *italic* if sorted correctly", "normal"),
        ]
        delimiter = "*"
        text_type = "italic"
        print(split_nodes_delimiter(old_nodes, delimiter, text_type))

    # Pass in a string with a pair of delimiters for bold:
    def test_bold(self):
        old_nodes = [
            TextNode("Some of this text should be **bold** if sorted correctly", "normal"),
        ]
        delimiter = "**"
        text_type = "bold"
        print(split_nodes_delimiter(old_nodes, delimiter, text_type))

    # Pass in a string with a pair of delimiters for code:
    def test_code(self):
        old_nodes = [
            TextNode("The following part `here` should appear as code", "normal"),
        ]
        delimiter = "`"
        text_type = "code"
        print(split_nodes_delimiter(old_nodes, delimiter, text_type))

    # Pass in a string with an odd number of delimiters:
    ### def test_oddDelimiters(self):
    ###     old_nodes = [
    ###         TextNode("*This is incorrect** Markdown syntax", "normal"),
    ###     ]
    ###     delimiter = "*"
    ###     text_type = "italic"
    ###     print(split_nodes_delimiter(old_nodes, delimiter, text_type))
    # ^ This test fails as it should

    # Pass in a string with more than one pair of the same kind of delimiter:
    def test_multiplePairs(self):
        old_nodes = [
            TextNode("*Several* parts of this text should appear as *italic*, including *this part*", "normal"),
        ]
        delimiter = "*"
        text_type = "italic"
        print(split_nodes_delimiter(old_nodes, delimiter, text_type))

    # Pass in more than one old_node in a list:
    def test_multipleOldNodes(self):
        old_nodes = [
            TextNode("This one is *italic*", "normal"),
            TextNode("This one is also *italic*", "normal"),
        ]
        delimiter = "*"
        text_type = "italic"
        print(split_nodes_delimiter(old_nodes, delimiter, text_type))

    # Pass in a text string with multiple delimiters, and call the function multiple times to achieve the goal:
    def test_multipleCalls(self):
        old_nodes = [
            TextNode("This one is *italic*, this one is **bold**, and this one is `code`.", "normal"),
        ]
        print(split_nodes_delimiter(split_nodes_delimiter(split_nodes_delimiter(old_nodes, "**", TextType.BOLD), "*", TextType.ITALIC), "`", TextType.CODE))
    