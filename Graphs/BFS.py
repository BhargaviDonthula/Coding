from collections import deque

class Graph():	
	def BFS(self, graph):
		visited = []
		start = "0"
		queue = deque([start])
		visited.append(start)
		while(queue):
			current = queue.popleft()
			for neighbour in graph[current]:
				if neighbour not in visited:
					visited.append(neighbour)
					queue.append(neighbour)

		return visited



graph = {
			'0': set(['1', '2']),
			'1': set(['0', '3', '4']),
			'2': set(['0']),
			'3': set(['1']),
			'4': set(['2', '3'])
		}
obj = Graph()
print(obj.BFS(graph))

