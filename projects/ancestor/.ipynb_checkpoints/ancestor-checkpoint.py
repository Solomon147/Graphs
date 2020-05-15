import sys
sys.path.insert(0, '../graph')
from graph import Graph


def earliest_ancestor(ancestors, starting_node):
    family_tree = Graph()
    
    for tbh in ancestors:
        if tbh[0] not in family_tree.vertices:
            family_tree.add_vertex(tbh[0])
            
        if tbh[1] not in family_tree.vertices:
            family_tree.add_vertex(tbh[1])
            
        family_tree.add_edge(tbh[0], tbh[1])
        
    relations = []
    
    for parent in family_tree.vertices:
        path = family_tree.bfs(parent, starting_node)
        if path is not None:
            relations.append(path)
            
    if len(relations) > 1:
        oldest = relations[0]
        for path in relations:
            if path is not None and len(path) > len(oldest):
                oldest = path
        return oldest[0]
    else:
        return -1