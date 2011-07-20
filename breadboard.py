"""
CAD model of thorlabs breadboard
"""
import math
from py2scad import *
from part import Part

class Breadboard(Part):

    def make(self):
        length = self.params['length']
        width = self.params['width']
        thickness = self.params['thickness']
        hole_spacing = self.params['hole_spacing']
        hole_diameter = self.params['hole_diameter']
        hole_offset = self.params['hole_offset']
        color = self.params['color']
        
        # Create list of breadboard holes
        hole_list = []
        start_pos_x = -0.5*length + hole_offset
        start_pos_y = -0.5*width + hole_offset
        pos_x = start_pos_x
        pos_y = start_pos_y 
        while pos_y < 0.5*width:
            hole_list.append((pos_x, pos_y, hole_diameter))
            pos_x += hole_spacing
            if pos_x > 0.5*length:
                pos_x = start_pos_x
                pos_y += hole_spacing

        # Create bread board
        breadboard = plate_w_holes(length, width, thickness, hole_list)
        self.part = Color(breadboard,rgba=color)


# -----------------------------------------------------------------------------
if __name__ == '__main__':
    import params
    part = Breadboard(**params.breadboard)
    prog = SCAD_Prog()
    prog.fn = 50
    prog.add(part)
    prog.write('breadboard.scad')


