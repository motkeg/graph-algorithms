
from Graph import *




time =0 

def bfs_path(G,s,q=False):

    color ,d , pi = G.get_nodes().copy(),G.get_nodes().copy(),G.get_nodes().copy()
        
    
    #init
    for v in G.get_nodes():
        d[v]=0
        color[v]='W'
        
    # init s
    stack=[s]
    d[s]=0
    color[s]='G'
    
    while stack:
        u = stack.pop()
        for v in G. getAdj(u):
            if color[v]=='W':
                color[v]='G'
                d[v]=int(d[u])+1
                pi[v]=u
                stack.append(v)
                
        color[u]='B'
    if not q:    
        print "(BFS)Shortest Path from '" + str(s) +"' : " ,d    
    return {'distance':d,'pi':pi}            
                


 
 
def dfs_path(G,q=False):
    
    color ,d,f, pi = G.get_nodes().copy(),G.get_nodes().copy(),G.get_nodes().copy(),G.get_nodes().copy()
    end={}
    
    def visit(G,u):
        color[u]="G"
        global time
        time += 1
        d[u]=time
        for v in G.getAdj(u):
            if (color[v]=='W'):
                pi[v]=u
                visit(G, v)
            
        time += 1
        f[u]=time
        end[u]=(d[u],f[u])
        color[u]="B"    
                        
     ##############################################   
    
    
    # init
    for v in G.get_nodes():
        color[v]='W'
        
    for u in  G.get_nodes():
        if (color[u]=='W'): visit(G, u)
    
    
    
    
    if not q:
        print "\n(DFS)Shortest Path of graph:"  
        print "time: " ,str(end)
        print "pi: " ,str(pi)   
    return {'time':end,'pi':pi}                       
    
    


def Dijkstra(G,s):
    d,pi =  G.get_nodes().copy() ,G.get_nodes().copy()
    w =G.get_edges().copy()
    stack=[]
    
    def Relax(u,v,w):
        if (d[v] > d[u] + w[(u,v)]):
            d[v] = d[u] + w[(u,v)]
            pi[v]=u
            
            
    for v in d:
        d[v]=10000000000000000000000000
        
    d[s]=0
    Heap = d.copy()
    
    while Heap:
        u = min(Heap, key=Heap.get)
        stack.append(u)
        for v in G.getAdj(u):
            Relax(u, v, w)
            Heap = d.copy()
        for k in stack:
            if k in Heap.keys():    
                Heap.pop(k)
    
    
    
    print "Dijkstra path  result  from '" ,str(s)+"': " ,str(d) 
    return d
    
         
    
def Floyd_Warshall(G):
    pi=[]
    D=[]
    n=len(G.get_nodes().copy())
    w =G.get_edges().copy()
    
    # init 
    for i in xrange(n):
        pi_temp=[]
        D_temp=[]
        for j in xrange(n):
            if (i,j) in w.keys():
                pi_temp.append(i)
                D_temp.append(w[(i,j)])
            else:
                pi_temp.append('X')
                D_temp.append(10000000000000000000000000)
                
        pi.append(pi_temp)
        D.append(D_temp)        
    
                    
    for i in xrange(n):
        for j in xrange(n):
            for k in xrange(n):   
                if (D[i][j] <= D[i][k] +D[k][j]):
                    D[i][j]=D[i][j]
                    pi[i][j]=pi[i][j]
                else:
                    D[i][j]=D[i][k] +D[k][j]
                    pi[i][j]=pi[k][j]
    
    
    
    # set good looking 
    for i in xrange(n):
        for j in xrange(n):
            if D[i][j]==10000000000000000000000000:
                D[i][j]='X'
               
        print D[i]
       
    return {'dist':D,'pi':pi}                     
           
   
    
    
