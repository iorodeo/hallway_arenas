"""
Creates a vibration grommet
"""
from py2scad import *
from part import Part

class Vibration_Grommet(Part):

    def make(self):
        outer_diam = self.params['outer_diameter']
        hole_diam = self.params['hole_diameter']
        height = self.params['height']
        inner_diam = self.params['inner_diameter']
        inner_height = self.params['inner_height']

        # Create cylinder for main body of gommet
        body_r = 0.5*outer_diam
        body_cyl = Cylinder(h=height,r1=body_r,r2=body_r)

        # Cut cylinder and cylinder for inner groove
        inner_cut_cyl = Cylinder(h=inner_height,r1=2*body_r,r2=2*body_r)
        inner_r = 0.5*inner_diam
        inner_cyl = Cylinder(h=height, r1=inner_r, r2=inner_r)

        # Cut cylinder for hole
        hole_r = 0.5*hole_diam
        hole_cut_cyl = Cylinder(h=2*height,r1=hole_r,r2=hole_r)

        # Make part
        self.part = Difference([body_cyl, inner_cut_cyl])
        self.part = Union([self.part, inner_cyl])
        self.part = Difference([self.part, hole_cut_cyl])


# -----------------------------------------------------------------------------
if __name__ == '__main__':

    import params
    grommet = Vibration_Grommet(**params.vibration_grommet)
    prog = SCAD_Prog()
    prog.fn = 50
    prog.add(grommet)
    prog.write('vibration_grommet.scad')
