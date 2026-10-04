import unittest
import tempfile
import sortit
class class1(unittest.TestCase):
    def fonk1(self):
        with tempfile.NamedTemporaryFile(b1 = 'w+') as tmp_file:
            tmp_file.write('34\n2\n333\n10\n8\n')
            tmp_file.seek(0)
            b2 = ['34', '2', '333', '10', '8']
            b3 = sortit.read_lines(tmp_file.name)
            self.assertEqual(b3, b2)
    def fonk2(self):
        with tempfile.NamedTemporaryFile(b1 = 'w+') as tmp_file:
            tmp_file.write('dfdf\na\ngg\n\n\n\nhty\ncccccc\nzz\n')
            tmp_file.seek(0)
            b2 = ['dfdf', 'a', 'gg', '', '', '', 'hty', 'cccccc', 'zz']
            b3 = sortit.read_lines(tmp_file.name)
            self.assertEqual(b3, b2)
    def fonk3(self):
        with tempfile.NamedTemporaryFile(b1 = 'w+') as tmp_file:
            sortit.write_file(b4 = True, allow_duplicates=False, file_name=tmp_file.name, data=[34, 2, 333, 10, 8])
            tmp_file.seek(0)
            b5 = tmp_file.read().splitlines()
            b2 = ['34', '2', '333', '10', '8']
            self.assertEqual(b5, b2)
    def fonk4(self):
        with self.assertRaises(sortit.FileReadError):
            sortit.read_lines('non_existent_file.txt')
    def fonk5(self):
        with self.assertRaises(sortit.FileReadError):
            sortit.write_file(b4 = True, allow_duplicates=True, file_name='output.txt', data=['zz', 'hty', 'gg', 'dfdf', 'cccccc', 'a', '', '', ''])
    def fonk6(self):
        with self.assertRaises(sortit.NotIntError):
            sortit.convert_lines_to_ints(b4 = True, lines=['34', 'z', '333', '10', '8'])
    def fonk7(self):
        with self.assertRaises(sortit.NotIntError):
            sortit.convert_lines_to_ints(b4 = True, lines=['dfdf', 'a', 'gg', '', '', '', 'hty', 'cccccc', 'zz'])
if b6 = = '__main__':
    unittest.main()