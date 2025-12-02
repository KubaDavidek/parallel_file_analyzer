import os
from lib.duplicate_finder import find_duplicates_by_hash



TEMP_FOLDERS = [
    os.path.join(os.getenv("USERPROFILE"), "AppData", "Local", "Temp"),
    os.path.join(os.getenv("WINDIR"), "Temp"),
]

def analyze_files(results):
    print("\n===== ANALÝZA SOUBORŮ =====\n")

    total_files = len(results)
    total_size = sum(r[1] for r in results)

    print(f"Počet nalezených souborů: {total_files}")
    print(f"Celková velikost: {total_size / (1024*1024):.2f} MB\n")

    print("TOP 10 největších souborů:")
    print("--------------------------")
    largest = sorted(results, key=lambda r: r[1], reverse=True)[:10]

    for path, size, _ in largest:
        print(f"{size/1024/1024:8.2f} MB | {os.path.basename(path)}")
    print()

    ext_count = {}
    ext_size = {}

    for path, size, ext in results:
        if ext not in ext_count:
            ext_count[ext] = 0
        ext_count[ext] += 1

        if ext not in ext_size:
            ext_size[ext] = 0
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


def analyze_duplicates_by_hash(results):
    print("\n===== DUPLICITY PODLE HASH =====")
    print("--------------------------------")

    dupes = find_duplicates_by_hash(results)

    if not dupes:
        print("Žádné duplicity nenalezeny.\n")
        return

    for h, paths in dupes.items():
        print(f"\nHash: {h[:16]}... ({len(paths)} souborů)")
        for p in paths:
            print(f"  - {p}")
    print()

def analyze_temp():
    print("\n===== TEMP ANALÝZA =====")
    print("-------------------------")

    for folder in TEMP_FOLDERS:
        if not os.path.exists(folder):
            continue

        file_count = 0
        total_size = 0

        for root, dirs, files in os.walk(folder):
            for f in files:
                file_count += 1
                try:
                    total_size += os.path.getsize(os.path.join(root, f))
                except:
                    pass

        print(folder)
        print(f" - {file_count} souborů")
        print(f" - velikost: {total_size/1024/1024:.2f} MB\n")
