"""
def dfs(graph, start, visited=None):
	if visited == None:
		visited = []
	visited.append(start)
	for node in graph[start]- set(visited):
		if node not in visited:
		    dfs(graph, node, visited)
	return visited


graph = {
			'0': set(['1', '2']),
			'1': set(['0', '3', '4']),
			'2': set(['0']),
			'3': set(['1']),
			'4': set(['2', '3'])
		}

print(dfs(graph, '0'))
"""
class Graph():
	
	def DFS(self, graph):
		visited = []
		start = "0"
		def traversal(start):
			visited.append(start)
			for node in graph[start]- set(visited):
				if node not in visited:
				    traversal(node)
			return visited

		return traversal(start)

graph = {
			'0': set(['1', '2']),
			'1': set(['0', '3', '4']),
			'2': set(['0']),
			'3': set(['1']),
			'4': set(['2', '3'])
		}
obj = Graph()
print(obj.DFS(graph))

