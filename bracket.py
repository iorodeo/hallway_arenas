"""
CAD model for 80/20 single, 4-hole bracket
"""
from py2scad import *
from part import Part

class Bracket(Part):

    def make(self):

        # Extract parameters
        length = self.params['length']
        width = self.params['width']
        thickness = self.params['thickness']
        hole_spacing = self.params['hole_spacing']
        hole_diam = self.params['hole_diam']

        # Create plate template and cut holes
        hole_list = []
        for i in (-1,1):
            x_pos = i*0.5*hole_spacing
            hole_list.append((x_pos,0,hole_diam))
        temp_plate = plate_w_holes(length,width,thickness,hole_list)


        h_plate = Translate(temp_plate,v=(0,0,0.5*thickness))
        v_plate = Rotate(temp_plate,a=90,v=(0,1,0))
        v_plate = Translate(v_plate,v=(0.5*length-0.5*thickness,0,0.5*length))

        self.part = Union([h_plate, v_plate])


# -----------------------------------------------------------------------------
if __name__ == '__main__':

    import params
    part = Bracket(**params.bracket)
    prog = SCAD_Prog()
    prog.fn = 50
    prog.add(part)
    prog.write('bracket.scad')
