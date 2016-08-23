
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
        print "(BFS)Shortest "+G.name+ " Path from '" + str(s) +"' : " ,d    
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
        print "\n(DFS)Shortest Path of graph "+G.name+" :"  
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
    
    
    
    print "Dijkstra for "+ G.name+ " path  result  from '" ,str(s)+"': " ,str(d) 
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
    print "(Floyd-Warshall for "+G.name+" :\n"
    for i in xrange(n):
        for j in xrange(n):
            if D[i][j]==10000000000000000000000000:
                D[i][j]='X'
               
        print D[i]
       
    return {'dist':D,'pi':pi}                     




           
def Edmond_Karp(G,s,t):
    N={'G':G,'C':G.get_edges().copy()}
    f={}
    total=0
    Nf=N.copy()
    Cf=N.copy()
    
    print "----------------------(Edmond_Karp)-----------------\n"
    def getPath(G,s,t):
        p={}
        bfs=bfs_path(G,s)
        target=bfs['pi'][t]
        if int(target)!=int(t):
            while int(target) != int(t):
                p[(target,t)]=G.get_edges()[(target,t)]
                t=target
                target=bfs['pi'][t]
                
            return p
        else:
            return {}
        
    
    for e in G.get_edges().copy().keys():
        f[e]=0
        f[(e[1],e[0])]=0
       
        
    i=0    
    p=getPath(Nf['G'], s, t)
    while len(p.keys())>0:
        i+=1
        cf_e=min(p, key=p.get)
        cf=Nf['C'][cf_e]
        total+=cf
        print "P"+str(i)+":" ,p
        
        for e in p.keys():
            f[e] = f[e]+cf
            f[(e[1],e[0])] = int(f[(e[1],e[0])]) -cf
            
            Nf['G'].remove_edge(e)
            Nf['G'].add_edge(e[0],e[1],Nf['C'][e]-cf)
            Nf['C'][e]=Nf['C'][e]-cf
            
            if Nf['C'][e]==0:
                 Nf['G'].remove_edge(e)
                       
            if (e[1],e[0]) not in Nf['C'].keys():
                Nf['C'][(e[1],e[0])] = cf
                Nf['G'].add_edge(e[1],e[0],cf)
            else:
                
                Nf['G'].add_edge(e[1],e[0],Nf['C'][(e[1],e[0])]+cf)
                Nf['C'][(e[1],e[0])] =Nf['C'][(e[1],e[0])]+ cf
                
            p=getPath(Nf['G'], s, t) 
       
        
    print "Edmonds-Karp: {graph name}:" +G.name+ " [Path: from {0} to {1} [max flow] = {2} ]".format(s,t,total)
    
    print "\n----------------------(Edmond_Karp)------------------------------"
    return f    
               
            
   
    
    
