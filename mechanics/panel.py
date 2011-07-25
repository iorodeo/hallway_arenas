"""
CAD model of visual display panel
"""
from py2scad import *
from part import Part

class Panel(Part):

    def make(self):
        length = self.params['length']
        height = self.params['height']
        width = self.params['width']
        self.part = Cube(size=(length,width, height))
        pass

# -----------------------------------------------------------------------------
if __name__ == '__main__':

    import params
    part = Panel(**params.panel)
    prog = SCAD_Prog()
    prog.fn = 50
    prog.add(part)
    prog.write('panel.scad')
