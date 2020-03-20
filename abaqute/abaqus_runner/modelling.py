import logging

import numpy as np
import collections
import itertools as it

class Node(object):
    id_counter=it.count(1)
    
    def __init__(self,coor,exists=False,id_=None):
        self.coor=coor
        if id_ is None:
            self.id=next(Node.id_counter)
        else:
            self.id=id_
            Node.id_counter=it.count(self.id+1)
        self.exists=exists
    
    def __str__(self):
        return f"Node id:{self.id}, coor:{self.coor}"
    
    def __repr__(self):
        return f"Node id:{self.id}, coor:{self.coor}"

class Element(object):
    id_counter=it.count(1)
    
    def __init__(self,*nodes):
        self.nodes=nodes
        self.id=next(Element.id_counter)
        self.name=f'Elem_{self.id}'

class NodeSet(object):
    def __init__(self,name,*nodes):
        self.name=name
        self.nodes=nodes

def write_to_file(filepath,lines):
    with open(filepath,'w') as f:
        f.write("\n".join(lines))

class Model:
    def __init__(self):
        self.data=collections.defaultdict(list)
        # self.data['node_data'] = ["*Node"]
        # self.data['boundary_data'] = ["*Boundary", "** Name: BC-1 Type: Displacement/Rotation"]
        self.are_nodes_provided=False
        self.are_boundaries_provided=False
        self._item_order=it.count()
        pass
    
    def _add_to_data(self,key,lines):
        self.data[key].append("\n".join(lines))
    
    # print(self.data[key])
    
    def add_node(self,node: Node):
        if node.exists: return
        node_coor=",".join(map(lambda x:str(float(x)),node.coor))
        # node_id = next(self.node_id_counter)
        node_id=node.id
        lines=list()
        if not 'node_data' in self.data:
            lines.append("*Node")
        lines.append(f"{node_id},{node_coor}")
        self._add_to_data('node_data',lines)
    
    def add_nodeset(self,nodeset: NodeSet):
        lines=[f"*Nset, nset={nodeset.name}"]
        ids_line=",".join([str(x.id) for x in nodeset.nodes])
        lines.append(" "+ids_line+',')
        self._add_to_data('nodeset_data',lines)
    
    def add_raw_data(self,data: str):
        # self.data['raw_data'].append(data)
        self._add_to_data('raw_data',[data])
    
    def add_gap(self,gap_value,element):
        lines=[f"*GAP,Elset={element.name}",f"{gap_value},1,0,0,1"]
        self._add_to_data('gap_data',lines)
    
    def create_node(self,coor,exists=False):
        node=Node(coor,exists=exists)
        self.add_node(node)
        return node
    
    def create_element(self,*nodes):
        elem=Element(*nodes)
        self.add_element(elem)
        return elem
    
    def add_element(self,element: Element):
        lines=[f'*Element,TYPE=GAPUNI,ELSET={element.name}']
        lines.append(",".join(map(str,[element.id,*[x.id for x in element.nodes]])))
        self._add_to_data('element_data',lines)
    
    def add_boundary(self,nodeset,dispDOF,rotDOF,actual_magn=None):
        if actual_magn is None:
            text=f"{nodeset.name}, {dispDOF}, {rotDOF}"
        else:
            text=f"{nodeset.name}, {dispDOF}, {rotDOF}, {float(actual_magn)}"
        lines=list()
        if not 'boundary_data' in self.data:
            lines.extend(["** Name: BC-1 Type: Displacement/Rotation","*Boundary"])
        lines.append(text)
        self._add_to_data('boundary_data',lines)
    
    def add_py_curve(self,data):
        lines=['*SURFACE BEHAVIOR,PRESSURE-OVERCLOSURE=TABULAR','0.0,0.0']
        for data_line in np.round(data,15):
            lines.append(",".join(map(str,data_line)))
        self._add_to_data('py_curves',lines)
    
    def add_friction(self,elastic_slip,myu):
        lines=[f'*Friction, ELASTIC SLIP={elastic_slip}',str(myu)]
        self._add_to_data('friction_data',lines)
    
    def generate(self):
        all_lines=list()
        # sorted_data = sorted(self.data.items(), key=lambda item: item[1][0])
        # print(sorted_data)
        for key,lines in self.data.items():
            # logger.debug('key: %s', key)
            all_lines.extend(lines)
        return "\n".join(all_lines)
    
    def write_to_file(self,filepath):
        with open(filepath,'w') as f:
            f.write(self.generate())
