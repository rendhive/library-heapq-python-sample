import heapq

class TopN:
    def __init__(self, n):
        self.n = n
        self.heap = []

    def add(self, val):
        if len(self.heap) < self.n:
            heapq.heappush(self.heap, val)
        else:
            heapq.heappushpop(self.heap, val)  # push and pop smallest if current size exceeds n

top_n_tracker = TopN(3)
top_n_tracker.add(3)
top_n_tracker.add(1)
top_n_tracker.add(5)
top_n_tracker.add(2)
top_n_tracker.add(4)

print("Top 3 elemen terbesar:", top_n_tracker.heap)
# Fungsi: Menyimpan hanya elemen terbesar dalam ukuran tetap.
# Kondisi: Ketika Anda ingin menjaga n elemen terbesar dari kumpulan data yang mengalir.
