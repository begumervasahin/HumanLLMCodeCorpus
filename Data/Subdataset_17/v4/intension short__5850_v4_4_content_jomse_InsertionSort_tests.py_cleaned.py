import unittest
import tempfile
import sortit
class SortItTests(unittest.TestCase):
    def test_read_lines_with_integers(self):
        with tempfile.NamedTemporaryFile(mode='w+') as tmp_file:
            tmp_file.write('34\n2\n333\n10\n8\n')
            tmp_file.seek(0)
            expected_lines = ['34', '2', '333', '10', '8']
            actual_lines = sortit.read_lines(tmp_file.name)
            self.assertEqual(actual_lines, expected_lines)
    def test_read_lines_with_strings(self):
        with tempfile.NamedTemporaryFile(mode='w+') as tmp_file:
            tmp_file.write('dfdf\na\ngg\n\n\n\nhty\ncccccc\nzz\n')
            tmp_file.seek(0)
            expected_lines = ['dfdf', 'a', 'gg', '', '', '', 'hty', 'cccccc', 'zz']
            actual_lines = sortit.read_lines(tmp_file.name)
            self.assertEqual(actual_lines, expected_lines)
    def test_file_writer_with_integers(self):
        with tempfile.NamedTemporaryFile(mode='w+') as tmp_file:
            sortit.write_file(sort_as_integers=True, allow_duplicates=False, file_name=tmp_file.name, data=[34, 2, 333, 10, 8])
            tmp_file.seek(0)
            written_lines = tmp_file.read().splitlines()
            expected_lines = ['34', '2', '333', '10', '8']
            self.assertEqual(written_lines, expected_lines)
    def test_read_lines_with_invalid_file(self):
        with self.assertRaises(sortit.FileReadError):
            sortit.read_lines('non_existent_file.txt')
    def test_write_file_with_invalid_data(self):
        with self.assertRaises(sortit.FileReadError):
            sortit.write_file(sort_as_integers=True, allow_duplicates=True, file_name='output.txt', data=['zz', 'hty', 'gg', 'dfdf', 'cccccc', 'a', '', '', ''])
    def test_convert_lines_to_integers_with_invalid_data(self):
        with self.assertRaises(sortit.NotIntError):
            sortit.convert_lines_to_ints(sort_as_integers=True, lines=['34', 'z', '333', '10', '8'])
    def test_convert_lines_to_integers_with_strings(self):
        with self.assertRaises(sortit.NotIntError):
            sortit.convert_lines_to_ints(sort_as_integers=True, lines=['dfdf', 'a', 'gg', '', '', '', 'hty', 'cccccc', 'zz'])
if __name__ == '__main__':
    unittest.main()