"""
Base class for makeing parts
"""
from py2scad import *

class Part(object):

    def __init__(self, **kwargs):
        self.params = kwargs
        self.make()

    def __str__(self):
        if self.part:
            return self.part.__str__()
        else:
            return ''

    def make(self):
        self.part = []

    def translate(self,v=(0,0,0)):
        self.part = Translate(self.part,v=v)

    def rotate(self,a=0,v=(1,0,0)):
        self.part = Rotate(self.part,a=a,v=v)

    def color(self,rgba=(0,0,0,0)):
        self.part = Color(self.part,rgba=rgba)

    def get_vconfig_obj(self,name):
        
        color = self.params['color'][0:3]
        opacity = self.params['color'][3]
        parameters = {
                'specular_power' : 0.8,
                'specular'       : 0.7,
                'diffuse'        : 0.7, 
                'color'          : color,
                'opacity'        : opacity, 
                } 
        obj = {'filename' : '%s.stl'%(name,), 'parameters' : parameters}
        return obj
