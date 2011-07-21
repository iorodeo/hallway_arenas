"""
CAD model for camera mounting posts.
"""
from py2scad import *
from part import Part

class Camera_Post(Part):

    def make(self):
        dxf_profile = self.params['dxf_profile']
        length = self.params['length']
        width = self.params['width']
        part = Linear_DXF_Extrude(dxf_profile,height=length)
        part = Scale(part,v=(INCH2MM, INCH2MM, 1.0))
        self.part = part

# -----------------------------------------------------------------------------
if __name__ == '__main__':

    import params
    part = Camera_Post(**params.camera_post)
    prog = SCAD_Prog()
    prog.fn = 50
    prog.add(part)
    prog.write('camera_post.scad')
