# Graph
```Python
import typing as t  
  
  
class Graph:  
    graph_dict = {}  
  
    def add_edge(self, node, neighbour):  
        if node not in self.graph_dict:  
            self.graph_dict[node] = [neighbour]  
        else:  
            self.graph_dict[node].append(neighbour)  
  
    def neighbours(self, node) -> t.List:  
        return list(self.graph_dict.get(node, []))
  
    def show_edges(self):  
        for node in self.graph_dict:  
            for neighbour in self.graph_dict[node]:  
                print("(", node, ", ", neighbour, ")")
```