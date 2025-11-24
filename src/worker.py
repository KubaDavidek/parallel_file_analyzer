import os

def worker(worker_id, q, results, lock):
    while True:
        path = q.get()

        if path is None:
            q.task_done()
            break

        try:
            size = os.path.getsize(path)
            ext = os.path.splitext(path)[1].lower()

            with lock:
                results.append((path, size, ext))

        except:
            pass

        q.task_done()
