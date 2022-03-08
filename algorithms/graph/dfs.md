# DFS (Depth First Search)

DFS algorithm is exploring every path all the way to the leaf of the graph. As in other graph algorithms, we keep track of the nodes that were already explored to prevent cycling.

When choosing DFS, it is useful to consider the width and depth of the graph. If the graph is very wide and solutions are frequent, DFS could be the right choice. On the other hand, if the graph is very deep choosing the BFS can be better option.

Applications:
- path finding
- discovering the longest path
- cycling detection

```Python
import typing as t  
from src.datastructures.graph import Graph  
  
  
def dfs(graph: Graph, root, target):  
    return _dfs(graph=graph, root=root, target=target, explored=set())  
  
  
def _dfs(graph: Graph, root: int, target: int, explored: t.Set):  
    if root == target:  
        return True  
  
	explored.add(root)  
  
    for neighbour in graph.neighbours(root):  
        if neighbour not in explored:  
            result = _dfs(graph, neighbour, target, explored)  
            if result:  
                return result
```