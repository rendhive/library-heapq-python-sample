import heapq

def dijkstra(graph, start):
    queue = []
    heapq.heappush(queue, (0, start))  # (cost, vertex)
    distances = {start: 0}
    
    while queue:
        current_distance, current_vertex = heapq.heappop(queue)
        
        for neighbor, weight in graph[current_vertex]:
            distance = current_distance + weight
            
            if neighbor not in distances or distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(queue, (distance, neighbor))

    return distances

# Contoh graf
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('C', 2), ('D', 5)],
    'C': [('D', 1)],
    'D': []
}

print("Jarak terpendek dari A:", dijkstra(graph, 'A'))
# Fungsi: Menemukan jarak terpendek menggunakan algoritma Dijkstra.
# Kondisi: Ketika Anda ingin menghitung rute terpendek pada graf.
