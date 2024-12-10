import unittest
from splitblocks import markdown_to_blocks

class TestMarkdownToBlocks(unittest.TestCase):
    # Pass in an empty string:
    def test_01emptyString(self):
        text = ""
        print(f"\n{markdown_to_blocks(text)}")

    # Pass in a list:
    ### def test_02list(self):
    ###     text = ["String in a list"]
    ###     print(markdown_to_blocks(text))
    # ^ Test failed as it should.

    # Pass in a single line:
    def test_03oneLine(self):
        text = "Single line string"
        print(markdown_to_blocks(text))

    # Pass in two paragraphs:
    def test_04twoLines(self):
        text = "Single line string. \n Here's another line."
        print(markdown_to_blocks(text))

    # Pass in two paragraphs with extra newlines and empty strings:
    def test_05emptyCases(self):
        text = "Single line string. \n \n\n\n Here's another line after some newlines. \n"
        print(markdown_to_blocks(text))

    # Pass in the example from the assignment:
    def test_06assignmentCase(self):
        text = """# This is a heading

        This is a paragraph of text. It has some **bold** and *italic* words inside of it.

        * This is the first list item in a list block
        * This is a list item
        * This is another list item"""
        print(markdown_to_blocks(text))

if __name__ == "__main__":
    unittest.main()