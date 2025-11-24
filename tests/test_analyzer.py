import unittest


class TestAnalyzer(unittest.TestCase):

    def test_extension_counting(self):
        results = [
            ("file1.txt", 10, ".txt"),
            ("file2.txt", 20, ".txt"),
            ("file3.jpg", 30, ".jpg"),
        ]

        expected_counts = {
            ".txt": 2,
            ".jpg": 1
        }

        ext_count = {}
        for _, _, ext in results:
            ext_count[ext] = ext_count.get(ext, 0) + 1

        self.assertEqual(ext_count, expected_counts)

if __name__ == "__main__":
    unittest.main()
