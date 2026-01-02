import heapq

class PriorityQueue:
    def __init__(self):
        self.elements = []

    def push(self, item, priority):
        heapq.heappush(self.elements, (priority, item))

    def pop(self):
        return heapq.heappop(self.elements)[1]

pq = PriorityQueue()
pq.push('task1', 2)
pq.push('task2', 1)
print("Proses berdasarkan prioritas:")
print(pq.pop())
# Fungsi: Implementasi antrian prioritas menggunakan heap.
# Kondisi: Ketika Anda perlu mengelola tugas dengan prioritas.
