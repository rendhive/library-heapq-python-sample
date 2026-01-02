import heapq

numbers = [10, 25, 30, 5, 15]
heapq.heapify(numbers)

print("Tiga angka terkecil:")
for _ in range(3):
    print(heapq.heappop(numbers), end=' ')
# Fungsi: Mengambil sejumlah elemen terkecil dari heap.
# Kondisi: Ketika Anda perlu mengambil beberapa item dengan nilai terkecil dari koleksi yang memiliki banyak nilai.
