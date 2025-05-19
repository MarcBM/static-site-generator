import unittest
from textnode import TextNode, TextType
from leafnode import LeafNode
from main import text_node_to_html_node

class TestTextNodeToHtmlNode(unittest.TestCase):
  def test_raw_text(self):
    text_node = TextNode("This is some raw text", TextType.TEXT)
    html_node = text_node_to_html_node(text_node)
    self.assertEqual(html_node.tag, None)
    self.assertEqual(html_node.value, "This is some raw text")
    self.assertIsNone(html_node.props)
    self.assertIsNone(html_node.children)
    
  def test_bold_text(self):
    text_node = TextNode("This is some bold text", TextType.BOLD)
    html_node = text_node_to_html_node(text_node)
    self.assertEqual(html_node.tag, "b")
    self.assertEqual(html_node.value, "This is some bold text")
    self.assertIsNone(html_node.props)
    self.assertIsNone(html_node.children)
    
  def test_italic_text(self):
    text_node = TextNode("This is some italic text", TextType.ITALIC)
    html_node = text_node_to_html_node(text_node)
    self.assertEqual(html_node.tag, "i")
    self.assertEqual(html_node.value, "This is some italic text")
    self.assertIsNone(html_node.props)
    self.assertIsNone(html_node.children)
  
  def test_code_text(self):
    text_node = TextNode("This is some code text", TextType.CODE)
    html_node = text_node_to_html_node(text_node)
    self.assertEqual(html_node.tag, "code")
    self.assertEqual(html_node.value, "This is some code text")
    self.assertIsNone(html_node.props)
    self.assertIsNone(html_node.children)
  
  def test_link_text(self):
    text_node = TextNode("This is some link text", TextType.LINK, "https://example.com")
    html_node = text_node_to_html_node(text_node)
    self.assertEqual(html_node.tag, "a")
    self.assertEqual(html_node.value, "This is some link text")
    self.assertEqual(html_node.props, {"href": "https://example.com"})
    self.assertIsNone(html_node.children)
    
  def test_image_text(self):
    text_node = TextNode("This is some image text", TextType.IMAGE, "https://example.com/image.jpg")
    html_node = text_node_to_html_node(text_node)
    self.assertEqual(html_node.tag, "img")
    self.assertEqual(html_node.value, "")
    self.assertEqual(html_node.props, {"src": "https://example.com/image.jpg", "alt": "This is some image text"})
    self.assertIsNone(html_node.children)
    
  def test_unknown_text_type(self):
    text_node = TextNode("This is some unknown text", "unknown")
    with self.assertRaises(ValueError):
      text_node_to_html_node(text_node)
      
  def test_result_type(self):
    text_node = TextNode("This is some bold text", TextType.BOLD)
    html_node = text_node_to_html_node(text_node)
    self.assertIsInstance(html_node, LeafNode)
    
if __name__ == "__main__":
  unittest.main()