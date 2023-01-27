import heapq

graph = {'A': {'B': 2, 'C': 3},
         'B': {'D': 2, 'E': 4},
         'C': {'F': 5, 'G': 1},
         'D': {'H': 3},
         'E': {'H': 4},
         'F': {'H': 2},
         'G': {'H': 3},
         'H': {}}

def uniform_cost_search(graph, start, goal):
    frontier = []
    heapq.heappush(frontier, (0, start))
    came_from = {}
    cost_so_far = {}
    came_from[start] = None
    cost_so_far[start] = 0

    while frontier:
        current = heapq.heappop(frontier)[1]

        if current == goal:
            break

        for next in graph[current]:
            new_cost = cost_so_far[current] + graph[current][next]
            if next not in cost_so_far or new_cost < cost_so_far[next]:
                cost_so_far[next] = new_cost
                priority = new_cost
                heapq.heappush(frontier, (priority, next))
                came_from[next] = current

    return came_from, cost_so_far

def reconstruct_path(came_from, start, goal):
    current = goal
    path = [current]
    while current != start:
        current = came_from[current]
        path.append(current)
    path.reverse()
    return path

came_from, cost_so_far = uniform_cost_search(graph, 'A', 'H')
path = reconstruct_path(came_from, 'A', 'H')
print(cost_so_far,path)