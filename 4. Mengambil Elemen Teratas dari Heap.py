import heapq

heap = [1, 2, 5, 3]
smallest = heapq.heappop(heap)

print("Elemen terkecil yang diambil dari heap:", smallest)
print("Heap setelah penghapusan:", heap)
# Fungsi: Mengambil dan menghapus elemen teratas (terkecil) dari heap.
# Kondisi: Ketika Anda ingin mendapatkan elemen terkecil dari heap.
