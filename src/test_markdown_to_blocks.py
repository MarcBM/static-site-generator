import unittest

from main import markdown_to_blocks

class TestMarkdownToBlocks(unittest.TestCase):
  def test_markdown_to_blocks(self):
    md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
    blocks = markdown_to_blocks(md)
    self.assertEqual(
        blocks,
        [
            "This is **bolded** paragraph",
            "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
            "- This is a list\n- with items",
        ],
    )
    
  def test_markdown_to_blocks_with_empty_string(self):
    md = ""
    blocks = markdown_to_blocks(md)
    self.assertEqual(blocks, [])
    
  def test_markdown_to_blocks_with_no_markdown(self):
    md = "This is a plain text without any markdown."
    blocks = markdown_to_blocks(md)
    self.assertEqual(blocks, ["This is a plain text without any markdown."])
    
  def test_markdown_to_blocks_with_many_empty_lines(self):
    md = "\n\n\nThis is a paragraph with multiple empty lines above it.\n\n\n"
    blocks = markdown_to_blocks(md)
    self.assertEqual(blocks, ["This is a paragraph with multiple empty lines above it."])
    
  def test_markdown_to_blocks_with_lots_of_whitespace(self):
    md = "   This is a paragraph with leading and trailing whitespace.   "
    blocks = markdown_to_blocks(md)
    self.assertEqual(blocks, ["This is a paragraph with leading and trailing whitespace."])