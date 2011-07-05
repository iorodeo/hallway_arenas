"""
Creates assembly of top and bottom plates for hallway arena
"""
from py2scad import *
from assembly import Assembly
from hallway_top_plate import Hallway_Top_Plate
from hallway_bottom_plate import Hallway_Bottom_Plate

class Hallway_Plate_Assembly(Assembly):

    def make(self):
        # Create components
        top_plate = Hallway_Top_Plate(**self.params.hallway_top_plate)
        bottom_plate = Hallway_Bottom_Plate(**self.params.hallway_bottom_plate)

        # Translate into position
        bottom_z_shift = 0.5*self.params.hallway_bottom_plate['thickness']
        bottom_plate.translate(v=(0,0,bottom_z_shift))
        top_z_shift = 2*bottom_z_shift + 0.5*self.params.hallway_top_plate['thickness']
        top_plate.translate(v=(0,0,top_z_shift))

        # Add color
        bottom_plate.color(rgba=self.params.hallway_bottom_plate['color'])
        top_plate.color(rgba=self.params.hallway_top_plate['color'])

        self.parts = {
                'top_plate' : top_plate, 
                'bottom_plate' : bottom_plate,
                }

# -----------------------------------------------------------------------------
if __name__ == '__main__':

    import params
    assem = Hallway_Plate_Assembly(params=params)
    prog = SCAD_Prog()
    prog.fn = 50
    prog.add(assem)
    prog.write('hallway_plate_assembly.scad')
