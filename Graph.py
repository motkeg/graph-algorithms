class Graph():
    
    
    def __init__(self):
        self.nodes = {}
        self.edges = {}
        self.Adj = {}
        
    def add_node(self,node,name=""):
        self.nodes[node]=name
        self.Adj[node]=[]
    
    def  add_edge(self,source,target,weight=1):
        self.edges[(source,target)]=weight
        self.Adj[source].append(target)
    
    def get_nodes(self):
        return self.nodes
    
    def get_edges(self):
        return self.edges
    
    def getAdj(self,node,reverse=False):
        if reverse == True:        
            return sorted(self.Adj[node], reverse=True)         
        return self.Adj[node]   
    
     
    def build_Heap(self):
        heap= self.get_nodes().copy().keys()
        min=[heap[0]]
        
        def extract_min():
            temp='infinite'
            index=0
            for j in self.getAdj(min[0]):
                if j in heap:
                    if temp=='infinite':
                        temp=self.edges[(min[0],j)]
                    else:
                        if temp >  int(self.edges[(min[0],j)]):
                            temp =  int(self.edges[(min[0],j)])
                            index=j
            if index  in heap:
                            
                min[0]=index
            temp='infinite'
            heap.remove(index)
            return  index              
            
        for e in self.get_edges().keys():
            heap.append((e,self.edges[e]))
            
            
        #heap.sort(key=lambda tup: tup[1])   
        return extract_min        
        