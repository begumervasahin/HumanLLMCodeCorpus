import unittest
def check_pesel(pesel_nr):
    if len(pesel_nr) != 11:
        return False
    if not pesel_nr.isdigit():
        return False
    weights = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3]
    total_sum = sum(int(pesel_nr[i]) * weights[i] for i in range(10))
    check_digit = (10 - (total_sum % 10)) % 10
    return check_digit == int(pesel_nr[-1])
class TestPeselValidator(unittest.TestCase):
    def test_valid_pesel(self):
        self.assertTrue(check_pesel("92121510595"))
        self.assertTrue(check_pesel("99810235403"))
    def test_invalid_pesel(self):
        self.assertFalse(check_pesel("44051401358"))
        self.assertFalse(check_pesel("51401358"))
        self.assertFalse(check_pesel("12345678901"))
if __name__ == "__main__":
    unittest.main()