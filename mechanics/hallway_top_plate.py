
"""
Creates top plate for hallway arena
"""
from py2scad import *
from part import Part

class Hallway_Top_Plate(Part):

    def make(self):
        length = self.params['length']
        thickness = self.params['thickness']
        width = self.params['width']
        radius = self.params['radius']
        hole_diam = self.params['mount_hole_diam']
        hole_spacing = self.params['mount_hole_space']
        cutout_width = self.params['cutout_width']
        cutout_length = self.params['cutout_length']

        # Create plate and cut mounting holes
        plate = rounded_box(length,width,thickness,radius, round_z = False)
        hole_r = 0.5*hole_diam
        cut_cyl = Cylinder(h=2*thickness,r1=hole_r,r2=hole_r)
        x_shift = 0.5*hole_spacing
        cut_cyl_pos = Translate(cut_cyl,v=(x_shift,0,0))
        cut_cyl_neg = Translate(cut_cyl,v=(-x_shift,0,0))
        self.part = Difference([plate, cut_cyl_pos, cut_cyl_neg])

        # Create cutout for arena tube
        cut_cube = Cube(size=(cutout_length, cutout_width, 2*thickness))
        self.part = Difference([self.part, cut_cube])


# -----------------------------------------------------------------------------
if __name__ == '__main__':

    import params
    plate = Hallway_Top_Plate(**params.hallway_top_plate)
    prog = SCAD_Prog()
    prog.fn = 50
    prog.add(plate)
    prog.write('hallway_top_plate.scad')

    plate.projection()
    refCube = Cube(size=(INCH2MM,INCH2MM,INCH2MM)) 
    y_shift = 0.5*params.hallway_top_plate['width'] 
    y_shift += 2*params.hallway_top_plate['thickness'] 
    y_shift += 0.5*INCH2MM 
    refCube = Translate(refCube,v=(0,y_shift,0))
    refCube = Projection(refCube)
    prog = SCAD_Prog()
    prog.fn = 50
    prog.add(plate)
    prog.add(refCube)
    prog.write('hallway_top_plate_projection.scad')
