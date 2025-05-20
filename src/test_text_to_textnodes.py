import unittest

from main import text_to_textnodes
from textnode import TextNode, TextType

class TestTextToTextNodes(unittest.TestCase):
  def test_base_case(self):
    text = "This is a test"
    expected_nodes = [
      TextNode("This is a test", TextType.TEXT)
    ]
    result = text_to_textnodes(text)
    self.assertEqual(result, expected_nodes)
    
  def test_bold_text(self):
    text = "This is a **bold** test"
    expected_nodes = [
      TextNode("This is a ", TextType.TEXT),
      TextNode("bold", TextType.BOLD),
      TextNode(" test", TextType.TEXT)
    ]
    result = text_to_textnodes(text)
    self.assertEqual(result, expected_nodes)
    
  def test_italic_text(self):
    text = "This is a _italic_ test"
    expected_nodes = [
      TextNode("This is a ", TextType.TEXT),
      TextNode("italic", TextType.ITALIC),
      TextNode(" test", TextType.TEXT)
    ]
    result = text_to_textnodes(text)
    self.assertEqual(result, expected_nodes)
    
  def test_code_text(self):
    text = "This is a `code` test"
    expected_nodes = [
      TextNode("This is a ", TextType.TEXT),
      TextNode("code", TextType.CODE),
      TextNode(" test", TextType.TEXT)
    ]
    result = text_to_textnodes(text)
    self.assertEqual(result, expected_nodes)
    
  def test_link_text(self):
    text = "This is a [link](https://example.com) test"
    expected_nodes = [
      TextNode("This is a ", TextType.TEXT),
      TextNode("link", TextType.LINK, "https://example.com"),
      TextNode(" test", TextType.TEXT)
    ]
    result = text_to_textnodes(text)
    self.assertEqual(result, expected_nodes)
    
  def test_image_text(self):
    text = "This is an ![alt text](https://example.com/image.png) test"
    expected_nodes = [
      TextNode("This is an ", TextType.TEXT),
      TextNode("alt text", TextType.IMAGE, "https://example.com/image.png"),
      TextNode(" test", TextType.TEXT)
    ]
    result = text_to_textnodes(text)
    self.assertEqual(result, expected_nodes)
    
  def test_multiple_text_types(self):
    text = "This is a **bold** and _italic_ and `code` and [link](https://example.com) and ![alt text](https://example.com/image.png) test"
    expected_nodes = [
      TextNode("This is a ", TextType.TEXT),
      TextNode("bold", TextType.BOLD),
      TextNode(" and ", TextType.TEXT),
      TextNode("italic", TextType.ITALIC),
      TextNode(" and ", TextType.TEXT),
      TextNode("code", TextType.CODE),
      TextNode(" and ", TextType.TEXT),
      TextNode("link", TextType.LINK, "https://example.com"),
      TextNode(" and ", TextType.TEXT),
      TextNode("alt text", TextType.IMAGE, "https://example.com/image.png"),
      TextNode(" test", TextType.TEXT)
    ]
    result = text_to_textnodes(text)
    self.assertEqual(result, expected_nodes)
    
  def test_empty_string(self):
    text = ""
    expected_nodes = [
      TextNode("", TextType.TEXT)
    ]
    result = text_to_textnodes(text)
    self.assertEqual(result, expected_nodes)
    
  def test_formatting_at_start_and_end(self):
    text = "**This is a test**"
    expected_nodes = [
      TextNode("This is a test", TextType.BOLD)
    ]
    result = text_to_textnodes(text)
    self.assertEqual(result, expected_nodes)
    
  def test_formatting_with_no_text(self):
    text = "****"
    expected_nodes = [
      TextNode("", TextType.BOLD)
    ]
    result = text_to_textnodes(text)
    self.assertEqual(result, expected_nodes)
    
  def test_text_types_at_start_and_end(self):
    text = "**This is a test** and _this is italic_ and `this is code`"
    expected_nodes = [
      TextNode("This is a test", TextType.BOLD),
      TextNode(" and ", TextType.TEXT),
      TextNode("this is italic", TextType.ITALIC),
      TextNode(" and ", TextType.TEXT),
      TextNode("this is code", TextType.CODE)
    ]
    result = text_to_textnodes(text)
    self.assertEqual(result, expected_nodes)
    
  def test_text_types_with_no_text(self):
    text = "**** and __ and ``"
    expected_nodes = [
      TextNode("", TextType.BOLD),
      TextNode(" and ", TextType.TEXT),
      TextNode("", TextType.ITALIC),
      TextNode(" and ", TextType.TEXT),
      TextNode("", TextType.CODE)
    ]
    result = text_to_textnodes(text)
    self.assertEqual(result, expected_nodes)
    
if __name__ == '__main__':
  unittest.main()