# hw04/main.py

from collections import deque

def bipartition(graph):
    """
    Return a tuple (left_set, right_set) if the graph is bipartite.
    If not bipartite, return None.
    """
    color = {}
    left_set = set()
    right_set = set()

    for node in graph:
        if node not in color:
            queue = deque([node])
            color[node] = 0  # Start coloring with 0
            left_set.add(node)

            while queue:
                u = queue.popleft()
                for v in graph.get(u, []):
                    if v not in color:
                        # Assign opposite color
                        color[v] = 1 - color[u]
                        queue.append(v)
                        if color[v] == 0:
                            left_set.add(v)
                        else:
                            right_set.add(v)
                    elif color[v] == color[u]:
                        # Same color neighbor -> not bipartite
                        return None

    return (left_set, right_set)
