"""
Creates standoff grommet assembly
"""
from py2scad import *
from assembly import Assembly
from standoff_round import Standoff_Round
from vibration_grommet import Vibration_Grommet

class Standoff_Grommet_Assembly(Assembly):

    def __init__(self,**kwargs):
        self.standoff_name = kwargs['standoff_name']
        super(Standoff_Grommet_Assembly,self).__init__(params=kwargs['params'])

    def make(self):

        # Create components
        standoff_params = getattr(self.params,self.standoff_name)
        standoff = Standoff_Round(**standoff_params)
        grommet = Vibration_Grommet(**self.params.vibration_grommet)
        explode_z = self.params.explode_z

        # Shift grommet into position
        grommet_z_shift = 0.5*self.params.vibration_grommet['height']
        grommet.translate(v=(0,0,grommet_z_shift))
        grommet.color(rgba=self.params.vibration_grommet['color'])

        # Shift standoff into position
        standoff_z_shift = 0.5*standoff_params['length'] + 2*grommet_z_shift + explode_z
        standoff.translate(v=(0,0,standoff_z_shift))
        standoff.color(rgba=standoff_params['color'])
        self.parts = {
                'standoff' : standoff,
                'grommet'  : grommet,
                }
        # Values for later use in larger assemblies
        self.z_min = 0.0
        self.z_max = self.params.vibration_grommet['height'] + standoff_params['length']

# -----------------------------------------------------------------------------
if __name__ == '__main__':

    import params
    assem = Standoff_Grommet_Assembly(params=params,standoff_name='hallway_standoff')
    prog = SCAD_Prog()
    prog.fn = 50
    prog.add(assem)
    prog.write('standoff_grommet_assembly.scad')
