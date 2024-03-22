import math

import graphviz


def read_square_matrix(file_path):
    with open(file_path, "r") as file:
        lines = file.readlines()
        n = len(lines)
        matrix = [[0 for _ in range(n)] for _ in range(n)]

        for i in range(n):
            row = list(map(int, lines[i].split()))
            for j in range(n):
                if row[j] == 0:
                    matrix[i][j] = math.inf
                else:
                    matrix[i][j] = row[j]

        return matrix


def create_graph(matrix):
    dot = graphviz.Digraph(graph_attr={"rankdir": "LR"})
    n = len(matrix)

    for i in range(n):
        dot.node(str(i))

    for i in range(n):
        for j in range(n):
            if matrix[i][j] != math.inf:
                dot.edge(str(i), str(j), label=str(matrix[i][j]))

    return dot
