import unittest

from blocktype import BlockType

class TestBlockType(unittest.TestCase):
  def test_base_case(self):
    block = "This is a test"
    expected_block_type = BlockType.PARAGRAPH
    result = BlockType.block_to_block_type(block)
    self.assertEqual(result, expected_block_type)
    
  def test_header(self):
    block = "# This is a header"
    expected_block_type = BlockType.HEADING
    result = BlockType.block_to_block_type(block)
    self.assertEqual(result, expected_block_type)
    
    block = "## This is also a header"
    expected_block_type = BlockType.HEADING
    result = BlockType.block_to_block_type(block)
    self.assertEqual(result, expected_block_type)
    
    block = "###### This is also a header"
    expected_block_type = BlockType.HEADING
    result = BlockType.block_to_block_type(block)
    self.assertEqual(result, expected_block_type)
    
    block = "This is not a header"
    expected_block_type = BlockType.PARAGRAPH
    result = BlockType.block_to_block_type(block)
    self.assertEqual(result, expected_block_type)
    
    block = "####### This is not a header"
    expected_block_type = BlockType.PARAGRAPH
    result = BlockType.block_to_block_type(block)
    self.assertEqual(result, expected_block_type)
    
    block = "## This is a header with # inside"
    expected_block_type = BlockType.HEADING
    result = BlockType.block_to_block_type(block)
    self.assertEqual(result, expected_block_type)
    
    block = "This is not a header with ## inside"
    expected_block_type = BlockType.PARAGRAPH
    result = BlockType.block_to_block_type(block)
    self.assertEqual(result, expected_block_type)
    
    block = "##"
    expected_block_type = BlockType.PARAGRAPH
    result = BlockType.block_to_block_type(block)
    self.assertEqual(result, expected_block_type)
    
  def test_code(self):
    block = "```python\nprint('Hello, World!')\n```"
    expected_block_type = BlockType.CODE
    result = BlockType.block_to_block_type(block)
    self.assertEqual(result, expected_block_type)
    
    block = "```python\nprint('Hello, World!')"
    expected_block_type = BlockType.PARAGRAPH
    result = BlockType.block_to_block_type(block)
    self.assertEqual(result, expected_block_type)
    
    block = "This is not a code block"
    expected_block_type = BlockType.PARAGRAPH
    result = BlockType.block_to_block_type(block)
    self.assertEqual(result, expected_block_type)
    
  def test_quote(self):
    block = "> This is a quote"
    expected_block_type = BlockType.QUOTE
    result = BlockType.block_to_block_type(block)
    self.assertEqual(result, expected_block_type)
    
    block = "> This is a quote\n> with multiple lines"
    expected_block_type = BlockType.QUOTE
    result = BlockType.block_to_block_type(block)
    self.assertEqual(result, expected_block_type)
    
    block = "This is not a quote"
    expected_block_type = BlockType.PARAGRAPH
    result = BlockType.block_to_block_type(block)
    self.assertEqual(result, expected_block_type)
    
    block = "> This is not a quote\nThis is a normal line"
    expected_block_type = BlockType.PARAGRAPH
    result = BlockType.block_to_block_type(block)
    self.assertEqual(result, expected_block_type)
    
  def test_unordered_list(self):
    block = "- This is an unordered list item"
    expected_block_type = BlockType.UNORDERED_LIST
    result = BlockType.block_to_block_type(block)
    self.assertEqual(result, expected_block_type)
    
    block = "- This is an unordered list item\n- with multiple lines"
    expected_block_type = BlockType.UNORDERED_LIST
    result = BlockType.block_to_block_type(block)
    self.assertEqual(result, expected_block_type)
    
    block = "This is not an unordered list"
    expected_block_type = BlockType.PARAGRAPH
    result = BlockType.block_to_block_type(block)
    self.assertEqual(result, expected_block_type)
    
    block = "- This is not an unordered list\nThis is a normal line"
    expected_block_type = BlockType.PARAGRAPH
    result = BlockType.block_to_block_type(block)
    self.assertEqual(result, expected_block_type)
    
  def test_ordered_list(self):
    block = "1. This is an ordered list item"
    expected_block_type = BlockType.ORDERED_LIST
    result = BlockType.block_to_block_type(block)
    self.assertEqual(result, expected_block_type)
    
    block = "1. This is an ordered list item\n2. with multiple lines"
    expected_block_type = BlockType.ORDERED_LIST
    result = BlockType.block_to_block_type(block)
    self.assertEqual(result, expected_block_type)
    
    block = "This is not an ordered list"
    expected_block_type = BlockType.PARAGRAPH
    result = BlockType.block_to_block_type(block)
    self.assertEqual(result, expected_block_type)
    
    block = "1. This is not an ordered list\nThis is a normal line"
    expected_block_type = BlockType.PARAGRAPH
    result = BlockType.block_to_block_type(block)
    self.assertEqual(result, expected_block_type)
    
    block = "1. This is not an ordered list\n2.This is a normal line"
    expected_block_type = BlockType.PARAGRAPH
    result = BlockType.block_to_block_type(block)
    self.assertEqual(result, expected_block_type)
    
    block = "1. This is not an ordered list\n2. This is a normal line\n4. This line skips 3"
    expected_block_type = BlockType.PARAGRAPH
    result = BlockType.block_to_block_type(block)
    self.assertEqual(result, expected_block_type)
    
  def test_empty_block(self):
    block = ""
    expected_block_type = BlockType.PARAGRAPH
    result = BlockType.block_to_block_type(block)
    self.assertEqual(result, expected_block_type)
    
if __name__ == "__main__":
  unittest.main()