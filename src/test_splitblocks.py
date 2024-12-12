import unittest
from splitblocks import markdown_to_blocks, block_to_block_type

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

class TestBlockToBlockType(unittest.TestCase):
    # Pass in an empty string:
    def test_01emptyString(self):
        text = ""
        print(f"block_to_block_type test results:\nWant (normal): {block_to_block_type(text)}")

    # Pass in a list:
    ### def test_02list(self):
    ###     text = ["String in a list"]
    ###     print(block_to_block_type(text))
    # ^ Test failed as it should.

    # Pass in a single line of text:
    def test_03plainText(self):
        text = "Here's some text"
        print(f"Want (normal): {block_to_block_type(text)}")

    # Pass in a heading:
    def test_04heading(self):
        text = "# Heading"
        print(f"Want (heading): {block_to_block_type(text)}")

    # Pass in a different kind of heading:
    def test_05heading2(self):
        text = "#### Heading"
        print(f"Want (heading): {block_to_block_type(text)}")

    # Pass in an invalid heading:
    def test_06invalidHeading(self):
        text = "############# Heading"
        print(f"Want (normal): {block_to_block_type(text)}")

    # Pass in a code block:
    def test_07codeBlock(self):
        text = "```Here's some code```"
        print(f"Want (code): {block_to_block_type(text)}")

    # Pass in an invalid code block:
    def test_08invalidCodeBlock(self):
        text = "```Here's some wrong code``"
        print(f"Want (normal): {block_to_block_type(text)}")

    # Pass in a quote:
    def test_09quote(self):
        text = ">Quote"
        print(f"Want (quote): {block_to_block_type(text)}")

    # Pass in a multi-line quote:
    def test_10multilineQuote(self):
        text = """>Here's the start of the quote
        > here's some more
        > and here's the end.
        """
        print(f"Want (quote): {block_to_block_type(text)}")

    # Pass in an unordered list:
    def test_11unorderedList(self):
        text = """* Here's the start of a list.
        * Here's the end.
        """
        print(f"Want (unordered_list): {block_to_block_type(text)}")

    # Pass in an unordered list:
    def test_12unorderedList(self):
        text = """- Here's the start of a list.
        - Here's the end.
        """
        print(f"Want (unordered_list): {block_to_block_type(text)}")

    # Pass in an unordered list:
    def test_13unorderedList(self):
        text = """* Here's the start of a list.
        - Here's the middle.
        * Here's the end.
        """
        print(f"Want (unordered_list): {block_to_block_type(text)}")

    # Pass in an incorrect unordered list:
    def test_14invalidUnorderedList(self):
        text = """* Here's the start of a list.
         Here's the middle.
        * Here's the end.
        """
        print(f"Want (normal): {block_to_block_type(text)}")

    # Pass in an ordered list:
    def test_15orderedList(self):
        text = """1. Here's the start
        2. Here's the middle
        3. Here's the end.
        """
        print(f"Want (ordered_list): {block_to_block_type(text)}")

    # Pass in an ordered list with incorrect numbers:
    def test_16invalidOrderedList(self):
        text = """1. Here's the start
        3. Here's the middle
        1. Here's the end.
        """
        print(f"Want (normal): {block_to_block_type(text)}")

    # Pass in a long ordered list:
    def test_17orderedList(self):
        text = """1. Here's the start
        2. Here's the middle
        3. Here's the end.
        4. 4
        5. 5
        6. 6
        7. 7
        8. 8
        9. 9
        10. 10
        11. 11
        """
        print(f"Want (ordered_list): {block_to_block_type(text)}")

if __name__ == "__main__":
    unittest.main()