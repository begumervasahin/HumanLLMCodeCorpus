import os
import unittest
from changewords.changewords import ChangeWords
class TestChangeWords(unittest.TestCase):
    def setUp(self):
        self.change = ChangeWords()
        self.parser = self.change.create_parser()
        self.change_words = self.change.change_words
    def test_is_words_changed(self):
        parsed_args = self.parser.parse_args(['--path', 'changewords_test',
                                              '--file_type', '.py',
                                              '--from_string', 'helloworld',
                                              '--to_string', 'mantabjiwa'])
        path = parsed_args.path
        file_type = parsed_args.file_type
        from_string = parsed_args.from_string
        to_string = parsed_args.to_string
        self.assertTrue(self.change_words(path, file_type, from_string, to_string))
if __name__ == '__main__':
    unittest.main()