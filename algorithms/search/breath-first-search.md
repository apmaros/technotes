# BFS - Breath First Search
```python
class Graph:  
    graph = {}  
  
    def add(self, node, neighbour):  
        if node not in self.graph:  
            self.graph[node] = []  
  
        self.graph[node].append(neighbour)  
  
        return self  
  
 def neighbours(self, node):  
        return self.graph.get(node, [])  
  
def bfs(graph: Graph, node: int, target: int):  
    """  
    Returns True when node is connected to the target 
    """ 
    visited = set(node)  
    to_visit = graph.neighbours(node)  
  
    while to_visit:  
        current = to_visit.pop(0)  
  
        if current == target:  
            return True  
  
        # visit if not visited  
        if current not in visited:  
            visited.add(current)  
            to_visit.extend(graph.neighbours(current))  
  
    return False  
  
  
if __name__ == '__main__':  
    graph = Graph()  
  
    (graph  
     .add('1', '2').add('1', '3')  
     .add('2', '4').add('2', '5')  
     .add('3', '5')  
     .add('5', '7')  
     .add('3', '8')  
     .add('5', '6'))  
  
    assert bfs(graph, '1', '7')  
    assert not bfs(graph, '1', '9')
```
