import unittest
from splitbydelimiter import split_nodes_delimiter, split_nodes_image, split_nodes_link
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


class TestSplitByLink(unittest.TestCase):
    # Input an empty string:
    def test_1emptyString(self):
        old_nodes = [
            TextNode("", "normal")
        ]
        print(f"\n{split_nodes_link(old_nodes)}")
    
    # Input a string with no image:
    def test_2noLink(self):
        old_nodes = [
            TextNode("This string has no link", "normal")
        ]
        print(split_nodes_link(old_nodes))

    # Input a string with one link:
    def test_3oneLink(self):
        old_nodes = [
            TextNode("This is a [link](www.link.com), how does it look?", "normal")
        ]
        print(split_nodes_link(old_nodes))

    # Input a string with two links:
    def test_4twoLinks(self):
        old_nodes = [
            TextNode("Here's a different [link](hotLink.com), and so is [this one](hyperlink.org/link)", "normal")
        ]
        print(split_nodes_link(old_nodes))

    # Input a string with three links:
    def test_5threeLinks(self):
        old_nodes = [
            TextNode("Here's the first link: [link_1](link.example/#1). Here's the second [link](link.example/#2). And here's the third and final [link](link.example/#3)", "normal")
        ]
        print(split_nodes_link(old_nodes))

    # Input a string that's just an image:
    def test_6onlyLink(self):
        old_nodes = [
            TextNode("[This is just a link](linkTester.com)", "normal")
        ]
        print(split_nodes_link(old_nodes))

    # Input a string that starts with a link:
    def test_7startWithImage(self):
        old_nodes = [
            TextNode("[Anchor text immediately](wikipedia.org), and then normal text.", "normal")
        ]
        print(split_nodes_link(old_nodes))

    # Input a pair of nodes, each with link-containing strings:
    def test_8twoNodesWithLinks(self):
        old_nodes = [
            TextNode("Here's a node with a link: [This is the link](linkExample.biz), do you like it?", "normal"),
            TextNode("Link number 2: [Click here!](scam.link.tv)", "normal"),
        ]
        print(split_nodes_link(old_nodes))

# Repeat the image tests with the link version:
class TestSplitByImage(unittest.TestCase):
    # Input an empty string:
    def test_1emptyString(self):
        old_nodes = [
            TextNode("", "normal")
        ]
        print(f"\n{split_nodes_image(old_nodes)}")
    
    # Input a string with no image:
    def test_2noImage(self):
        old_nodes = [
            TextNode("This string has no image", "normal")
        ]
        print(split_nodes_image(old_nodes))

    # Input a string with one image:
    def test_3oneImage(self):
        old_nodes = [
            TextNode("This is an image: ![Here's the alt text](www.imageExample.com), how does it look?", "normal")
        ]
        print(split_nodes_image(old_nodes))

    # Input a string with two images:
    def test_4twoImages(self):
        old_nodes = [
            TextNode("This is an image: ![Here's the alt text](www.imageExample.com), and so is this: ![Here's a second alt text](secondImage.org/image.png)", "normal")
        ]
        print(split_nodes_image(old_nodes))

    # Input a string with three images:
    def test_5threeImages(self):
        old_nodes = [
            TextNode("Here's the first image: ![Alt text #1](www.imageExample.com). Here's the second image: ![Alt text #2](secondImage.org/image.png). And here's the third and final image: ![Alt text #3](final.image.png)", "normal")
        ]
        print(split_nodes_image(old_nodes))

    # Input a string that's just an image:
    def test_6onlyImage(self):
        old_nodes = [
            TextNode("![This is just an image](www.imageExample.com)", "normal")
        ]
        print(split_nodes_image(old_nodes))

    # Input a string that starts with an image:
    def test_7startWithImage(self):
        old_nodes = [
            TextNode("![This is just an image](www.imageExample.com), but then there's more text.", "normal")
        ]
        print(split_nodes_image(old_nodes))

    # Input a pair of nodes, each with image-containing strings:
    def test_8twoNodesWithImages(self):
        old_nodes = [
            TextNode("Here's a node with an image: ![This is just an image](www.imageExample.com), do you like it?", "normal"),
            TextNode("Image number 2: ![Alt text example](image.link.example.png)", "normal"),
        ]
        print(split_nodes_image(old_nodes))        
    
class TestSplitByImageAndLink(unittest.TestCase):
    # Test passing a string into the link and image functions in turn:
    def test_1linkThenImage(self):
        old_nodes = [
            TextNode("Here's an image: ![Image alt text](image.com), and here's a [link](examplelink.com). How are they?", "normal")
        ]
        print(f"\n{split_nodes_image(split_nodes_link(old_nodes))}")

    # Test passing a string into the image and link functions in turn:
    def test_2imageThenLink(self):
        old_nodes = [
            TextNode("Here's an image: ![Image alt text](image.com), and here's a [link](examplelink.com). How are they?", "normal")
        ]
        print(split_nodes_link(split_nodes_image(old_nodes)))

if __name__ == "__main__":
    unittest.main()