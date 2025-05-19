import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
  def test_default_constructor(self):
    node = HTMLNode()
    self.assertIsNone(node.tag)
    self.assertIsNone(node.value)
    self.assertIsNone(node.children)
    self.assertIsNone(node.props)
    
  def test_constructor_with_tag(self):
    node = HTMLNode(tag="div")
    self.assertEqual(node.tag, "div")
    self.assertIsNone(node.value)
    self.assertIsNone(node.children)
    self.assertIsNone(node.props)
    
  def test_constructor_with_value(self):
    node = HTMLNode(value="Hello, World!")
    self.assertIsNone(node.tag)
    self.assertEqual(node.value, "Hello, World!")
    self.assertIsNone(node.children)
    self.assertIsNone(node.props)
  
  def test_constructor_with_children(self):
    child_node = HTMLNode(tag="span", value="Child")
    node = HTMLNode(children=[child_node])
    self.assertIsNone(node.tag)
    self.assertIsNone(node.value)
    self.assertEqual(node.children, [child_node])
    self.assertIsNone(node.props)
    
  def test_constructor_with_props(self):
    node = HTMLNode(props={"class": "my-class", "id": "my-id"})
    self.assertIsNone(node.tag)
    self.assertIsNone(node.value)
    self.assertIsNone(node.children)
    self.assertEqual(node.props, {"class": "my-class", "id": "my-id"})
    
  def test_constructor_with_all_params(self):
    child_node = HTMLNode(tag="span", value="Child")
    node = HTMLNode(tag="div", value="Hello, World!", children=[child_node], props={"class": "my-class"})
    self.assertEqual(node.tag, "div")
    self.assertEqual(node.value, "Hello, World!")
    self.assertEqual(node.children, [child_node])
    self.assertEqual(node.props, {"class": "my-class"})
    
  def test_repr(self):
    node = HTMLNode(tag="div", value="Hello, World!", children=[], props={"class": "my-class"})
    self.assertEqual(repr(node), "HTMLNode(tag=div, value=Hello, World!, children=[], props={'class': 'my-class'})")
    
  def test_repr_no_props(self):
    node = HTMLNode(tag="div", value="Hello, World!", children=[])
    self.assertEqual(repr(node), "HTMLNode(tag=div, value=Hello, World!, children=[], props=None)")
    
  def test_repr_no_children(self):
    node = HTMLNode(tag="div", value="Hello, World!", props={"class": "my-class"})
    self.assertEqual(repr(node), "HTMLNode(tag=div, value=Hello, World!, children=None, props={'class': 'my-class'})")
    
  def test_repr_no_value(self):
    node = HTMLNode(tag="div", children=[], props={"class": "my-class"})
    self.assertEqual(repr(node), "HTMLNode(tag=div, value=None, children=[], props={'class': 'my-class'})")
    
  def test_repr_no_tag(self):
    node = HTMLNode(value="Hello, World!", children=[], props={"class": "my-class"})
    self.assertEqual(repr(node), "HTMLNode(tag=None, value=Hello, World!, children=[], props={'class': 'my-class'})")
    
  def test_to_html(self):
    self.assertRaises(NotImplementedError, lambda: HTMLNode().to_html())
    
  def test_props_to_html(self):
    node = HTMLNode(props={"class": "my-class", "id": "my-id"})
    self.assertEqual(node.props_to_html(), ' class="my-class" id="my-id"')
    
  def test_props_to_html_empty(self):
    node = HTMLNode(props={})
    self.assertEqual(node.props_to_html(), "")
    
  def test_props_to_html_none(self):
    node = HTMLNode()
    self.assertEqual(node.props_to_html(), "")
    
if __name__ == "__main__":
    unittest.main()