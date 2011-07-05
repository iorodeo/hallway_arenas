"""
Creates bottom plate for hallway arena
"""
from py2scad import *
from part import Part

class Hallway_Bottom_Plate(Part):

    def make(self):
        length = self.params['length']
        thickness = self.params['thickness']
        width = self.params['width']
        radius = self.params['radius']
        hole_diam = self.params['mount_hole_diam']
        hole_spacing = self.params['mount_hole_space']
        motor_cutout_width = self.params['motor_cutout_width']
        motor_cutout_length = self.params['motor_cutout_length']
        motor_cutout_gap = self.params['motor_cutout_gap']
        motor_hole_diam = self.params['motor_mount_hole_diam']
        motor_hole_space = self.params['motor_mount_hole_space']

        # Create plate and cut mounting holes
        plate = rounded_box(length,width,thickness,radius, round_z = False)
        hole_r = 0.5*hole_diam
        cut_cyl = Cylinder(h=2*thickness,r1=hole_r,r2=hole_r)
        x_shift = 0.5*hole_spacing
        cut_cyl_pos = Translate(cut_cyl,v=(x_shift,0,0))
        cut_cyl_neg = Translate(cut_cyl,v=(-x_shift,0,0))
        self.part = Difference([plate, cut_cyl_pos, cut_cyl_neg])

        # Add motor cutouts
        cut_cube = Cube(size=(motor_cutout_length, motor_cutout_width, 2*thickness))
        cutout_x_shift = 0.5*hole_spacing - motor_cutout_gap - 0.5*motor_cutout_length
        cut_cube_pos = Translate(cut_cube,v=(cutout_x_shift, 0, 0))
        cut_cube_neg = Translate(cut_cube,v=(-cutout_x_shift, 0, 0))
        self.part = Difference([self.part, cut_cube_pos, cut_cube_neg])

        # Add motor mount holes
        motor_hole_r = 0.5*motor_hole_diam
        cut_cyl_base = Cylinder(h=2*thickness,r1=motor_hole_r, r2=motor_hole_r)
        motor_hole_y_shift = 0.5*motor_hole_space 
        for i in (-1,1):
            for j in (-1,1):
                x_pos = i*cutout_x_shift
                y_pos = j*motor_hole_y_shift
                cut_cyl = Translate(cut_cyl_base,v=(x_pos,y_pos,0))
                self.part = Difference([self.part, cut_cyl])


# -----------------------------------------------------------------------------
if __name__ == '__main__':

    import params
    plate = Hallway_Bottom_Plate(**params.hallway_bottom_plate)
    prog = SCAD_Prog()
    prog.fn = 50
    prog.add(plate)
    prog.write('hallway_bottom_plate.scad')


