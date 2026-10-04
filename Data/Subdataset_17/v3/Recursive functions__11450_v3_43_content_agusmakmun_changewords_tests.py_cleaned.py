import argparse
import os
class ChangeWords:
    def create_parser(self):
        parser = argparse.ArgumentParser(description='Change words in files.')
        parser.add_argument('--path', required=True, help='Path to directory or file.')
        parser.add_argument('--file_type', required=True, help='Type of files to search.')
        parser.add_argument('--from_string', required=True, help='String to search for.')
        parser.add_argument('--to_string', required=True, help='String to replace with.')
        return parser
    def change_words(self, path, file_type, from_string, to_string):
        if os.path.isfile(path) and path.endswith(file_type):
            self._replace_in_file(path, from_string, to_string)
            return True
        elif os.path.isdir(path):
            for root, _, files in os.walk(path):
                for file in files:
                    if file.endswith(file_type):
                        file_path = os.path.join(root, file)
                        self._replace_in_file(file_path, from_string, to_string)
            return True
        return False
    def _replace_in_file(self, file_path, from_string, to_string):
        with open(file_path, 'r') as file:
            content = file.read()
        new_content = content.replace(from_string, to_string)
        with open(file_path, 'w') as file:
            file.write(new_content)
if __name__ == "__main__":
    changer = ChangeWords()
    parser = changer.create_parser()
    args = parser.parse_args()
    changer.change_words(args.path, args.file_type, args.from_string, args.to_string)
import os
import unittest
from changewords.changewords import ChangeWords
class ChangeWordsTestCase(unittest.TestCase):
    def setUp(self):
        self.change_words_instance = ChangeWords()
        self.parser = self.change_words_instance.create_parser()
        self.test_dir = 'changewords_test'
        self.test_file = 'test_file.py'
        self.from_string = 'helloworld'
        self.to_string = 'mantabjiwa'
        if not os.path.exists(self.test_dir):
            os.makedirs(self.test_dir)
        with open(os.path.join(self.test_dir, self.test_file), 'w') as f:
            f.write(f"This is a test file with the word {self.from_string} in it.")
    def tearDown(self):
        if os.path.exists(self.test_dir):
            for root, _, files in os.walk(self.test_dir):
                for file in files:
                    os.remove(os.path.join(root, file))
            os.rmdir(self.test_dir)
    def test_is_words_changed(self):
        args = self.parser.parse_args([
            '--path', self.test_dir,
            '--file_type', '.py',
            '--from_string', self.from_string,
            '--to_string', self.to_string
        ])
        self.assertTrue(self.change_words_instance.change_words(
            args.path, args.file_type, args.from_string, args.to_string))
        with open(os.path.join(self.test_dir, self.test_file), 'r') as f:
            content = f.read()
            self.assertIn(self.to_string, content)
            self.assertNotIn(self.from_string, content)
if __name__ == '__main__':
    unittest.main()