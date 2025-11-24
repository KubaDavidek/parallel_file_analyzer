import os.path
from collections import defaultdict

def analyze(results):

    total_files = len(results)
    total_size = sum(r[1] for r in results)

    print(f"Počet nalezených souborů: {total_files}")
    print(f"Celková velikost: {total_size / (1024*1024):.2f} MB\n")

    print("TOP 10 největších souborů:")
    print("--------------------------")
    largest = sorted(results, key=lambda r: r[1], reverse=True)[:10]

    for path, size, i in largest:
        print(f"{size/1024/1024:8.2f} MB | {os.path.basename(path)}")
    print()


    ext_count = defaultdict(int)
    ext_size = defaultdict(int)

    for i, size, ext in results:
        ext_count[ext] += 1
        ext_size[ext] += size

    print("TOP 10 přípon podle počtu:")
    print("--------------------------")
    top_count = sorted(ext_count.items(), key=lambda kv: kv[1], reverse=True)[:10]
    for ext, count in top_count:
        print(f"{ext:8s} | {count}")
    print()

    print("TOP 10 přípon podle velikosti:")
    print("--------------------------")
    top_size = sorted(ext_size.items(), key=lambda kv: kv[1], reverse=True)[:10]
    for ext, size in top_size:
        print(f"{ext:8s} | {size/1024/1024:8.2f} MB")
    print()
