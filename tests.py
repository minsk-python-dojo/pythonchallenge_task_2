import unittest

import task


class TestTask(unittest.TestCase):

    def test_shift_char_returns_shifted_char(self):
        input_char = 'K'
        expected_char = 'M'
        self.assertEqual(expected_char, task.shift_char(input_char))

        input_char = 'O'
        expected_char = 'Q'
        self.assertEqual(expected_char, task.shift_char(input_char))

        input_char = 'E'
        expected_char = 'G'
        self.assertEqual(expected_char, task.shift_char(input_char))

    def test_shift_char_returns_shifted_chars_from_edge_cases(self):
        input_char = 'Y'
        expected_char = 'A'
        self.assertEqual(expected_char, task.shift_char(input_char))

        input_char = 'Z'
        expected_char = 'B'
        self.assertEqual(expected_char, task.shift_char(input_char))


    def test_shift_string_returns_CDE_when_got_ABC(self):
        input_char = 'abc'
        expected_char = 'cde'
        self.assertEqual(expected_char, task.shift_string(input_char))


    def test_non_shift_special_symbols_returns_the_same_symbols(self):
        input_char = '.'
        expected_char = '.'
        self.assertEqual(expected_char, task.shift_char(input_char))

        input_char = ' '
        expected_char = ' '
        self.assertEqual(expected_char, task.shift_char(input_char))






