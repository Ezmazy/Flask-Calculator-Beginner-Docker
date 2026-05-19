import unittest
from logic import check_posted_data


class TestCalculatorLogic(unittest.TestCase):

    def test_add_valid(self):
        result = check_posted_data({"x": 184, "y": 323}, "add")
        self.assertEqual(result, 200)

    def test_add_missing_param(self):
        result = check_posted_data({"x": 142}, "add")
        self.assertEqual(result, 301)

    def test_division_valid(self):
        result = check_posted_data({"x": 184, "y": 323}, "division")
        self.assertEqual(result, 200)

    def test_division_by_zero(self):
        result = check_posted_data({"x": 143, "y": 0}, "division")
        self.assertEqual(result, 302)

    def test_division_missing_param(self):
        result = check_posted_data({"x": 142}, "division")
        self.assertEqual(result, 301)

    def test_subtract_valid(self):
        result = check_posted_data({"x": 10, "y": 3}, "subtract")
        self.assertEqual(result, 200)

    def test_multiply_valid(self):
        result = check_posted_data({"x": 5, "y": 6}, "multiply")
        self.assertEqual(result, 200)


if __name__ == "__main__":
    unittest.main()
