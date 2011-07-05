"""
CAD model for panels assembly
"""
from py2scad import *
from assembly import Assembly
from panels_pcb_assembly import Panels_PCB_Assembly
from standoff_grommet_assembly import Standoff_Grommet_Assembly

class Panels_Assembly(Assembly):

    def make(self):
        # Create components
        panels_pcb_assembly = Panels_PCB_Assembly(params = self.params)
        standoff_assembly_pos = Standoff_Grommet_Assembly(params=self.params)
        standoff_assembly_neg = Standoff_Grommet_Assembly(params=self.params)

        # Translate plate assemby into possition
        plate_z_shift = standoff_assembly_pos.z_max
        panels_pcb_assembly.translate(v=(0,0,plate_z_shift))

        # Translate standoffs into position
        standoff_x_shift = 0.5*self.params.hallway_bottom_plate['mount_hole_space'] 
        standoff_assembly_pos.translate(v=(standoff_x_shift, 0, 0))
        standoff_assembly_neg.translate(v=(-standoff_x_shift, 0, 0))

        self.parts = {
                'panels_pcb_assembly'   : panels_pcb_assembly,
                'standoff_assembly_pos' : standoff_assembly_pos,
                'standoff_assembly_neg' : standoff_assembly_neg,
                }

# -----------------------------------------------------------------------------
if __name__ == '__main__':

    import params
    assem = Panels_Assembly(params=params)
    prog = SCAD_Prog()
    prog.fn = 50
    prog.add(assem)
    prog.write('panels_assembly.scad')
