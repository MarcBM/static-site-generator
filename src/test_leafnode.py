import unittest
from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
  def test_default_constructor(self):
    node = LeafNode(tag="div", value="Hello, World!")
    self.assertEqual(node.tag, "div")
    self.assertEqual(node.value, "Hello, World!")
    self.assertIsNone(node.children)
    self.assertIsNone(node.props)
    
  def test_constructor_with_props(self):
    node = LeafNode(tag="div", value="Hello, World!", props={"class": "my-class"})
    self.assertEqual(node.tag, "div")
    self.assertEqual(node.value, "Hello, World!")
    self.assertIsNone(node.children)
    self.assertEqual(node.props, {"class": "my-class"})
    
  def test_to_html(self):
    node = LeafNode(tag="div", value="Hello, World!", props={"class": "my-class"})
    self.assertEqual(node.to_html(), '<div class="my-class">Hello, World!</div>')
    
  def test_to_html_no_tag(self):
    node = LeafNode(tag=None, value="Hello, World!")
    self.assertEqual(node.to_html(), "Hello, World!")
    
  def test_to_html_no_value(self):
    node = LeafNode(tag="div", value=None)
    with self.assertRaises(ValueError):
      node.to_html()
    node = LeafNode(tag="div", value=None, props={"class": "my-class"})
    with self.assertRaises(ValueError):
      node.to_html()
    node = LeafNode(tag=None, value=None)
    with self.assertRaises(ValueError):
      node.to_html()
    node = LeafNode(tag=None, value=None, props={"class": "my-class"})
    with self.assertRaises(ValueError):
      node.to_html()
  
  def test_to_html_no_props(self):
    node = LeafNode(tag="div", value="Hello, World!")
    self.assertEqual(node.to_html(), "<div>Hello, World!</div>")
    node = LeafNode(tag="div", value="Hello, World!", props=None)
    self.assertEqual(node.to_html(), "<div>Hello, World!</div>")