import time
import threading
from queue import Queue

from conf.config import ROOT_FOLDER, NUM_WORKERS
from src.producer import producer
from src.worker import worker
from src.analyzer import analyze


def main():
    start_time = time.time()

    print("\n===== ANALÝZA SOUBORŮ =====\n")
    print("Analyzuji...\n")

    q = Queue()
    results = []
    lock = threading.Lock()

    producer_thread = threading.Thread(target=producer, args=(ROOT_FOLDER, q))
    producer_thread.start()

    workers = []
    for i in range(NUM_WORKERS):
        t = threading.Thread(target=worker, args=(i, q, results, lock))
        t.start()
        workers.append(t)

    producer_thread.join()
    q.join()

    for t in workers:
        t.join()

    analyze(results)

    end_time = time.time()
    print(f"\nCelkový čas běhu programu: {end_time - start_time:.2f} s")


if __name__ == "__main__":
    main()
