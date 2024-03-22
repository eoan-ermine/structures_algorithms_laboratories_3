import math


def bellman_shortest_path(graph, source, dest):
    n = len(graph)

    dist = [math.inf] * n
    dist[source] = 0

    for _ in range(n - 1):
        for u in range(n):
            for v in range(n):
                weight = graph[u][v]
                if weight != 0 and dist[u] != math.inf and dist[u] + weight < dist[v]:
                    dist[v] = dist[u] + weight

    return dist[dest]
