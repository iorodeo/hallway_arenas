from py2scad import *
from part import Part

class Pager_Motor_Holder(Part):

    def make(self):
        # Extract parameters
        length = self.params['length']
        width = self.params['width']
        thickness = self.params['thickness']
        cutout_length = self.params['cutout_length']
        cutout_depth = self.params['cutout_depth']
        mount_hole_diam = self.params['mount_hole_diam']
        counter_bore_diam = self.params['counter_bore_diam']
        counter_bore_depth = self.params['counter_bore_depth']
        tie_slot_height = self.params['tie_slot_height']
        tie_slot_width = self.params['tie_slot_width']
        tie_slot_offset = self.params['tie_slot_offset']

        # Create part
        part = Cube(size=(length,width,thickness))

        # Cutout slot for motor
        cut_cube = Cube(size=(cutout_length, 2*width, thickness))
        z_shift = thickness - cutout_depth
        cut_cube = Translate(cut_cube,v=(0,0,z_shift))
        part = Difference([part,cut_cube])

        # Add mount hole
        cut_cyl_radius = 0.5*mount_hole_diam
        cut_cyl = Cylinder(h=2*thickness,r1=cut_cyl_radius,r2=cut_cyl_radius)
        part = Difference([part,cut_cyl])

        # Add counter bore
        cut_cyl_radius = 0.5*counter_bore_diam
        cut_cyl = Cylinder(h=thickness,r1=cut_cyl_radius,r2=cut_cyl_radius)
        z_shift = thickness - cutout_depth - counter_bore_depth
        cut_cyl = Translate(cut_cyl,v=(0,0,z_shift))
        part = Difference([part, cut_cyl])

        # Add cable tie slots

        # Slot throught side
        cut_cube = Cube(size=(2*length,tie_slot_width,tie_slot_height))
        z_shift = -0.5*tie_slot_height + 0.5*thickness - tie_slot_offset
        cut_cube = Translate(cut_cube,v=(0,0,z_shift))
        part = Difference([part, cut_cube])

        # Slot from bottom
        cut_cube = Cube(size=(2*tie_slot_width,tie_slot_width,thickness))
        cut_cube = Translate(cut_cube,v=(0,0,-thickness))
        x_shift = 0.5*length 
        z_shift = thickness - tie_slot_offset
        cut_cube_pos = Translate(cut_cube,v=(x_shift,0,z_shift))
        cut_cube_neg = Translate(cut_cube,v=(-x_shift,0,z_shift))
        part = Difference([part,cut_cube_pos,cut_cube_neg])

        # Orient part
        part = Rotate(part,a=180,v=(1,0,0))
        part = Translate(part,v=(0,0,-0.5*thickness))

        self.part = part

# -----------------------------------------------------------------------------
if __name__ == '__main__':

    import params
    part = Pager_Motor_Holder(**params.pager_motor_holder)
    prog = SCAD_Prog()
    prog.fn = 50
    prog.add(part)
    prog.write('pager_motor_holder.scad')

