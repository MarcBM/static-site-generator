import unittest

from main import extract_title

class TestExtractTitle(unittest.TestCase):
  def test_base_case(self):
    text = "# This is a title"
    expected = "This is a title"
    result = extract_title(text)
    self.assertEqual(result, expected)
    
  def test_no_title(self):
    text = "This is not a title"
    self.assertRaises(ValueError, extract_title, text)
    
  def test_empty_string(self):
    text = ""
    self.assertRaises(ValueError, extract_title, text)
    
  def test_multiple_titles(self):
    text = "# Title 1\n# Title 2"
    expected = "Title 1"
    result = extract_title(text)
    self.assertEqual(result, expected)
    
  def test_title_with_special_characters(self):
    text = "# Title with special characters !@#$%^&*()"
    expected = "Title with special characters !@#$%^&*()"
    result = extract_title(text)
    self.assertEqual(result, expected)
    
  def test_title_with_whitespace(self):
    text = "#   Title with leading and trailing whitespace   "
    expected = "Title with leading and trailing whitespace"
    result = extract_title(text)
    self.assertEqual(result, expected)
    
  def test_title_with_newline(self):
    text = "# Title with newline\n"
    expected = "Title with newline"
    result = extract_title(text)
    self.assertEqual(result, expected)
    
  def test_title_with_more_content(self):
    text = "# Title with more content\nThis is some additional content."
    expected = "Title with more content"
    result = extract_title(text)
    self.assertEqual(result, expected)
    
if __name__ == "__main__":
  unittest.main()