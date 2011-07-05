"""
CAD model for systems assembly
"""

from py2scad import *
from assembly import Assembly
from hallway_assembly import Hallway_Assembly
from backlight_assembly import Backlight_Assembly

class System_Assembly(Assembly):

    def make(self):
        hallway_assembly = Hallway_Assembly(params=self.params)
        backlight_assembly = Backlight_Assembly(params=self.params)
        self.parts = {
                'hallway_assembly'   : hallway_assembly,
                'backlight_assembly' : backlight_assembly,
                }

# -----------------------------------------------------------------------------
if __name__ == '__main__':
    import params
    assem = System_Assembly(params=params)
    prog = SCAD_Prog()
    prog.fn = 50
    prog.add(assem)
    prog.write('system_assembly.scad')
