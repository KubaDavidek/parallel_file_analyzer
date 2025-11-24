import unittest
from queue import Queue
from src.producer import producer
import tempfile
import os

class TestProducer(unittest.TestCase):

    def test_producer_puts_files(self):
        with tempfile.TemporaryDirectory() as tmp:
            file1 = os.path.join(tmp, "a.txt")
            with open(file1, "w") as f:
                f.write("X")

            q = Queue()
            producer(tmp, q)

            found = []
            while not q.empty():
                p = q.get()
                if p is not None:
                    found.append(os.path.basename(p))

            self.assertIn("a.txt", found)

if __name__ == "__main__":
    unittest.main()
