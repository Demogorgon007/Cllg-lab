from itertools import permutations
from sys import maxsize


def Tsp(graph, startnode) :
    nodes = []
    path = []
    leng = len(graph)

    for i in range(leng) :
        if i != startnode :
            nodes.append(i)

    max_leng = maxsize
    next_permutation = permutations(nodes)

    for permutation in next_permutation :
        path_mes = 0
        s = startnode
        for element in permutation :
            path_mes += graph[s][element]
            s = element
        path.append(permutation)
        path_mes += graph[s][startnode]
        print(path_mes)
        print(path)

    if max_leng > path_mes :
        max_leng = path_mes
        path.append(permutation)


    return max_leng, path


graph = [[0, 5, 4, 1], [6, 0, 4, 9], [10, 11, 0, 13], [14, 6, 16, 0]]
startnode = 3
result = Tsp(graph, startnode)

print('Minimum cost : ', result[0])

for i in result[1] :
    print('path :', startnode, i, startnode)









