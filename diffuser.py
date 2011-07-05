"""
CAD model for diffuser plate 
"""
from py2scad import *
from part import Part

class Diffuser(Part):

    def make(self):
        length = self.params['length']
        width = self.params['width']
        thickness = self.params['thickness']
        hole_diam = self.params['mount_hole_diam']
        space_x = self.params['mount_hole_space']

        # Create plate and mounting holes
        self.part = Cube(size=(length,width,thickness))
        hole_r = 0.5*hole_diam
        cut_cyl_base = Cylinder(h=2*thickness, r1=hole_r, r2=hole_r)
        for i in (-1,1):
            pos_x = i*0.5*space_x
            cut_cyl = Translate(cut_cyl_base,v=(pos_x, 0, 0))
            self.part = Difference([self.part,cut_cyl])

# -----------------------------------------------------------------------------
if __name__ == '__main__':

    import params
    part = Diffuser(**params.diffuser)
    prog = SCAD_Prog()
    prog.fn = 50
    prog.add(part)
    prog.write('diffuser.scad')
