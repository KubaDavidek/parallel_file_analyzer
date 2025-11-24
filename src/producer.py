import os
from conf.config import NUM_WORKERS

def producer(root, q):
    for folder, dirs, files in os.walk(root):
        for f in files:
            q.put(os.path.join(folder, f))

    for i in range(NUM_WORKERS):
        q.put(None)
