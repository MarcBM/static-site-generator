import unittest
from main import split_nodes_link
from main import TextNode, TextType

class TestSplitNodesLink(unittest.TestCase):
  def test_split_links(self):
    node = TextNode(
        "This is text with a [link](https://example.com) and another [second link](https://example.com/2)",
        TextType.TEXT,
    )
    new_nodes = split_nodes_link([node])
    self.assertListEqual(
        [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://example.com"),
            TextNode(" and another ", TextType.TEXT),
            TextNode("second link", TextType.LINK, "https://example.com/2"),
        ],
        new_nodes,
    )
    
  def test_split_links_with_no_links(self):
    node = TextNode(
        "This is text with no links",
        TextType.TEXT,
    )
    new_nodes = split_nodes_link([node])
    self.assertListEqual(
        [
            TextNode("This is text with no links", TextType.TEXT),
        ],
        new_nodes,
    )
    
  def test_split_links_with_link_at_the_end(self):
    node = TextNode(
        "This is text with a [link](https://example.com)",
        TextType.TEXT,
    )
    new_nodes = split_nodes_link([node])
    self.assertListEqual(
        [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://example.com"),
        ],
        new_nodes,
    )
    
  def test_split_links_with_link_at_the_start(self):
    node = TextNode(
        "[link](https://example.com) This is text with a link",
        TextType.TEXT,
    )
    new_nodes = split_nodes_link([node])
    self.assertListEqual(
        [
            TextNode("link", TextType.LINK, "https://example.com"),
            TextNode(" This is text with a link", TextType.TEXT),
        ],
        new_nodes,
    )
    
  def test_split_links_with_link_in_the_middle(self):
    node = TextNode(
        "This is text with a [link](https://example.com) in the middle",
        TextType.TEXT,
    )
    new_nodes = split_nodes_link([node])
    self.assertListEqual(
        [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://example.com"),
            TextNode(" in the middle", TextType.TEXT)
        ],
        new_nodes,
    )
    
  def test_split_links_with_non_text_node(self):
    nodes = [TextNode("This is a bold node", TextType.BOLD), 
             TextNode("This is text with a [link](https://example.com)", TextType.TEXT)]
    new_nodes = split_nodes_link(nodes)
    self.assertListEqual(
        [
            TextNode("This is a bold node", TextType.BOLD),
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://example.com"),
        ],
        new_nodes,
    )
    
  def test_split_links_with_empty_string(self):
    node = TextNode(
        "",
        TextType.TEXT,
    )
    new_nodes = split_nodes_link([node])
    self.assertListEqual(
        [
            TextNode("", TextType.TEXT),
        ],
        new_nodes,
    )
    
  def test_split_links_with_multiple_link_nodes(self):
    node = TextNode(
        "This is text with a [link](https://example.com) and another [second link](https://example.com/2)",
        TextType.TEXT,
    )
    node2 = TextNode(
        "This is text with a [link](https://example.com) and another [second link](https://example.com/2)",
        TextType.TEXT,
    )
    new_nodes = split_nodes_link([node, node2])
    self.assertListEqual(
        [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://example.com"),
            TextNode(" and another ", TextType.TEXT),
            TextNode("second link", TextType.LINK, "https://example.com/2"),
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://example.com"),
            TextNode(" and another ", TextType.TEXT),
            TextNode("second link", TextType.LINK, "https://example.com/2"),
        ],
        new_nodes,
    )
if __name__ == "__main__":
    unittest.main()