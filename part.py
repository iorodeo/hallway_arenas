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


