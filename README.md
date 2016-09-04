# graph-algorithms
High level algrorithms for computer Science

language: `python 2.7`.  
Realized algorithms:
* **simple BFS**
* **simple DFS**
* **BFS for shorter path**
* **DFS for shorter path**
* **Dijkstra**
* **Floyd-Warshall**  
* **Edmonds-Karp** 


**_you can live a comment for ask a realization of algorithm that not include in the list_** 

**OutPut**
```
------------------------------------

Calculate DFS and BFS...
BFS result: [0, 1, 4, 5, 3, 2]
DFS result: [0, 1, 3, 2, 4, 5]
                  End                 

(BFS)Shortest G1 Path from '0' :  {0: 0, 1: 1, 2: 3, 3: 2, 4: 1, 5: 1}

(DFS)Shortest Path of graph G1 :
time:  {0: (1, 12), 1: (2, 9), 2: (4, 5), 3: (3, 8), 4: (6, 7), 5: (10, 11)}
pi:  {0: '0', 1: 0, 2: 3, 3: 1, 4: 3, 5: 0}

Dijkstra for G1 path  result  from ' 0':  {0: 0, 1: 5, 2: 17, 3: 10, 4: 3, 5: 2}

(Floyd-Warshall for G1 :

['X', 5, 'X', 10, 3, 2]
['X', 'X', 12, 5, 4, 'X']
['X', 6, 18, 11, 10, 'X']
['X', 13, 7, 18, 8, 'X']
['X', 'X', 'X', 'X', 'X', 'X']
['X', 'X', 'X', 'X', 'X', 'X']

----------------------(Edmond_Karp)-----------------

(BFS)Shortest G1 Path from '0' :  {0: 0, 1: 1, 2: 3, 3: 2, 4: 1, 5: 1}
P1: {(0, 1): 5, (3, 2): 7, (1, 3): 5}
remove (0, 1)
remove Adj 1 of - 0
remove (0, 1)
remove Adj 1 of - 0
(BFS)Shortest G1 Path from '0' :  {0: 0, 1: 0, 2: 0, 3: 0, 4: 1, 5: 1}
remove (3, 2)
remove Adj 2 of - 3
(BFS)Shortest G1 Path from '0' :  {0: 0, 1: 0, 2: 0, 3: 0, 4: 1, 5: 1}
remove (1, 3)
remove Adj 3 of - 1
remove (1, 3)
remove Adj 3 of - 1
(BFS)Shortest G1 Path from '0' :  {0: 0, 1: 0, 2: 0, 3: 0, 4: 1, 5: 1}
Edmonds-Karp: {graph name}:G1 [Path: from 0 to 2 [max flow] = 5 ]

----------------------(Edmond_Karp)------------------------------

----------------------(Edmond_Karp)-----------------

(BFS)Shortest G2 Path from '0' :  {0: 0, 1: 1, 2: 1, 3: 2}
P1: {(2, 3): 4, (0, 2): 2}
remove (2, 3)
remove Adj 3 of - 2
(BFS)Shortest G2 Path from '0' :  {0: 0, 1: 1, 2: 1, 3: 2}
remove (0, 2)
remove Adj 2 of - 0
remove (0, 2)
remove Adj 2 of - 0
(BFS)Shortest G2 Path from '0' :  {0: 0, 1: 1, 2: 2, 3: 2}
P2: {(0, 1): 3, (1, 3): 2}
remove (0, 1)
remove Adj 1 of - 0
(BFS)Shortest G2 Path from '0' :  {0: 0, 1: 1, 2: 2, 3: 2}
remove (1, 3)
remove Adj 3 of - 1
remove (1, 3)
remove Adj 3 of - 1
(BFS)Shortest G2 Path from '0' :  {0: 0, 1: 1, 2: 2, 3: 3}
P3: {(1, 2): 2, (0, 1): 1, (2, 3): 2}
remove (1, 2)
remove Adj 2 of - 1
(BFS)Shortest G2 Path from '0' :  {0: 0, 1: 1, 2: 2, 3: 3}
remove (0, 1)
remove Adj 1 of - 0
remove (0, 1)
remove Adj 1 of - 0
(BFS)Shortest G2 Path from '0' :  {0: 0, 1: 0, 2: 0, 3: 0}
remove (2, 3)
remove Adj 3 of - 2
(BFS)Shortest G2 Path from '0' :  {0: 0, 1: 0, 2: 0, 3: 0}
Edmonds-Karp: {graph name}:G2 [Path: from 0 to 3 [max flow] = 5 ]

----------------------(Edmond_Karp)------------------------------



```


**Run-Time :**
```
-------------------Run Time-----------------------------
Tue Aug 23 22:55:10 2016    log.txt

         722 function calls (717 primitive calls) in 0.004 seconds

   Ordered by: call count

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
      183    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
       79    0.000    0.000    0.000    0.000 {method 'keys' of 'dict' objects}
       71    0.000    0.000    0.000    0.000 Graph.py:31(getAdj)
       65    0.000    0.000    0.000    0.000 {method 'copy' of 'dict' objects}
       61    0.000    0.000    0.000    0.000 Graph.py:19(get_nodes)
       56    0.000    0.000    0.000    0.000 {method 'pop' of 'list' objects}
       33    0.000    0.000    0.000    0.000 Graph.py:15(add_edge)
       33    0.000    0.000    0.000    0.000 {method 'pop' of 'dict' objects}
       23    0.000    0.000    0.000    0.000 Graph.py:22(get_edges)
       15    0.000    0.000    0.000    0.000 {method 'remove' of 'list' objects}
       15    0.001    0.000    0.001    0.000 Graph.py:25(remove_edge)
       13    0.001    0.000    0.001    0.000 shortest_paths.py:7(bfs_path)
       12    0.000    0.000    0.001    0.000 shortest_paths.py:171(getPath)
       10    0.000    0.000    0.000    0.000 Graph.py:11(add_node)
       10    0.000    0.000    0.000    0.000 {min}
        8    0.000    0.000    0.000    0.000 shortest_paths.py:87(Relax)
        7    0.000    0.000    0.000    0.000 {len}
      6/1    0.000    0.000    0.000    0.000 shortest_paths.py:45(visit)
        6    0.000    0.000    0.000    0.000 {sorted}
        2    0.000    0.000    0.000    0.000 Graph.py:4(__init__)
        2    0.000    0.000    0.000    0.000 {range}
        2    0.001    0.000    0.003    0.001 shortest_paths.py:163(Edmond_Karp)
        2    0.000    0.000    0.000    0.000 {method 'format' of 'str' objects}
        1    0.000    0.000    0.004    0.004 <string>:1(<module>)
        1    0.001    0.001    0.001    0.001 shortest_paths.py:116(Floyd_Warshall)
        1    0.000    0.000    0.000    0.000 shortest_paths.py:82(Dijkstra)
        1    0.000    0.000    0.000    0.000 dfs_bfs.py:13(bfs)
        1    0.000    0.000    0.004    0.004 main.py:10(Main)
        1    0.000    0.000    0.000    0.000 dfs_bfs.py:1(dfs)
        1    0.000    0.000    0.000    0.000 shortest_paths.py:40(dfs_path)
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}



```





