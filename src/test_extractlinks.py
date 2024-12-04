import unittest
from extractlinks import extract_markdown_images, extract_markdown_links

class TestImageExtraction(unittest.TestCase):
    # Pass a string with no image links:
    def test1_noLink(self):
        text = "This contains no images"
        print(extract_markdown_images(text))

    # Pass an empty string:
    def test2_emptyString(self):
        text = ""
        print(extract_markdown_images(text))

    # Pass a string with one image link:
    def test3_oneImageLink(self):
        text = "This string contains one image link: ![Here's the alt text](https://www.image.source)"
        print(extract_markdown_images(text))

    # Pass a string with two image links:
    def test4_twoImageLinks(self):
        text = "Here's one image link: ![Here's the alt text](https://www.image.source), and here's another: ![This is the second alt text](www.secondimage.com)"
        print(extract_markdown_images(text))

    # Pass a string with one image link with an empty alt text:
    def test5_emptyAltText(self):
        text = "This has no alt text: ![](https://www.image.source)"
        print(extract_markdown_images(text))

    # Pass a string with one image link with an empty image link:
    def test6_emptyImageLink(self):
        text = "This has no link: ![Example alt text]()"
        print(extract_markdown_images(text))

class TestILinkExtraction(unittest.TestCase):
    # Pass a string with no links:
    def test1_noLink(self):
        text = "This contains no links"
        print(extract_markdown_links(text))

    # Pass an empty string:
    def test2_emptyString(self):
        text = ""
        print(extract_markdown_links(text))

    # Pass a string with one link:
    def test3_oneLink(self):
        text = "This string contains one [link](https://www.example.link)"
        print(extract_markdown_links(text))

    # Pass a string with two links:
    def test4_twoLinks(self):
        text = "Here's one [link](https://www.link.example), and here's [another](www.second.link)"
        print(extract_markdown_links(text))

    # Pass a string with one link with an empty anchor text:
    def test5_emptyAnchor(self):
        text = "This has no anchor text: [](https://link.example)"
        print(extract_markdown_links(text))

    # Pass a string with one link with an empty link:
    def test6_emptyLink(self):
        text = "This has no link: [Example anchor text]()"
        print(extract_markdown_links(text))

if __name__ == "__main__":
    unittest.main()