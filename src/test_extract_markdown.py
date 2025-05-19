import unittest

from main import extract_markdown_images, extract_markdown_links

class TestExtractMarkdown(unittest.TestCase):
  def test_extract_image(self):
    text = "![alt text](https://example.com/image.png)"
    expected = [("alt text", "https://example.com/image.png")]
    result = extract_markdown_images(text)
    self.assertEqual(result, expected)
    text = "![alt text](https://example.com/image.png) and ![another alt text](https://example.com/another_image.png)"
    expected = [
      ("alt text", "https://example.com/image.png"),
      ("another alt text", "https://example.com/another_image.png")
    ]
    result = extract_markdown_images(text)
    self.assertEqual(result, expected)
    
  def test_extract_link(self):
    text = "[link text](https://example.com)"
    expected = [("link text", "https://example.com")]
    result = extract_markdown_links(text)
    self.assertEqual(result, expected)
    text = "[link text](https://example.com) and [another link text](https://example.com/another_link)"
    expected = [
      ("link text", "https://example.com"),
      ("another link text", "https://example.com/another_link")
    ]
    result = extract_markdown_links(text)
    self.assertEqual(result, expected)
    
  def test_extract_image_with_link(self):
    text = "[link text](https://example.com) and ![alt text](https://example.com/image.png)"
    expected = [
      ("alt text", "https://example.com/image.png")
    ]
    result = extract_markdown_images(text)
    self.assertEqual(result, expected)
    text = "[link text](https://example.com) and ![alt text](https://example.com/image.png) and [another link text](https://example.com/another_link)"
    expected = [
      ("alt text", "https://example.com/image.png")
    ]
    result = extract_markdown_images(text)
    self.assertEqual(result, expected)
    text = "[link text](https://example.com) and ![alt text](https://example.com/image.png) and ![another alt text](https://example.com/another_image.png)"
    expected = [
      ("alt text", "https://example.com/image.png"),
      ("another alt text", "https://example.com/another_image.png")
    ]
    result = extract_markdown_images(text)
    self.assertEqual(result, expected)
    
  def test_extract_link_with_image(self):
    text = "[link text](https://example.com) and ![alt text](https://example.com/image.png)"
    expected = [
      ("link text", "https://example.com")
    ]
    result = extract_markdown_links(text)
    self.assertEqual(result, expected)
    text = "[link text](https://example.com) and ![alt text](https://example.com/image.png) and [another link text](https://example.com/another_link)"
    expected = [
      ("link text", "https://example.com"),
      ("another link text", "https://example.com/another_link")
    ]
    result = extract_markdown_links(text)
    self.assertEqual(result, expected)
    text = "[link text](https://example.com) and ![alt text](https://example.com/image.png) and ![another alt text](https://example.com/another_image.png)"
    expected = [
      ("link text", "https://example.com")
    ]
    result = extract_markdown_links(text)
    self.assertEqual(result, expected)

  def test_extract_empty(self):
    text = ""
    expected = []
    result = extract_markdown_images(text)
    self.assertEqual(result, expected)
    result = extract_markdown_links(text)
    self.assertEqual(result, expected)
    
  def test_extract_no_markdown(self):
    text = "This is a plain text without any markdown."
    expected = []
    result = extract_markdown_images(text)
    self.assertEqual(result, expected)
    result = extract_markdown_links(text)
    self.assertEqual(result, expected)
    
  def test_extract_invalid_markdown(self):
    text = "This is an invalid markdown ![alt text](https://example.com/image.png and [link text]https://example.com)"
    expected = []
    result = extract_markdown_images(text)
    self.assertEqual(result, expected)
    result = extract_markdown_links(text)
    self.assertEqual(result, expected)
    
if __name__ == "__main__":
  unittest.main()