"""
Creates standoff grommet assembly
"""
from py2scad import *
from assembly import Assembly
from standoff_round import Standoff_Round
from vibration_grommet import Vibration_Grommet

class Standoff_Grommet_Assembly(Assembly):

    def make(self):

        # Create components
        standoff = Standoff_Round(**self.params.hallway_standoff)
        grommet = Vibration_Grommet(**self.params.vibration_grommet)

        # Shift grommet into position
        grommet_z_shift = 0.5*self.params.vibration_grommet['height']
        grommet = Translate(grommet,v=(0,0,grommet_z_shift))
        grommet = Color(grommet, rgba=self.params.vibration_grommet['color'])

        # Shift standoff into position
        standoff_z_shift = 0.5*self.params.hallway_standoff['length'] + 2*grommet_z_shift
        standoff = Translate(standoff, v=(0,0,standoff_z_shift))
        standoff = Color(standoff, rgba=self.params.hallway_standoff['color'])
        self.parts = {
                'standoff' : standoff,
                'grommet'  : grommet,
                }
        # Values for later use in larger assemblies
        self.z_min = 0.0
        self.z_max = self.params.vibration_grommet['height'] + self.params.hallway_standoff['length']

# -----------------------------------------------------------------------------
if __name__ == '__main__':

    import params
    assem = Standoff_Grommet_Assembly(params=params)
    prog = SCAD_Prog()
    prog.fn = 50
    prog.add(assem)
    prog.write('standoff_grommet_assembly.scad')
