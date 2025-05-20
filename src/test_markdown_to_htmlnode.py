import unittest

from main import markdown_to_htmlnode

class TestMarkdownToHtmlNode(unittest.TestCase):
  def test_paragraphs(self):
    md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""

    node = markdown_to_htmlnode(md)
    html = node.to_html()
    self.assertEqual(
        html,
        "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
    )

  def test_codeblock(self):
      md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""

      node = markdown_to_htmlnode(md)
      html = node.to_html()
      self.assertEqual(
          html,
          "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
      )
  
  def test_heading(self):
      md = """
# This is a heading

## This is a subheading

### This is a sub-subheading
"""
      node = markdown_to_htmlnode(md)
      html = node.to_html()
      self.assertEqual(
          html,
          "<div><h1>This is a heading</h1><h2>This is a subheading</h2><h3>This is a sub-subheading</h3></div>",
      )
      
  def test_quote(self):
      md = """
> This is a quote
> This is the same quote

> This is another quote
> This is the same quote
"""
      node = markdown_to_htmlnode(md)
      html = node.to_html()
      self.assertEqual(
          html,
          "<div><blockquote>This is a quote\nThis is the same quote</blockquote><blockquote>This is another quote\nThis is the same quote</blockquote></div>",
      )
      
  def test_unordered_list(self):
      md = """
- This is an unordered list item
- with multiple lines
- This is another unordered list item
"""
      node = markdown_to_htmlnode(md)
      html = node.to_html()
      self.assertEqual(
          html,
          "<div><ul><li>This is an unordered list item</li><li>with multiple lines</li><li>This is another unordered list item</li></ul></div>",
      )
      
      md = """
- This is an unordered list item
- with multiple lines

- This is another unordered list item
- with multiple lines
"""
      node = markdown_to_htmlnode(md)
      html = node.to_html()
      self.assertEqual(
          html,
          "<div><ul><li>This is an unordered list item</li><li>with multiple lines</li></ul><ul><li>This is another unordered list item</li><li>with multiple lines</li></ul></div>",
      )
      
  def test_ordered_list(self):
      md = """
1. This is an ordered list item
2. with multiple lines
3. This is another ordered list item
"""
      node = markdown_to_htmlnode(md)
      html = node.to_html()
      self.assertEqual(
          html,
          "<div><ol><li>This is an ordered list item</li><li>with multiple lines</li><li>This is another ordered list item</li></ol></div>",
      )
      
      md = """
1. This is an ordered list item
2. with multiple lines
3. This is another ordered list item

1. This is an ordered list item
2. with multiple lines
3. This is another ordered list item
"""
      node = markdown_to_htmlnode(md)
      html = node.to_html()
      self.assertEqual(
          html,
          "<div><ol><li>This is an ordered list item</li><li>with multiple lines</li><li>This is another ordered list item</li></ol><ol><li>This is an ordered list item</li><li>with multiple lines</li><li>This is another ordered list item</li></ol></div>",
      )
      
  def test_empty_string(self):
      md = ""
      node = markdown_to_htmlnode(md)
      html = node.to_html()
      self.assertEqual(html, "<div></div>")
      md = "   "
      node = markdown_to_htmlnode(md)
      html = node.to_html()
      self.assertEqual(html, "<div></div>")
      md = "\n\n\n"
      node = markdown_to_htmlnode(md)
      html = node.to_html()
      self.assertEqual(html, "<div></div>")
      
  def test_paragraph_with_links(self):
      md = """
This is a paragraph with a [link](https://example.com) and some text.

This is another paragraph with a [link](https://example.com) and some text.
"""
      node = markdown_to_htmlnode(md)
      html = node.to_html()
      self.assertEqual(
          html,
          "<div><p>This is a paragraph with a <a href=\"https://example.com\">link</a> and some text.</p><p>This is another paragraph with a <a href=\"https://example.com\">link</a> and some text.</p></div>",
      )
      
  def test_list_with_decorators(self):
      md = """
- This _is_ an **unordered** list item
- with multiple `lines`
"""
      node = markdown_to_htmlnode(md)
      html = node.to_html()
      self.assertEqual(
          html,
          "<div><ul><li>This <i>is</i> an <b>unordered</b> list item</li><li>with multiple <code>lines</code></li></ul></div>",
      )