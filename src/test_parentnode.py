import unittest

from parentnode import ParentNode

class TestParentNode(unittest.TestCase):
  def test_default_constructor(self):
    node = ParentNode(tag="div", children=[])
    self.assertEqual(node.tag, "div")
    self.assertEqual(node.children, [])
    self.assertIsNone(node.props)
    
  def test_constructor_with_props(self):
    node = ParentNode(tag="div", children=[], props={"class": "my-class"})
    self.assertEqual(node.tag, "div")
    self.assertEqual(node.children, [])
    self.assertEqual(node.props, {"class": "my-class"})
    
  def test_constructor_with_children(self):
    child_node = ParentNode(tag="span", children=[], props={"class": "child"})
    node = ParentNode(tag="div", children=[child_node])
    self.assertEqual(node.tag, "div")
    self.assertEqual(node.children, [child_node])
    self.assertIsNone(node.props)
    
  def test_to_html(self):
    child_node = ParentNode(tag="span", children=[], props={"class": "child"})
    node = ParentNode(tag="div", children=[child_node], props={"class": "my-class"})
    self.assertEqual(node.to_html(), '<div class="my-class"><span class="child"></span></div>')
    node = ParentNode(tag="div", children=[child_node])
    self.assertEqual(node.to_html(), '<div><span class="child"></span></div>')
    node = ParentNode(tag="div", children=[])
    self.assertEqual(node.to_html(), '<div></div>')
    node = ParentNode(tag="div", children=[], props={"class": "my-class"})
    self.assertEqual(node.to_html(), '<div class="my-class"></div>')
    node = ParentNode(tag="div", children=None)
    with self.assertRaises(ValueError):
      node.to_html()
    node = ParentNode(tag="div", children=None, props={"class": "my-class"})
    with self.assertRaises(ValueError):
      node.to_html()
    node = ParentNode(tag=None, children=[], props={"class": "my-class"})
    with self.assertRaises(ValueError):
      node.to_html()
    node = ParentNode(tag=None, children=[], props=None)
    with self.assertRaises(ValueError):
      node.to_html()
    node = ParentNode(tag=None, children=None, props={"class": "my-class"})
    with self.assertRaises(ValueError):
      node.to_html()
    node = ParentNode(tag=None, children=None)
    with self.assertRaises(ValueError):
      node.to_html()
    node = ParentNode(tag=None, children=None, props=None)
    with self.assertRaises(ValueError):
      node.to_html()
      
  def test_to_html_nested(self):
    child_node = ParentNode(tag="span", children=[], props={"class": "child"})
    grandchild_node = ParentNode(tag="a", children=[], props={"href": "https://example.com"})
    child_node.children.append(grandchild_node)
    node = ParentNode(tag="div", children=[child_node], props={"class": "my-class"})
    self.assertEqual(node.to_html(), '<div class="my-class"><span class="child"><a href="https://example.com"></a></span></div>')
    node = ParentNode(tag="div", children=[child_node])
    self.assertEqual(node.to_html(), '<div><span class="child"><a href="https://example.com"></a></span></div>')
    
if __name__ == "__main__":
  unittest.main()