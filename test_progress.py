import unittest
from progress import completion_percent

class ProgressTests(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(completion_percent([]), 0.0)
    def test_half_done(self):
        self.assertEqual(completion_percent(["done", "todo"]), 50.0)
    def test_all_done(self):
        self.assertEqual(completion_percent(["done", "done"]), 100.0)
    def test_all_todo(self):
        self.assertEqual(completion_percent(["todo", "todo"]), 0.0)
    def test_rounding(self):
        self.assertEqual(completion_percent(["done", "todo", "todo"]), 33.3)
    def test_single_done(self):
        self.assertEqual(completion_percent(["done"]), 100.0)
    def test_invalid_status(self):
        with self.assertRaises(ValueError):
            completion_percent(["unknown"])
    def test_wrong_input_type(self):
        with self.assertRaises(TypeError):
            completion_percent("done")

if __name__ == "__main__":
    unittest.main()
