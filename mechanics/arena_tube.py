"""
Creates CAD model for arena tube

"""
from py2scad import *
from part import Part

class Arena_Tube(Part):

    def make(self):
        length = self.params['length']
        width = self.params['width']
        height = self.params['height']
        thickness = self.params['thickness']

        # Create rectange for part and cut hole
        self.part = Cube(size=(length,width,height))
        cut_cyl = Cube(size=(2*length,width-thickness, height-thickness))
        self.part = Difference([self.part,cut_cyl])

# -----------------------------------------------------------------------------
if __name__ == '__main__':

    import params
    part = Arena_Tube(**params.arena_tube)
    prog = SCAD_Prog()
    prog.fn = 50
    prog.add(part)
    prog.write('arena_tube.scad')
