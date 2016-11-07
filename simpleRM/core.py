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
        try:
        
            yield Requirement(k,parent,v)
            
            if 'requirements' in v.keys():
                for r in walk_gen(v['requirements'],parent=k) :
                    yield r
        except:
            print('Error parsing requirement with tag, check synthax! ',k)

class Requirement():
    
    def __init__(self,tag,parent,properties):
        """ 
        tag: identifier, parent: parent requirement tag, properties: dict of parameters 
        """
        self.tag = tag # unique identifier
        self.parent = parent # parent requirement
        
        self.status = properties["status"] if "status" in properties.keys() else "draft"
        
        for k in ["tag","req","rationale","status","solution","validation"]:
            if k in properties.keys():
                self.__setattr__(k, properties[k])

        if 'requirements' in properties.keys():
            self.children = list(properties['requirements'].keys())

    
    def __getattr__(self,attr):
        """ called when attr is not found in ususal places"""
        return None
            
    def __repr__(self):
        return '%s parent:%s children:%s' % (self.tag,self.parent, str(self.children))
        
        
class DataProvider():
    """ parses trees and returns data upon request """
    
    def __init__(self, fName):
        
        self._data = yaml.load(open(fName,'r'),loader.Loader) 
    
        self.requirements = {}
        for r in walk_gen(self._data['requirements']):
            self.requirements[r.tag] = r
    
    
    def requirementsTable(self):
        """ create an overview table of the requirements """
        
        header = ["tag","status","solution","validation"]

        rows = []
        for tag,r in self.requirements.items():
            rows.append([ str(getattr(r,h)) for h in header])
        
        return dict(header=header,rows=rows)
        
        
if __name__ == "__main__":
    # some quick-and-dirty prototyping here, sorry
    
    dp = DataProvider('../requirements/simpleSE.yml')
    
    print(dp.requirements)
    