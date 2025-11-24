import unittest
from queue import Queue
from threading import Lock
from src.worker import worker
import os
import tempfile

class TestWorker(unittest.TestCase):

    def test_worker_processes_file(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = os.path.join(tmp, "file.txt")
            with open(path, "w") as f:
                f.write("hello")

            q = Queue()
            results = []
            lock = Lock()

            q.put(path)
            q.put(None)

            worker(0, q, results, lock)

            self.assertEqual(len(results), 1)
            self.assertEqual(results[0][2], ".txt")
            self.assertEqual(results[0][1], 5)

if __name__ == "__main__":
    unittest.main()
