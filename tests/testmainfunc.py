import main
import unittest
from unittest.mock import patch

class TestMainFunc(unittest.TestCase):

    def test_all_doc_owners_names(self):
        expected_res = {element['name'] for element in main.documents}
        self.assertEqual(expected_res, main.get_all_doc_owners_names())

    @patch('builtins.input', lambda user_doc_number: '11-2')
    def test_doc_owner_name(self):
        self.assertEqual('Геннадий Покемонов', main.get_doc_owner_name())

    def test_all_docs_info(self):
        expected_res = [list(document.values()) for document in main.documents]
        self.assertEqual(expected_res, main.show_all_docs_info())

    @patch('builtins.input', lambda user_doc_number: '10006')
    def test_doc_shelf(self):
        self.assertEqual('2', main.get_doc_shelf())

    @patch('builtins.input', side_effect=['1231112', 'passport', 'Peter', '3'])
    def test_add_new_doc(self, mock_input):
        self.assertEqual('3', main.add_new_doc())
        assert {'1231112', 'passport', 'Peter'} in [set(doc_values.values()) for doc_values in main.documents]
        assert '1231112' in main.directories['3']

    @patch('builtins.input', lambda user_doc_number: '1231112')
    def test_delete_doc(self):
        self.assertEqual(True, main.delete_doc()[1])
        assert {'1231112', 'passport', 'Peter'} not in [set(doc_values.values()) for doc_values in main.documents]
        assert '1231112' not in main.directories['3']
