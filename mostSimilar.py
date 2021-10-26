from collections import defaultdict, deque
def mostSimilar(n, roads, names, targetPath):
    
    # Build original graph (undirected)
    graph = defaultdict(list)
    for a, b in roads:
        graph[a].append(b)
        graph[b].append(a)
        
    graph[None] = range(n) # add a sentinel node for convinience, so the path will always start with 'None'
    que = deque([]) # processing queue
    que.append([None]) # push the sentinel node in tue que
    
    L = len(targetPath)
    
    visited = [[False] * n for _ in range(L)] # table to store visited node at each path lengh
    
    # find shortest distance at length L
    while que:
        path = que.popleft()
        
        k = len(path) - 1 # exclude the 'None' in path
        
        if k == L:
            return path[1:] # reached the path with minimum edit distance
        
        for child in graph[path[-1]]:
            if visited[k][child] is False: # only visite child at length k once
                visited[k][child] = True
                if names[child] == targetPath[k]: # weight 0 edge, high priority
                    que.appendleft(path + [child])
                else: # weight 1 edge, low priority
                    que.append(path + [child])
