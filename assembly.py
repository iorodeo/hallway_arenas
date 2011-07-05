"""
Base class for assemblies
"""
from py2scad import *

class Assembly(object):

    def __init__(self, **kwargs):
        self.params = kwargs['params']
        self.make()

    def __str__(self):
        parts_str_list = [] 
        for name in self.parts:
            parts_str_list.append(self.parts[name].__str__())
            parts_str_list.append('\n')
        parts_str = ''.join(parts_str_list)
        return parts_str 

    def make(self):
        self.parts = {}

    def translate(self,v=(0,0,0)):
        for name,part in self.parts.iteritems():
            if isinstance(part,Assembly):
                self.parts[name].translate(v=v)
            else:
                self.parts[name] = Translate(part,v=v)

    def rotate(self,a=0,v=(1,0,0)):
        for name,part in self.parts.iteritems():
            if isinstance(part,Assembly):
                self.parts[name].rotate(a=a,v=v)
            else:
                self.parts[name] = Rotate(part,a=a,v=v)

