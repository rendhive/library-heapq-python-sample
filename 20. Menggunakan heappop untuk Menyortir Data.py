import heapq

numbers = [15, 20, 10, 5, 25]
heapq.heapify(numbers)

sorted_numbers = []
while numbers:
    sorted_numbers.append(heapq.heappop(numbers))

print("Daftar yang terurut:", sorted_numbers)
# Fungsi: Mengurutkan data dengan menggunakan heap.
# Kondisi: Ketika Anda ingin mengurutkan koleksi tanpa menggunakan metode sorting lainnya.
