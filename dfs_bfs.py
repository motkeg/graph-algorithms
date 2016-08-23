def dfs(G):
    visit, stack = [],[0]
    while (stack):
        v=stack.pop()
        if(v not in visit):
            visit.append(v)
            for u in G.getAdj(v,True):
                stack.append(u)        
               
    print "DFS result:", visit 
    return visit      
    
def bfs(G):
    L ,visit=[0] ,[]
    while L:
        v=L[0]
        if(v not in visit):
            visit.append(v)
            for u in G.getAdj(v):
                if u not in visit:
                    L.append(u)
        L = L[1:]
    print "BFS result:", visit
    return visit