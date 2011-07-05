"""
Create CAD model of pager motor
"""
from py2scad import *
from part import Part

class Pager_Motor(Part):

    def make(self):
        body_diam = self.params['body_diam']
        body_length = self.params['body_length']
        weight_diam = self.params['weight_diam']
        weight_length = self.params['weight_length']
        weight_offset = self.params['weight_offset']
        shaft_diam = self.params['shaft_diam']

        body_r = 0.5*body_diam
        body_cyl = Cylinder(h=body_length,r1=body_r,r2=body_r)

        weight_r = 0.5*weight_length
        weight_cyl = Cylinder(h=weight_length, r1=weight_r, r2=weight_r)

        shaft_r = 0.5*shaft_diam
        shaft_cyl = Cylinder(h=2*weight_offset,r1=shaft_r,r2=shaft_r)

        # Translate into position
        total_length = body_length + weight_length + weight_offset
        body_z_shift = 0.5*body_length - 0.5*total_length
        body_cyl = Translate(body_cyl,v=(0,0,body_z_shift))

        weight_z_shift = body_length + weight_offset + 0.5*weight_length - 0.5*total_length
        weight_cyl = Translate(weight_cyl,v=(0,0,weight_z_shift))

        shaft_z_shift = body_length + 0.5*weight_offset -0.5*total_length
        shaft_cyl = Translate(shaft_cyl,v=(0,0,shaft_z_shift))

        self.part = Union([body_cyl, weight_cyl, shaft_cyl])
        

# -----------------------------------------------------------------------------
if __name__ == '__main__':

    import params
    motor = Pager_Motor(**params.pager_motor)
    prog = SCAD_Prog()
    prog.fn = 50
    prog.add(motor)
    prog.write('pager_motor.scad')
