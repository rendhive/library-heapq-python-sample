import heapq

numbers = [8, 4, 6, 2, 9]
heapq.heapify(numbers)

sorted_numbers = [heapq.heappop(numbers) for _ in range(len(numbers))]

print("Daftar terurut:", sorted_numbers)
# Fungsi: Mengurutkan list dengan menggunakan heap.
# Kondisi: Ketika Anda ingin mengurutkan daftar tanpa menggunakan fungsi sort standard.
