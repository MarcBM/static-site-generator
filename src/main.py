import re
import os
import shutil

from blocktype import BlockType
from parentnode import ParentNode
from textnode import TextNode, TextType
from leafnode import LeafNode

def main():
  copy_directory("static", "public")
  
def copy_directory(source, destination):
  if os.path.exists(destination):
    shutil.rmtree(destination)
    
  os.mkdir(destination)
  for item in os.listdir(source):
    if os.path.isfile(os.path.join(source, item)):
      shutil.copy(os.path.join(source, item), os.path.join(destination, item))
    elif os.path.isdir(os.path.join(source, item)):
      new_destination = os.path.join(destination, item)
      os.mkdir(new_destination)
      copy_directory(os.path.join(source, item), new_destination)
  
  
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
      if len(parts) == 1:
        new_nodes.append(node)
        continue
      if len(parts) % 2 == 0:
        raise ValueError("invalid markdown, odd number of delimiters")
      for i in range(len(parts)):
        if i == 0 and parts[i] == "":
          continue
        if i == len(parts) - 1 and parts[i] == "":
          continue
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

def split_nodes_links_images(old_nodes, text_type):
  if text_type != TextType.LINK and text_type != TextType.IMAGE:
    raise ValueError("text_type must be either LINK or IMAGE")
  
  new_nodes = []
  for node in old_nodes:
    if node.text_type != TextType.TEXT:
      new_nodes.append(node)
      continue
    text = node.text
    extracts = []
    if text_type == TextType.LINK:
      extracts = extract_markdown_links(text)
    elif text_type == TextType.IMAGE:
      extracts = extract_markdown_images(text)
    remaining_text = text
    for i in range(len(extracts)):
      extract = extracts[i]
      extract_node = None
      extract_string = ""
      if text_type == TextType.LINK:
        extract_node = TextNode(extract[0], TextType.LINK, extract[1])
        extract_string = f"[{extract[0]}]({extract[1]})"
      elif text_type == TextType.IMAGE:
        extract_node = TextNode(extract[0], TextType.IMAGE, extract[1])
        extract_string = f"![{extract[0]}]({extract[1]})"
      parts = remaining_text.split(extract_string)
      if len(parts) == 1:
        if extract_string + parts[0] == remaining_text:
          new_nodes.append(extract_node)
          remaining_text = parts[0]
        else:
          new_nodes.append(TextNode(parts[0], TextType.TEXT))
          new_nodes.append(extract_node)
          remaining_text = ""
      else:
        if parts[0] != "":
          new_nodes.append(TextNode(parts[0], TextType.TEXT))
        new_nodes.append(extract_node)
        remaining_text = parts[1]
    if remaining_text != "":
      new_nodes.append(TextNode(remaining_text, TextType.TEXT))
    
  if len(new_nodes) == 0:
    new_nodes = old_nodes
  return new_nodes

def split_nodes_image(old_nodes):
  new_nodes = split_nodes_links_images(old_nodes, TextType.IMAGE)
  return new_nodes

def split_nodes_link(old_nodes):
  new_nodes = split_nodes_links_images(old_nodes, TextType.LINK)
  return new_nodes

def text_to_textnodes(text):
  nodes = [TextNode(text, TextType.TEXT)]
  nodes = split_nodes_link(nodes)
  nodes = split_nodes_image(nodes)
  delimiter_bold = "**"
  delimiter_italic = "_"
  delimiter_code = "`"
  nodes = split_nodes_delimiter(nodes, delimiter_bold, TextType.BOLD)
  nodes = split_nodes_delimiter(nodes, delimiter_italic, TextType.ITALIC)
  nodes = split_nodes_delimiter(nodes, delimiter_code, TextType.CODE)
  return nodes
  
def markdown_to_blocks(markdown):
  final_blocks = []
  blocks = markdown.split("\n\n")
  for block in blocks:
    block = block.strip()
    if block == "":
      continue
    final_blocks.append(block)
    
  return final_blocks

def markdown_to_htmlnode(markdown):
  blocks = markdown_to_blocks(markdown)
  parent_node = ParentNode(tag="div", children=[])
  for block in blocks:
    blocktype = BlockType.block_to_block_type(block)
    
    if blocktype == BlockType.CODE:
      block = block.replace("```", "").lstrip()
      code_text_node = TextNode(block, TextType.CODE)
      child_node = text_node_to_html_node(code_text_node)
      child_node = ParentNode(tag="pre", children=[child_node])
      
    else:
      child_node = text_to_children(block, blocktype)
      
    parent_node.children.append(child_node)
  return parent_node

def text_to_children(text, blocktype):
  if blocktype == BlockType.PARAGRAPH:
    text = text.replace("\n", " ")
    text_nodes = text_to_textnodes(text)
    children = []
    for node in text_nodes:
      child_node = text_node_to_html_node(node)
      children.append(child_node)
    return ParentNode(tag="p", children=children)
  elif blocktype == BlockType.HEADING:
    header_level = text.count("#")
    header_text = text.lstrip("#").strip()
    text_nodes = text_to_textnodes(header_text)
    children = []
    for node in text_nodes:
      child_node = text_node_to_html_node(node)
      children.append(child_node)
    return ParentNode(tag=f"h{header_level}", children=children)
  elif blocktype == BlockType.QUOTE:
    quote_lines = [line.lstrip("> ").rstrip() for line in text.splitlines()]
    quote_text = "\n".join(quote_lines).strip()
    text_nodes = text_to_textnodes(quote_text)
    children = []
    for node in text_nodes:
      child_node = text_node_to_html_node(node)
      children.append(child_node)
    return ParentNode(tag="blockquote", children=children)
  elif blocktype == BlockType.UNORDERED_LIST:
    list_items = [line.lstrip("- ").rstrip() for line in text.splitlines()]
    children = []
    for item in list_items:
      text_nodes = text_to_textnodes(item)
      item_children = []
      for node in text_nodes:
        child_node = text_node_to_html_node(node)
        item_children.append(child_node)
      children.append(ParentNode(tag="li", children=item_children))
    return ParentNode(tag="ul", children=children)
  elif blocktype == BlockType.ORDERED_LIST:
    list_items = [re.sub(r'^\d+\.\s*', '', line).rstrip() for line in text.splitlines()]
    children = []
    for item in list_items:
      text_nodes = text_to_textnodes(item)
      item_children = []
      for node in text_nodes:
        child_node = text_node_to_html_node(node)
        item_children.append(child_node)
      children.append(ParentNode(tag="li", children=item_children))
    return ParentNode(tag="ol", children=children)
  
        
  
if __name__ == "__main__":
  main()