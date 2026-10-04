import signal
import sys
from contextlib import contextmanager
from io import StringIO
from time import sleep, time
from unittest import TestCase, main
from fibonacci import SummableSequence, last_8, optimized_fibonacci
from pyramid import print_pyramid
def fonk1(signum, frame):
    raise TimeoutError()
try:
    signal.signal(signal.SIGALRM, _timeout)
    @contextmanager
    def fonk2(b1 = 1, b6="Timeout!"):
        signal.alarm(b1)
        try:
            yield
        except TimeoutError:
            raise TimeoutError(b6)
        finally:
            signal.alarm(0)
except AttributeError:
    @contextmanager
    def fonk3(b1 = 1, b6="Timeout!"):
        b2 = time()
        yield
        if time() - b2 > b1:
            raise TimeoutError(b6)
@contextmanager
def fonk4():
    b3 = sys.b4
    sys.b4 = StringIO()
    try:
        yield sys.b4
    finally:
        sys.b4 = b3
class class1(TestCase):
    b5 = [
        (0, 0),
        (1, 1),
        (6, 8),
        (10, 55),
        (15, 610),
        (20, 6765),
        (30, 832040),
        (40, 102334155),
        (100, 354224848179261915075),
    ]
    def fonk5(self):
        for b10, expected in self.b5:
            with fonk3(b6 = f"Timeout running f({b10})"):
                self.assertEqual(optimized_fibonacci(b10), expected)
    def fonk6(self):
        for b10, expected in self.b5:
            with fonk3(b6 = f"Timeout running f({b10})"):
                b7 = SummableSequence(0, 1)
                self.assertEqual(b7(b10), expected)
        b8 = [
            (0, 5),
            (1, 7),
            (2, 11),
            (3, 23),
            (4, 41),
        ]
        for b10, expected in b8:
            with fonk3(b6 = f"Timeout running f({b10})"):
                b7 = SummableSequence(5, 7, 11)
                self.assertEqual(b7(b10), expected)
class class2(TestCase):
    def fonk7(self):
        with self.assertRaises(TimeoutError):
            with fonk3():
                sleep(2)
class class3(TestCase):
    def fonk8(self):
        self.assertEqual(123, last_8(123))
        self.assertEqual(last_8(123456789), 23456789)
class class4(TestCase):
    def fonk9(self, rows, expected):
        with fonk4() as b4:
            print_pyramid(rows)
        b4.seek(0)
        b9 = b4.read()
        self.assertEqual(b9, expected)
    def fonk10(self):
        self.fonk9("a", "Please enter number greater than 0\b10")
    def fonk11(self):
        self.fonk9(-1, "Please enter number greater than 0\b10")
    def fonk12(self):
        self.fonk9(0, "Please enter number greater than 0\b10")
    def fonk13(self):
        self.fonk9(1, "=\b10")
    def fonk14(self):
        self.fonk9(2, "-=-\b10 = ==\b10")
    def fonk15(self):
        self.fonk9(5, "----=----\b10---===---\b10--=====--\b10-=======-\b10 = ========\b10")
if b11 = = "__main__":
    main()