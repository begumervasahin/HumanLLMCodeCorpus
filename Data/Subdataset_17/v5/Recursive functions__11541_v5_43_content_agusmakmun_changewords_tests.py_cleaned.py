import os
import unittest
from changewords.changewords import ChangeWords
class ChangeWordsTestCase(unittest.TestCase):
    def setUp(self):
        self.change_words_instance = ChangeWords()
        self.parser = self.change_words_instance.create_parser()
    def test_is_words_changed(self):
        args = [
            '--path', 'changewords_test',
            '--file_type', '.py',
            '--from_string', 'helloworld',
            '--to_string', 'mantabjiwa'
        ]
        parsed_args = self.parser.parse_args(args)
        result = self.change_words_instance.change_words(
            parsed_args.path,
            parsed_args.file_type,
            parsed_args.from_string,
            parsed_args.to_string
        )
        self.assertTrue(result)
if __name__ == '__main__':
    unittest.main()