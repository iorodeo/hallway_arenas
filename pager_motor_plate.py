"""
Creates a CAD model of the pager motor mount plates

"""
from py2scad import *
from part import Part

class Pager_Motor_Plate(Part):

    def make(self):
        length = self.params['length']
        width = self.params['width']
        thickness = self.params['thickness']
        hole_diam = self.params['hole_diam']
        hole_space = self.params['hole_space']

        # Create plate and cut mounting holes
        self.part = Cube(size=(length,width,thickness))
        hole_r = 0.5*hole_diam
        cut_cyl_base = Cylinder(h=2*thickness,r1=hole_r,r2=hole_r)
        x_shift = 0.5*hole_space
        for i in (-1,1):
            x_pos = i*x_shift
            cut_cyl = Translate(cut_cyl_base,v=(x_pos,0,0))
            self.part = Difference([self.part,cut_cyl])

# -----------------------------------------------------------------------------
if __name__ == '__main__':

    import params
    plate = Pager_Motor_Plate(**params.pager_motor_plate)
    prog = SCAD_Prog()
    prog.fn = 50
    prog.add(plate)
    prog.write('pager_motor_plate.scad')
