import heapq
import time

class TimingTracker:
    def __init__(self):
        self.timings = []

    def add_timing(self, task_name):
        start_time = time.time()
        heapq.heappush(self.timings, (start_time, task_name))

    def finish_timing(self):
        start_time, task_name = heapq.heappop(self.timings)
        elapsed_time = time.time() - start_time
        print(f"Task '{task_name}' finished in {elapsed_time:.2f} seconds.")

tracker = TimingTracker()
tracker.add_timing("Sleep 3s")
time.sleep(3)
tracker.finish_timing()
# Fungsi: Melacak waktu durasi eksekusi tugas.
# Kondisi: Ketika Anda perlu memonitor waktu eksekusi tugas.
