class Graph():
    
   
    def __init__(self,name=""):
        self.nodes = {}
        self.edges = {}
        self.Adj = {}
        self.name=name
        
        
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
    
    def remove_edge(self,e):
        print "remove" ,e
        self.edges.pop(e)
        print 'remove Adj '+ str(e[1])+ " of - " + str(e[0]) 
        self.Adj[e[0]].remove(e[1])
    
    def getAdj(self,node,reverse=False):
        if reverse == True:        
            return sorted(self.Adj[node], reverse=True)         
        return self.Adj[node]   
    
     
   
        