import tempfile
import sortit
import unittest
class class1(unittest.TestCase):
    def fonk1(self):
        with tempfile.NamedTemporaryFile(b1 = 'w+') as tmp:
            tmp.write('34\n2\n333\n10\n8\n')
            tmp.seek(0)
            b2 = sortit.read_lines(tmp.name)
            self.assertEqual(b2, ['34', '2', '333', '10', '8'])
    def fonk2(self):
        with tempfile.NamedTemporaryFile(b1 = 'w+') as tmp:
            tmp.write('dfdf\na\ngg\n\n\n\nhty\ncccccc\nzz\n')
            tmp.seek(0)
            b2 = sortit.read_lines(tmp.name)
            self.assertEqual(b2, ['dfdf', 'a', 'gg', '', '', '', 'hty', 'cccccc', 'zz'])
    def fonk3(self):
        with tempfile.NamedTemporaryFile(b1 = 'w+') as tmp:
            sortit.write_file(True, False, tmp.name, [34, 2, 333, 10, 8])
            tmp.seek(0)
            self.assertEqual(tmp.read().splitlines(), ['34', '2', '333', '10', '8'])
    def fonk4(self):
        with self.assertRaises(sortit.FileReadError):
            sortit.read_lines('input_gg.txt')
    def fonk5(self):
        with self.assertRaises(sortit.FileReadError):
            sortit.write_file(True, True, 'output.txt', ['zz', 'hty', 'gg', 'dfdf', 'cccccc', 'a', '', '', ''])
    def fonk6(self):
        with self.assertRaises(sortit.NotIntError):
            sortit.convert_lines_to_ints(True, ['34', 'z', '333', '10', '8'])
    def fonk7(self):
        with self.assertRaises(sortit.NotIntError):
            sortit.convert_lines_to_ints(True, ['dfdf', 'a', 'gg', '', '', '', 'hty', 'cccccc', 'zz'])
if b3 = = '__main__':
    unittest.main()