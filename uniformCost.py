import heapq
wEdges=[]
graph={}
vertices=input()
for i in vertices:
    graph[i]={}
edges = int(input("Enter the number of edges : "))
for i in range(edges):
    fromToP = input()
    s=""
    for i in fromToP[4:]:
        s+=i
    s.strip()
    beta=[fromToP[0],fromToP[2],int(s)]
    wEdges.append(beta)
# print(wEdges)
for u, v, dist in wEdges:
    graph[u][v]=dist
# print(graph)
print("Write start and goal state with space as a seperator ")
hello=input()

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
start = hello[0]
goal = hello[2]
came_from, cost_so_far = uniform_cost_search(graph, start, goal)
path = reconstruct_path(came_from, start, goal)
print("Hola!! The minimum cost is ",cost_so_far[goal],"\nThe least cost path is",path)

'''
11
v a 5
v b 8 
a b 2
a c 12
b d 6
b e 10
d c 3
d e 2
c f 5
d f 12
e f 7

7
A B 4
A C 2
B C 5
B D 10
C E 3
D F 11
E D 4
'''