#!/usr/bin/python
"Starten mit sudo mn --custom LeafAndSpineSwitchTopo.py --topo=LeafAndSpine,x,y      x = Anzahl Spine y = Anzahl Leaf"

from mininet.topo import Topo

class LeafAndSpine(Topo):
    def __init__(self, spine=2, leaf=2):
        Topo.__init__(self)

        spines = {}
        for s in range(spine):
            spines[s] = self.addSwitch('spine%s' % (s + 1))

        for ls in range(leaf):
            leafSwitch = self.addSwitch('leaf%s' % (ls + 1))

            for s in range(spine):
                switch = spines[s]
                self.addLink(leafSwitch, switch)

topos = { 'LeafAndSpine': ( lambda spine, leaf: LeafAndSpine(spine, leaf) ) }
