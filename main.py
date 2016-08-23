from Graph import *
from dfs_bfs import *
from shortest_paths import *
import cProfile,pstats



def Main():
    G=Graph()
    for id in range(0, 6):
        G.add_node(id,name=str(id))
    G.add_edge(0, 1, weight=5)
    G.add_edge(0, 4, weight=3)
    G.add_edge(0, 5, weight=2)
    G.add_edge(1, 3, weight=5)
    G.add_edge(1, 4, weight=4)
    G.add_edge(2, 1, weight=6)
    G.add_edge(3, 2, weight=7)
    G.add_edge(3, 4, weight=8)
    
    print "------------------------------------\n"
    print "Calculate DFS and BFS..."
    bfs(G)
    dfs(G)
    print
    bfs_path(G,0)
    dfs_path(G)
    print 
    Dijkstra(G,0)
    print
    Floyd_Warshall(G)
    
    print "\n------------------------------------"
    

    
    
    
    

if __name__ == '__main__':
   
    cProfile.run('Main()','log.txt')   
    p = pstats.Stats('log.txt')
    p.strip_dirs().sort_stats('calls').print_stats()   