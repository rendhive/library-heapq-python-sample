import heapq

numbers = [1, 5, 3, 7, 2, 8]
smallest = heapq.nsmallest(3, numbers)

print("Tiga angka terkecil:", smallest)
# Fungsi: Mengambil n elemen terkecil dari list.
# Kondisi: Ketika Anda ingin menemukan elemen dengan nilai terendah dari koleksi.
