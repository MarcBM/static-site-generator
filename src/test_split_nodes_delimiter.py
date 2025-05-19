import unittest

from textnode import TextNode, TextType
from main import split_nodes_delimiter

class TestSplitNodesDelimiter(unittest.TestCase):
  def test_split_pure_text(self):
    old_nodes = [TextNode("This is just text with no decorations", TextType.TEXT)]
    delimiter = "_"
    text_type = TextType.ITALIC
    expected_nodes = [
      TextNode("This is just text with no decorations", TextType.TEXT)
    ]
    result = split_nodes_delimiter(old_nodes, delimiter, text_type)
    self.assertEqual(result, expected_nodes)
    
  def test_bold_text(self):
    old_nodes = [TextNode("This is some bold text", TextType.BOLD)]
    delimiter = "_"
    text_type = TextType.ITALIC
    expected_nodes = [
      TextNode("This is some bold text", TextType.BOLD)
    ]
    result = split_nodes_delimiter(old_nodes, delimiter, text_type)
    self.assertEqual(result, expected_nodes)
    
  def test_split_text_with_delimiter(self):
    old_nodes = [TextNode("This is some _italic_ text", TextType.TEXT)]
    delimiter = "_"
    text_type = TextType.ITALIC
    expected_nodes = [
      TextNode("This is some ", TextType.TEXT),
      TextNode("italic", TextType.ITALIC),
      TextNode(" text", TextType.TEXT)
    ]
    result = split_nodes_delimiter(old_nodes, delimiter, text_type)
    self.assertEqual(result, expected_nodes)
    
  def test_split_text_with_multiple_delimiters(self):
    old_nodes = [TextNode("This is some _italic_ and _italic_ text", TextType.TEXT)]
    delimiter = "_"
    text_type = TextType.ITALIC
    expected_nodes = [
      TextNode("This is some ", TextType.TEXT),
      TextNode("italic", TextType.ITALIC),
      TextNode(" and ", TextType.TEXT),
      TextNode("italic", TextType.ITALIC),
      TextNode(" text", TextType.TEXT)
    ]
    result = split_nodes_delimiter(old_nodes, delimiter, text_type)
    self.assertEqual(result, expected_nodes)
    
  def test_split_text_with_different_delimiters(self):
    old_nodes = [TextNode("This is some _italic_ and **bold** and `code` text", TextType.TEXT)]
    delimiter = "_"
    text_type = TextType.ITALIC
    expected_nodes = [
      TextNode("This is some ", TextType.TEXT),
      TextNode("italic", TextType.ITALIC),
      TextNode(" and **bold** and `code` text", TextType.TEXT)
    ]
    result = split_nodes_delimiter(old_nodes, delimiter, text_type)
    self.assertEqual(result, expected_nodes)
    delimiter = "**"
    text_type = TextType.BOLD
    expected_nodes = [
      TextNode("This is some ", TextType.TEXT),
      TextNode("italic", TextType.ITALIC),
      TextNode(" and ", TextType.TEXT),
      TextNode("bold", TextType.BOLD),
      TextNode(" and `code` text", TextType.TEXT)
    ]
    result = split_nodes_delimiter(result, delimiter, text_type)
    self.assertEqual(result, expected_nodes)
    delimiter = "`"
    text_type = TextType.CODE
    expected_nodes = [
      TextNode("This is some ", TextType.TEXT),
      TextNode("italic", TextType.ITALIC),
      TextNode(" and ", TextType.TEXT),
      TextNode("bold", TextType.BOLD),
      TextNode(" and ", TextType.TEXT),
      TextNode("code", TextType.CODE),
      TextNode(" text", TextType.TEXT)
    ]
    result = split_nodes_delimiter(result, delimiter, text_type)
    self.assertEqual(result, expected_nodes)
    
  def test_split_multiple_nodes(self):
    old_nodes = [
      TextNode("This is some _italic_ text", TextType.TEXT),
      TextNode("This is some **bold** text", TextType.BOLD)
    ]
    delimiter = "_"
    text_type = TextType.ITALIC
    expected_nodes = [
      TextNode("This is some ", TextType.TEXT),
      TextNode("italic", TextType.ITALIC),
      TextNode(" text", TextType.TEXT),
      TextNode("This is some **bold** text", TextType.BOLD)
    ]
    result = split_nodes_delimiter(old_nodes, delimiter, text_type)
    self.assertEqual(result, expected_nodes)
    
  def test_split_multiple_eligible_nodes(self):
    old_nodes = [
      TextNode("This node has some _italic_ text", TextType.TEXT),
      TextNode("This node has multiple _instances_ of _italic_ text", TextType.TEXT),
      TextNode("This node is already a **code** node", TextType.CODE),
      TextNode("This node has some **BOLD** text", TextType.TEXT)
    ]
    delimiter = "_"
    text_type = TextType.ITALIC
    expected_nodes = [
      TextNode("This node has some ", TextType.TEXT),
      TextNode("italic", TextType.ITALIC),
      TextNode(" text", TextType.TEXT),
      TextNode("This node has multiple ", TextType.TEXT),
      TextNode("instances", TextType.ITALIC),
      TextNode(" of ", TextType.TEXT),
      TextNode("italic", TextType.ITALIC),
      TextNode(" text", TextType.TEXT),
      TextNode("This node is already a **code** node", TextType.CODE),
      TextNode("This node has some **BOLD** text", TextType.TEXT)
    ]
    result = split_nodes_delimiter(old_nodes, delimiter, text_type)
    self.assertEqual(result, expected_nodes)
    
    delimiter = "**"
    text_type = TextType.BOLD
    expected_nodes = [
      TextNode("This node has some _italic_ text", TextType.TEXT),
      TextNode("This node has multiple _instances_ of _italic_ text", TextType.TEXT),
      TextNode("This node is already a **code** node", TextType.CODE),
      TextNode("This node has some ", TextType.TEXT),
      TextNode("BOLD", TextType.BOLD),
      TextNode(" text", TextType.TEXT)
    ]
    result = split_nodes_delimiter(old_nodes, delimiter, text_type)
    self.assertEqual(result, expected_nodes)
    
  def test_split_invalid_markdown(self):
    old_nodes = [TextNode("This text has an _unmatched_ _delimiter", TextType.TEXT)]
    delimiter = "_"
    text_type = TextType.ITALIC
    with self.assertRaises(ValueError):
      split_nodes_delimiter(old_nodes, delimiter, text_type)
    
if __name__ == "__main__":
  unittest.main()