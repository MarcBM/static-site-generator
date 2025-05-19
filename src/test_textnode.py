import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
        
    def test_eq_different_text(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a different text node", TextType.BOLD)
        self.assertNotEqual(node, node2)
        
    def test_eq_different_type(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.ITALIC)
        self.assertNotEqual(node, node2)
        
    def test_eq_different_url(self):
        node = TextNode("This is a text node", TextType.BOLD, "https://example.com")
        node2 = TextNode("This is a text node", TextType.BOLD, "https://another-example.com")
        self.assertNotEqual(node, node2)
        
    def test_eq_different_object(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = "This is a string"
        self.assertNotEqual(node, node2)
        
    def test_eq_none(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = None
        self.assertNotEqual(node, node2)
    
    def test_eq_different_class(self):
        class DifferentClass:
            pass

        node = TextNode("This is a text node", TextType.BOLD)
        node2 = DifferentClass()
        self.assertNotEqual(node, node2)
        
    def test_url_none(self):
        node = TextNode("This is a text node", TextType.BOLD)
        self.assertIsNone(node.url)
        
    def test_eq_url_none(self):
        node = TextNode("This is a text node", TextType.LINK, "test-url.com")
        node2 = TextNode("This is a text node", TextType.LINK)
        self.assertNotEqual(node, node2)
        
    def test_rpr(self):
        node = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(repr(node), "TextNode(This is a text node, Bold, None)")


if __name__ == "__main__":
    unittest.main()