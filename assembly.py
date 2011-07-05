"""
Base class for assemblies
"""
import os
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

    def write_stl(self,parent_name=''):
        for name, part in self.parts.iteritems():

            if parent_name:
                combined_name = '%s_%s'%(parent_name,name)
            else:
                combined_name = name

            if isinstance(part,Assembly):
                part.write_stl(parent_name=combined_name)
            else:
                scad_filename = 'temp.scad'
                stl_filename = '%s.stl'%(combined_name,)

                # Create temporary scad file
                prog = SCAD_Prog()
                prog.fn = 50
                prog.add(part)
                prog.write(scad_filename)

                # Create stl file
                print 'writing %s'%(stl_filename,)
                os.system('openscad -s %s %s'%(stl_filename, scad_filename))

                # Remove scad file
                os.unlink(scad_filename)

