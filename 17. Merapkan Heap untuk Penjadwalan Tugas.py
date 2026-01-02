import heapq
import time

class TaskScheduler:
    def __init__(self):
        self.tasks = []

    def add_task(self, task_name, time_to_run):
        run_time = time.time() + time_to_run
        heapq.heappush(self.tasks, (run_time, task_name))

    def run_tasks(self):
        while self.tasks:
            run_time, task_name = heapq.heappop(self.tasks)
            wait_time = run_time - time.time()
            if wait_time > 0:
                time.sleep(wait_time)
            print(f"Running: {task_name}")

scheduler = TaskScheduler()
scheduler.add_task('Task 1', 2)
scheduler.add_task('Task 2', 1)

print("Menjalankan tugas dalam urutan waktu:")
scheduler.run_tasks()
# Fungsi: Menjadwalkan dan menjalankan tugas berdasarkan waktu eksekusi.
# Kondisi: Ketika Anda ingin mengatur dan mengelola tugas berdasarkan waktu yang dijadwalkan.
