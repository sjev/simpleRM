#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
main simpleRM module

@author: Jev Kuznetsov

"""

import yaml
import loader

def walk_gen(d, parent='ROOT'):
    """ tree walker, used to traverse through requirement trees """
    for k in sorted(d.keys()):
        v = d[k]
        yield Requirement(k,parent,v)
        
        if 'requirements' in v.keys():
            for r in walk_gen(v['requirements'],parent=k) :
                yield r


class Requirement():
    
    def __init__(self,tag,parent,properties):
        """ 
        tag: identifier, parent: parent requirement tag, properties: dict of parameters 
        """
        self.tag = tag # unique identifier
        self.parent = parent # parent requirement
        
        if 'requirements' in properties.keys():
            self.children = list(properties['requirements'].keys())
        else:
            self.children = None
    
    def __repr__(self):
        return '%s parent:%s children:%s' % (self.tag,self.parent, str(self.children))
        
        
class DataProvider():
    """ parses trees and returns data upon request """
    
    def __init__(self, fName):
        
        self._data = yaml.load(open(fName,'r'),loader.Loader) 
    
        self.requirements = [r for r in walk_gen(self._data['requirements'])]
    
        