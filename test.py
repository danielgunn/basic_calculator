import unittest
from stack import Stack
from main import evaluate_expression

class Test(unittest.TestCase):
    def test_fifo(self):
        s = Stack()
        for i in range(1, 100, 2):
            s.push(i)

        for i in range(99, 1, -2):
            self.assertEqual(i, s.pop())

    def test_calc1(self):
        self.assertEqual(evaluate_expression("1 + 1"),2)
        self.assertEqual(evaluate_expression("2 * 3 + 4"), 10)
        self.assertEqual(evaluate_expression("2 + 3 * 4"), 14)
        self.assertEqual(evaluate_expression("( 2 + 3 ) * 4"), 20)


if __name__ == '__main__':
    unittest.main()
