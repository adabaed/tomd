import unittest
import os
from main import extract_text_from_pdf, extract_text_from_doc, process_text_to_markdown

class TestTomd(unittest.TestCase):

    def test_extract_text_from_pdf(self):
        pdf_path = 'tests/sample.pdf'
        text = extract_text_from_pdf(pdf_path)
        self.assertIn('TEST PDF', text)

    def test_extract_text_from_doc(self):
        docx_path = 'tests/sample.docx'
        text = extract_text_from_doc(docx_path)
        self.assertIn('TEST DOC', text)

if __name__ == '__main__':
    unittest.main()