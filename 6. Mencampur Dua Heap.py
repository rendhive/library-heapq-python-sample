import heapq

heap1 = [1, 3, 5]
heap2 = [2, 4, 6]

merged_heap = heapq.merge(heap1, heap2)

print("Gabungan dua heap:")
print(list(merged_heap))
# Fungsi: Menggabungkan dua heap menjadi satu heap yang terurut.
# Kondisi: Ketika Anda perlu menggabungkan dua kumpulan data terurut.
