import heapq

class Smallest:
    def __init__(self):
        self.data = []

    def add(self, val):
        heapq.heappush(self.data, val)

    def get_smallest(self):
        return self.data[0] if self.data else None

smallest_tracker = Smallest()
smallest_tracker.add(5)
smallest_tracker.add(1)
smallest_tracker.add(3)

print("Elemen terkecil saat ini:", smallest_tracker.get_smallest())
# Fungsi: Menyimpan dan mengelola elemen terkecil dari kumpulan data secara terus menerus.
# Kondisi: Ketika Anda perlu melacak nilai terkecil secara dinamis saat nilai baru ditambahkan.
