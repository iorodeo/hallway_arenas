"""
CAD model for backlight assembly
"""
from py2scad import *
from assembly import Assembly
from backlight import Backlight
from diffuser import Diffuser
from standoff_round import Standoff_Round
from standoff_grommet_assembly import Standoff_Grommet_Assembly

class Backlight_Assembly(Assembly):

    def make(self):
        backlight = Backlight(**self.params.backlight)
        diffuser = Diffuser(**self.params.diffuser)
        backlight_standoff = {} 
        diffuser_standoff = {} 

        for val in ('pos', 'neg'):
            backlight_standoff[val] = Standoff_Grommet_Assembly(params=self.params,standoff_name='backlight_standoff')
            diffuser_standoff[val] = Standoff_Round(**self.params.diffuser_standoff)

        # Shift backlight standoffs into position
        x_shift = 0.5*self.params.backlight['mount_hole_space']
        for k,obj in backlight_standoff.iteritems():
            sign = 1 if k=='pos' else -1
            backlight_standoff[k].translate(v=(sign*x_shift,0,0))

        # Shift backlight into position
        z_shift = self.params.vibration_grommet['height'] + self.params.backlight_standoff['length'] + 0.5*self.params.backlight['thickness']
        backlight.translate(v=(0,0,z_shift))
        backlight.color(self.params.backlight['color'])

        # Shift diffuser standoffs into position, and set color
        z_shift = 0.5*self.params.diffuser_standoff['length']
        z_shift += self.params.vibration_grommet['height']
        z_shift += self.params.backlight_standoff['length']
        z_shift += self.params.backlight['thickness']
        x_shift = 0.5*self.params.backlight['mount_hole_space']
        for k,obj in diffuser_standoff.iteritems():
            sign = 1 if k=='pos' else -1
            diffuser_standoff[k].translate(v=(sign*x_shift,0,z_shift))
            diffuser_standoff[k].color(rgba=self.params.diffuser_standoff['color'])

        # Shift diffuser into position
        z_shift = 0.5*self.params.diffuser['thickness']
        z_shift += self.params.vibration_grommet['height']
        z_shift += self.params.diffuser_standoff['length']
        z_shift += self.params.backlight_standoff['length']
        z_shift += self.params.backlight['thickness']
        diffuser.translate(v=(0,0,z_shift))

        # Create parts dictionary
        self.parts = {}
        for k,obj in backlight_standoff.iteritems():
            self.parts['backlight_standoff_%s'%(k,)] = obj 
        for k,obj in diffuser_standoff.iteritems():
            self.parts['diffuser_standoff_%s'%(k,)] = obj
        self.parts['backlight'] = backlight
        self.parts['diffuser'] = diffuser

# -----------------------------------------------------------------------------
if __name__ == '__main__':

    import params
    assem = Backlight_Assembly(params=params)
    prog = SCAD_Prog()
    prog.fn = 50
    prog.add(assem)
    prog.write('backlight_assembly.scad')
