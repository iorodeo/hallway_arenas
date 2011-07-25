"""
CAD model of header for panels pcb
"""
from py2scad import *
from part import Part

class Header(Part):

    def make(self):
        length = self.params['length']
        height = self.params['height']
        width = self.params['width']
        self.part = Cube(size=(length,width, height))

# -----------------------------------------------------------------------------
if __name__ == '__main__':

    import params
    part = Header(**params.header)
    prog = SCAD_Prog()
    prog.fn = 50
    prog.add(part)
    prog.write('header.scad')
