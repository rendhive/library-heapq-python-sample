import heapq

tasks = [(5, 'Clean the house'), (1, 'Wake up'), (4, 'Do the dishes')]

heapq.heapify(tasks)
print("Daftar tugas berdasarkan prioritas:")
while tasks:
    priority, task = heapq.heappop(tasks)
    print(f"Priority {priority}: {task}")
# Fungsi: Mengelola daftar tugas berdasarkan prioritas.
# Kondisi: Ketika Anda ingin mengelola tugas dengan urutan prioritas.
