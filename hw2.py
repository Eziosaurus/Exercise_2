# Name: Edo Martinelli
# Section Leader: Abby Collier
# Date: 02/04/2021
# Assignment: ISTA 350 Hw2
# Summary: 
# Collaboration: Got help from Rich

import re

class Node:
    # Summary: 
    def __init__(self, datum = None):
        # Summary: 
        # Parameters: 
        # Returns:
        self.datum = datum
        self.children = []

    def get_child(self, datum = None):
        # Summary: 
        # Parameters: 
        # Returns:
        for child in self.children:
            if child.datum == datum:
                return child
    
    def __eq__(self, other):
        # Summary: 
        # Parameters: 
        # Returns:
        if len(self.children) != len(other.children):
            return False
        if not self.children:
            return True
        
        equal = True

        for child in self.children:
            other_child = other.get_child(child.datum)
            if not other_child:
                return False
            equal = equal and child == other_child
        return equal

class WatchListLinked:
    # Summary:
    def __init__(self, fname = ''):
        # Summary: 
        # Parameters: 
        # Returns:
        self.root = Node()
        self.root.children = [Node('5'), Node('10'), Node('20'), Node('50'), Node('100')]

        if fname:
            with open(fname) as fp:
                for line in fp:
                    sn, dnom = line.split()
                    self.insert(sn, dnom)

        self.validator = re.compile('^[A-M][A-L](?!0{8})\d{8}[A-NP-Y]$')

    def insert(self, sn, dnom):
        # Summary: 
        # Parameters: 
        # Returns:
        current = self.root.get_child(dnom)
        for ch in sn:
            next = current.get_child(ch)
            if not next:
                next = Node(ch)
                current.children.append(next)
            current = next
        if not current.get_child():
            current.children.append(Node())
    
    def search(self, sn, dnom):
        # Summary: 
        # Parameters: 
        # Returns:
        current = self.root.get_child(dnom)
        for ch in sn:
            next = current.get_child(ch)
            if not next:
                return False
            current = next
        if not current.get_child():
            return False
        
        return True

class WatchListDict:
    # Summary:
    def __init__(self, fname = ''):
        # Summary: 
        # Parameters: 
        # Returns:
        self.root = {'5': {}, '10': {}, '20': {}, '50': {}, '100': {}}
        if fname:
            file = open(fname, 'r')
            for line in file:
                sn, dnom = line.split()
                self.insert(sn, dnom)
        self.validator = re.compile('^[A-M][A-L](?!0{8})\d{8}[A-NP-Y]$')

    def insert(self, sn, dnom):
        # Summary: 
        # Parameters: 
        # Returns:
        current_dict = self.root[dnom]
        for ch in sn:
            if ch not in current_dict:
                current_dict[ch] = {}
            current_dict = current_dict[ch]
        if None not in current_dict:
            current_dict[None] = None
    
    def search(self, sn, dnom):
        # Summary: 
        # Parameters: 
        # Returns:
        current_dict = self.root[dnom]
        for ch in sn:
            if ch not in current_dict:
                return False
            current_dict = current_dict[ch]
        if None not in current_dict:
            return False
        
        return True

def check_bills(wl, fname):
    # Summary: 
    # Parameters: 
    # Returns:
    fake_bills = []
    
    for line in open(fname):
        bills = line.strip()
        sn, dnom = bills.split()

        if wl.search(sn, dnom) or not wl.validator.match(sn):
            fake_bills.append(bills)
        
    return fake_bills