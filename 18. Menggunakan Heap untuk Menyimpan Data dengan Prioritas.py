import heapq

class PriorityDataStore:
    def __init__(self):
        self.store = []

    def store_data(self, data, priority):
        heapq.heappush(self.store, (priority, data))

    def retrieve_highest_priority(self):
        return heapq.heappop(self.store)[1]

data_store = PriorityDataStore()
data_store.store_data('data1', 3)
data_store.store_data('data2', 1)

print("Data dengan prioritas tertinggi:", data_store.retrieve_highest_priority())
# Fungsi: Menyimpan dan mengambil data berdasarkan prioritas.
# Kondisi: Ketika Anda ingin menyimpan berbagai item dan mengambil item berdasarkan urutan prioritas.
