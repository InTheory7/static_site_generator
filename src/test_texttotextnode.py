import unittest
from textnode import TextNode, TextType
from texttotextnode import text_to_textnode

class TestTextToTextNode(unittest.TestCase):
    # Pass in an empty string:
    def test_01emptyString(self):
        text = ""
        print(f"\n{text_to_textnode(text)}")

    # Pass in a list:
    ### def test_02list(self):
    ###     text = ["Some text"]
    ###     print(text_to_textnode(text))

    # Pass in a TextNode:
    ### def test_03TextNode(self):
    ###     text = TextNode("Example text", TextType.BOLD)
    ###     print(text_to_textnode(text))

    # ^ Both tests fail as expected.

    # Pass in a string of plain text:
    def test_04plainText(self):
        text = "Here's some plain text"
        print(text_to_textnode(text))

    # Pass in a string containing bold text:
    def test_05boldText(self):
        text = "Here's some **bold** text"
        print(text_to_textnode(text))

    # Pass in a string containing italic text:
    def test_06italicText(self):
        text = "Here's some *italic* text"
        print(text_to_textnode(text))

    # Pass in a string containing code:
    def test_07code(self):
        text = "Here's some `code blocks`"
        print(text_to_textnode(text))

    # Pass in a string containing a link:
    def test_08link(self):
        text = "Here's a [link](www.exampleLink.com), does it work?"
        print(text_to_textnode(text))

    # Pass in a string containing an image:
    def test_09image(self):
        text = "Here's an image: ![Alt text example](imageLink.com/example.png)"
        print(text_to_textnode(text))

    # Pass a string containing all of the above:
    def test_10allTypes(self):
        text = "This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev) with some ordinary text at the end!"
        print(text_to_textnode(text))

if __name__ == "__main__":
    unittest.main()