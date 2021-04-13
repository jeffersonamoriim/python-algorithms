import numpy as np

vertices = {'arad': 0, 'zerind': 1, 'oradea': 2, 'sibiu': 3, 'timisoara': 4,
            'lugoj': 5, 'mehadia': 6, 'dobreta': 7, 'craiova': 8, 'rimnicu': 9,
            'fagaras': 10, 'pitesti': 11, 'bucharest': 12, 'giurgiu': 13}

cities = {0: 'arad', 1: 'zerind', 2: 'oradea', 3: 'sibiu', 4: 'timisoara',
          5: 'lugoj', 6: 'mehadia', 7: 'dobreta', 8: 'craiova', 9: 'rimnicu',
          10: 'fagaras', 11: 'pitesti', 12: 'bucharest', 13: 'giurgiu'}

edges = np.zeros([len(cities), len(cities)], dtype=int)

edges[vertices['arad'], [vertices['zerind']]] = 75
edges[vertices['arad'], [vertices['sibiu']]] = 140
edges[vertices['arad'], [vertices['timisoara']]] = 118

edges[vertices['zerind'],[vertices['arad']]] = 75
edges[vertices['zerind'],[vertices['oradea']]] = 71

edges[vertices['oradea'],[vertices['zerind']]] = 71
edges[vertices['oradea'],[vertices['sibiu']]] = 151

edges[vertices['sibiu'],[vertices['oradea']]] = 151
edges[vertices['sibiu'],[vertices['arad']]] = 140
edges[vertices['sibiu'],[vertices['fagaras']]] = 99
edges[vertices['sibiu'],[vertices['rimnicu']]] = 80

edges[vertices['timisoara'],[vertices['arad']]] = 118
edges[vertices['timisoara'],[vertices['lugoj']]] = 111

edges[vertices['lugoj'],[vertices['timisoara']]] = 111
edges[vertices['lugoj'],[vertices['mehadia']]] = 70

edges[vertices['mehadia'],[vertices['lugoj']]] = 70
edges[vertices['mehadia'],[vertices['dobreta']]] = 75

edges[vertices['dobreta'],[vertices['mehadia']]] = 75
edges[vertices['dobreta'],[vertices['craiova']]] = 120

edges[vertices['craiova'],[vertices['dobreta']]] = 120
edges[vertices['craiova'],[vertices['pitesti']]] = 138
edges[vertices['craiova'],[vertices['rimnicu']]] = 146

edges[vertices['rimnicu'],[vertices['craiova']]] = 146
edges[vertices['rimnicu'],[vertices['sibiu']]] = 80
edges[vertices['rimnicu'],[vertices['pitesti']]] = 97

edges[vertices['fagaras'],[vertices['sibiu']]] = 99
edges[vertices['fagaras'],[vertices['bucharest']]] = 211

edges[vertices['pitesti'],[vertices['rimnicu']]] = 97
edges[vertices['pitesti'],[vertices['craiova']]] = 138
edges[vertices['pitesti'],[vertices['bucharest']]] = 101

edges[vertices['bucharest'],[vertices['fagaras']]] = 211
edges[vertices['bucharest'],[vertices['pitesti']]] = 101
edges[vertices['bucharest'],[vertices['giurgiu']]] = 90


v = [item for item in vertices]

print(v)
print(edges)

import sys

class Dijkstra:

    def __init__(self, vertices, edges, start):
        self.size = len(edges)
        self.vertices = vertices
        self.fork = edges
        self.start = start

    def show_solution(self, distances):
        print("Best distances between {} to all the others".format(self.vertices[self.start]))
        for vertice in range(self.size):
            print(self.vertices[vertice], distances[vertice])

    def minimun_distance(self, distance, visited):
        minimun = sys.maxsize
        for vertice in range(self.size):
            if distance[vertice] < minimun and visited[vertice] == False:
                minimun = distance[vertice]
                index_minimun = vertice
        return index_minimun

    def dijkstra(self):
        distance = [sys.maxsize] * self.size
        distance[self.start] = 0
        visited = [False] * self.size

        for _ in range(self.size):
            minimun_index = self.minimun_distance(distance, visited)
            visited[minimun_index] = True
            for vertice in range(self.size):
                if self.fork[minimun_index][vertice] > 0 and visited[vertice] == False \
                    and distance[vertice] > distance[minimun_index] + self.fork[minimun_index][vertice]:
                    distance[vertice] = distance[minimun_index] + self.fork[minimun_index][vertice]

        self.show_solution(distance)

dijkstra = Dijkstra(cities, edges, vertices['arad'])
dijkstra.dijkstra()
