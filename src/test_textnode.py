import unittest
from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
    # Test equality:
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
    # Test equality with a URL:
    def test_eq2(self):
        node = TextNode("Escape", TextType.ITALIC, "www.bootdev.com")
        node2 = TextNode("Escape", TextType.ITALIC, "www.bootdev.com")
        self.assertEqual(node, node2)
    # Test unequality with different input text:
    def test_eq3(self):
        node = TextNode("These two should not be equal", TextType.CODE, "A")
        node2 = TextNode("Because this text is different", TextType.CODE, "A")
        self.assertNotEqual(node, node2)
    # Test unequality with different TextType:
    def test_eq4(self):
        node = TextNode("Equal", TextType.CODE)
        node2 = TextNode("Equal", TextType.ITALIC)
        self.assertNotEqual(node, node2)
    # Test unequality with different URL:
    def test_eq5(self):
        node = TextNode("Equal", TextType.CODE, "one.org")
        node2 = TextNode("Equal", TextType.CODE, "two.org")
        self.assertNotEqual(node, node2)
    # Test equality with None type URL:
    def test_eq6(self):
        node = TextNode("Escape", TextType.ITALIC, None)
        node2 = TextNode("Escape", TextType.ITALIC, None)
        self.assertEqual(node, node2)
    # Test unequality with different types for text input:
    def test_eq7(self):
        node = TextNode("Escape", TextType.ITALIC, None)
        node2 = TextNode(5, TextType.ITALIC, None)
        self.assertNotEqual(node, node2)

if __name__ == "__main__":
    unittest.main()