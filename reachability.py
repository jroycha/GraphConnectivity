#Uses python3

import sys
class Node_Component:
    def __init__(self,key):
        self.component={key}
        self.is_ref=False
        self.ref=None
    def get_comp_head(self):
        if not self.is_ref:
            return self
        if self.ref.is_ref:
            self.ref=self.ref.get_comp_head()
        return self.ref
    def print(self):
        if self.is_ref:
            print('Is Reference')
        else:
            print(self.component)

class Graph: #we insist that the edges be pairs [x,y] such that
    #x indexes the list of nodes appropriately, not only the node key
    def __init__(self,nodes,edges):
        self.nodes=[node for node in nodes]
        self.edges=edges
        self.node_comp=[Node_Component(node) for node in self.nodes]
        self.unique_comp=None
    def build_components(self):
        for edge in self.edges:
            #self.node_comp[edge[0]].print()
            #self.node_comp[edge[1]].print()
            node_0=self.nodes[edge[0]]
            node_1=self.nodes[edge[1]]
            comp_0=self.node_comp[node_0].get_comp_head()
            if edge[1] in comp_0.component:
                pass #we already knew this node was in this component
            else:
                comp_1=self.node_comp[node_1].get_comp_head()
                comp_0.component.update(comp_1.component)
                comp_1.ref=comp_0
                comp_1.is_ref=True
                #self.node_comp[edge[0]].print()
                #self.node_comp[edge[1]].print()
            #print('Finished an Edge')
    def find_unique_components(self):
        already_covered=[False]*len(self.nodes)
        uniques=[]
        for idx in range(len(self.nodes)):
            if already_covered[idx]:
                pass
            else:
                comp=self.node_comp[idx].get_comp_head()
                uniques.append(comp.component)
                for comp_idx in comp.component:
                    already_covered[comp_idx]=True
        self.unique_comp=uniques
        return self.unique_comp
    def same(self,x,y):
        component_with_x=self.node_comp[x].get_comp_head()
        if y in component_with_x.component:
            return True
        else:
            return False
    

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    x, y = data[2 * m:]
    G=Graph(list(range(n)),[[edge[0]-1,edge[1]-1] for edge in edges])
    G.build_components()
    #print(G.find_unique_components())
    print(int(G.same(x-1,y-1)))
