"""
CAD model for systems assembly
"""

from py2scad import *
from assembly import Assembly
from hallway_assembly import Hallway_Assembly
from backlight_assembly import Backlight_Assembly
from panels_assembly import Panels_Assembly

class Arena_Assembly(Assembly):

    def make(self):
        hallway_assembly = Hallway_Assembly(params=self.params)
        backlight_assembly = Backlight_Assembly(params=self.params)
        panels_assembly_pos = Panels_Assembly(params=self.params)
        panels_assembly_neg = Panels_Assembly(params=self.params)
        panels_assembly_offset = self.params.arena_assembly['panels_assembly_offset']
        explode_y = self.params.explode_y
        explode_z = self.params.explode_z

        # Translate positve and negative panel assemblies into position
        panels_assembly_pos.rotate(a=180,v=(0,0,1))
        y_shift = panels_assembly_offset + 2*explode_y
        panels_assembly_pos.translate(v=(0, y_shift,0))
        panels_assembly_neg.translate(v=(0,-y_shift,0))

        # Translate hallware assembly 
        hallway_assembly.translate(v=(0,0,explode_z))

        self.parts = {
                'hallway_assembly'   : hallway_assembly,
                'backlight_assembly' : backlight_assembly,
                'panels_assembly_pos' : panels_assembly_pos,
                'panels_assembly_neg' : panels_assembly_neg,
                }

# -----------------------------------------------------------------------------
if __name__ == '__main__':
    import params
    assem = Arena_Assembly(params=params)
    prog = SCAD_Prog()
    prog.fn = 50
    prog.add(assem)
    prog.write('arena_assembly.scad')
