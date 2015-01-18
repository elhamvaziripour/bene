import sys
sys.path.append('..')

from src import link
from src import node

class Network(object):
    def __init__(self,config):
        self.config = config
        self.nodes = {}
        self.address = 1
        self.build()

    def build(self):
        with open(self.config) as f:
            for line in f.readlines():
                if line.startswith('#'):
                    continue
                fields  = line.split()
                if len(fields) < 4:
                    continue
                start = self.get_node(fields[0])
                for i in xrange(1, len(fields)-2,3):
                    end = self.get_node(fields[i])
                    bandwidth_rate =  float(fields[i+1])
                    propagation_delay =  float(fields[i+2])
                    l = link.Link(self.address,start,endpoint=end,bandwidth=bandwidth_rate,propagation=propagation_delay)
                    self.address += 1
                    start.add_link(l)
                
    def get_node(self,name):
        if name not in self.nodes:
            self.nodes[name] = node.Node(name)
        return self.nodes[name]
