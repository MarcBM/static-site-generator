from enum import Enum
import re

class BlockType(Enum):
  PARAGRAPH = "Paragraph"
  HEADING = "Heading"
  CODE = "Code"
  QUOTE = "Quote"
  UNORDERED_LIST = "Unordered List"
  ORDERED_LIST = "Ordered List"
  
  def check_for_header(block):
    return bool(re.match(r'^(#{1,6})\s.+', block))
  
  def check_for_code(block):
    return block.startswith("```") and block.endswith("```")
  
  def check_for_quote(block):
    lines = [line for line in block.splitlines() if line.strip()]
    if not lines:
      return False
    return all(line.startswith(">") for line in lines)
  
  def check_for_unordered_list(block):
    lines = [line for line in block.splitlines() if line]
    if not lines:
      return False
    return all(line.startswith("- ") for line in lines)
  
  def check_for_ordered_list(block):
    lines = [line for line in block.splitlines() if line]
    if not lines:
      return False
    for idx, line in enumerate(lines, start=1):
      if not line.startswith(f"{idx}. "):
        return False
    return True
  
  def block_to_block_type(block):
    if BlockType.check_for_header(block):
      return BlockType.HEADING
    elif BlockType.check_for_code(block):
      return BlockType.CODE
    elif BlockType.check_for_quote(block):
      return BlockType.QUOTE
    elif BlockType.check_for_unordered_list(block):
      return BlockType.UNORDERED_LIST
    elif BlockType.check_for_ordered_list(block):
      return BlockType.ORDERED_LIST
    else:
      return BlockType.PARAGRAPH
