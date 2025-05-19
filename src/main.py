import re

from textnode import TextNode, TextType
from leafnode import LeafNode

def main():
  text_node = TextNode("This is some anchor text", TextType.LINK, "https://example.com")
  print(text_node)
  
def text_node_to_html_node(text_node):
  match text_node.text_type:
    case TextType.TEXT:
      return LeafNode(tag=None, value=text_node.text)
    case TextType.BOLD:
      return LeafNode(tag="b", value=text_node.text)
    case TextType.ITALIC:
      return LeafNode(tag="i", value=text_node.text)
    case TextType.CODE:
      return LeafNode(tag="code", value=text_node.text)
    case TextType.LINK:
      return LeafNode(tag="a", value=text_node.text, props={"href": text_node.url})
    case TextType.IMAGE:
      return LeafNode(tag="img", value="", props={"src": text_node.url, "alt": text_node.text})
    case _:
      raise ValueError(f"Unknown text type: {text_node.text_type}")
    
def split_nodes_delimiter(old_nodes, delimiter, text_type):
  new_nodes = []
  for node in old_nodes:
    if node.text_type == TextType.TEXT:
      text = node.text
      parts = text.split(delimiter)
      if len(parts) % 2 == 0:
        raise ValueError("invalid markdown, odd number of delimiters")
      for i in range(len(parts)):
        if i % 2 == 0:
          new_nodes.append(TextNode(parts[i], TextType.TEXT))
        else:
          new_nodes.append(TextNode(parts[i], text_type))
    else:
      new_nodes.append(node)
  return new_nodes

def extract_markdown_images(text):
  pattern = r"!\[(.*?)\]\((\S*?)\)"
  return re.findall(pattern, text)

def extract_markdown_links(text):
  pattern = r"(?:[^!]\[|^\[)(.*?)\]\((\S*?)\)"
  return re.findall(pattern, text)
  
  
if __name__ == "__main__":
  main()