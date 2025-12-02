import time
import threading
from queue import Queue

from conf.config import ROOT_FOLDER, NUM_WORKERS
from src.producer import producer
from src.worker import worker
from src.analyzer import analyze_files, analyze_duplicates_by_hash, analyze_temp


def main():
    print("\nVyberte akci:")
    print("1) Analýza souborů")
    print("2) Duplicity")
    print("3) TEMP analýza")

    choice = input("\nZadejte volbu (1–3): ")

    if choice == "3":
        analyze_temp()
        return

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

    if choice == "1":
        analyze_files(results)
    elif choice == "2":
        analyze_duplicates_by_hash(results)
    else:
        print("Neplatná volba.")

    end_time = time.time()
    print(f"\nCelkový čas běhu programu: {end_time - start_time:.2f} s")


if __name__ == "__main__":
    main()
