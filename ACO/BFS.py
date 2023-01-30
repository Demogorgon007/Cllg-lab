graph = {
    '5': ['6', '7'],
    '6': ['8', '9'],
    '7': ['10', '11'],
    '10': ['12', '13'],
    '8': [],
    '9': [],
    '12': [],
    '13': [],
    '11': []
}
print(graph)
visited = []
queue = []

def bfs(vis, graph, node):
  visited.append(node)
  queue.append(node)

  while queue:
    m = queue.pop(0)
    print (m, end = " ")

    for neighbour in graph[m]:
      if neighbour not in visited:
        visited.append(neighbour)
        queue.append(neighbour)

print("Following is the Breadth-First Search")
bfs(visited, graph, '7')


