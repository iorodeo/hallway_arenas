"""
Base class for assemblies
"""
import pickle
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
                self.parts[name].translate(v=v)

    def rotate(self,a=0,v=(1,0,0)):
        for name,part in self.parts.iteritems():
            if isinstance(part,Assembly):
                self.parts[name].rotate(a=a,v=v)
            else:
                self.parts[name].rotate(a=a,v=v)

    def convert2stl(self,parent_name=''):
        for name, part in self.parts.iteritems():
            if parent_name:
                combined_name = '%s_%s'%(parent_name,name)
            else:
                combined_name = name
            part.convert2stl(combined_name)

    def get_vconfig_obj_list(self,parent_name=''):
        obj_list = []
        for name, part in self.parts.iteritems(): 
            if parent_name:
                combined_name = '%s_%s'%(parent_name,name)
            else:
                combined_name = name
            if isinstance(part,Assembly):
                obj_list.extend(part.get_vconfig_obj_list(combined_name))
            else:
                obj_list.append(part.get_vconfig_obj(combined_name))
        return obj_list

    def write_vconfig(self, name):
        obj_list = self.get_vconfig_obj_list()
        config = {
                'background' : (0.8,0.8,0.8),
                'size'       : (600,600),
                'objects'    : obj_list,
                }
        filename = '%s_vconfig.pkl'%(name,)
        with open(filename,'w') as fid:
            pickle.dump(config,fid)



