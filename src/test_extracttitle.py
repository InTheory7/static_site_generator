import unittest
from extracttitle import extract_title

class TestExtractTitle(unittest.TestCase):
    # Input empty string:
    ### def test_01emptyString(self):
    ###     md = ""
    ###     print(extract_title(md))

    # Input string with only a deeper heading level
    ### def test_02deeperHeading(self):
    ###     md = "### Level 3 Heading"
    ###     print(extract_title(md))

    # ^ Both of the above produce errors as expected.

    # Input a string with only a header
    def test_03correctHeading(self):
        md = "# Level 1 title as expected"
        print(extract_title(md))

    # Input a multi-line string with a header
    def test_04multiLineCorrect(self):
        md = """# This is the title
        This is part of the text"""
        print(extract_title(md))

    # Input a multi-line string with a header not on the first line, but still first after whitespace:
    def test_05multiLineWithWhitespaceFirst(self):
        md = """
        # This is the title
        This is part of the text"""
        print(extract_title(md))

if __name__ == "__main__":
    unittest.main()