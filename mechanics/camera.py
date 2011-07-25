from py2scad import *
from part import Part

class Camera(Part):

    def make(self):
        # Extract parameters
        body_length = self.params['body_length']
        body_width = self.params['body_width']
        body_thickness = self.params['body_thickness']
        body_radius = self.params['body_radius']
        lens_shaft_diam = self.params['lens_shaft_diam']
        lens_shaft_length = self.params['lens_shaft_length']
        lens_diam = self.params['lens_diam']
        lens_length = self.params['lens_length']

        body = rounded_box(body_length, body_width, body_thickness, body_radius, round_x=False)

        # Create lens shaft
        r = 0.5*lens_shaft_diam
        lens_shaft = Cylinder(h=lens_shaft_length,r1=r,r2=r)
        lens_shaft = Rotate(lens_shaft,a=90,v=(0,1,0))
        x_shift = 0.5*lens_shaft_length + 0.5*body_length
        lens_shaft = Translate(lens_shaft,v=(x_shift,0,0))

        # Create lens
        r = 0.5*lens_diam
        lens = Cylinder(h=lens_length, r1=r, r2=r)
        lens = Rotate(lens,a=90,v=(0,1,0))
        x_shift = 0.5*lens_length 
        x_shift += 0.5*body_length
        x_shift += lens_shaft_length
        lens = Translate(lens,v=(x_shift,0,0))

        self.part = Union([body, lens_shaft,lens])



# -----------------------------------------------------------------------------
if __name__ == '__main__':

    import params
    part = Camera(**params.camera)
    prog = SCAD_Prog()
    prog.fn = 50
    prog.add(part)
    prog.write('camera.scad')
