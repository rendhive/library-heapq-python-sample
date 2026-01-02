import heapq

processes = []
heapq.heappush(processes, (1, 'Process 1'))  # (priority, 'name')
heapq.heappush(processes, (3, 'Process 3'))
heapq.heappush(processes, (2, 'Process 2'))

print("Proses berdasarkan prioritas:")
while processes:
    print(heapq.heappop(processes)[1])
# Fungsi: Mengambil elemen proses berdasarkan prioritas.
# Kondisi: Ketika Anda perlu mengelola eksekusi proses berdasarkan urutan prioritas.
