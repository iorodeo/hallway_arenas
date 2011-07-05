"""
CAD model for backlight assembly
"""
from py2scad import *
from assembly import Assembly
from backlight import Backlight
from diffuser import Diffuser
from standoff_round import Standoff_Round

class Backlight_Assembly(Assembly):

    def make(self):
        backlight = Backlight(**self.params.backlight)
        diffuser = Diffuser(**self.params.diffuser)
        backlight_standoff = {} 
        diffuser_standoff = {} 

        for val in ('pos', 'neg'):
            backlight_standoff[val] = Standoff_Round(**self.params.backlight_standoff)
            diffuser_standoff[val] = Standoff_Round(**self.params.diffuser_standoff)

        # Shift backlight standoffs into position
        z_shift = 0.5*self.params.backlight_standoff['length']
        x_shift = 0.5*self.params.backlight['mount_hole_space']
        for k,obj in backlight_standoff.iteritems():
            sign = 1 if k=='pos' else -1
            backlight_standoff[k] = Translate(obj,v=(sign*x_shift,0,z_shift))

        # Shift backlight into position
        z_shift = self.params.backlight_standoff['length'] + 0.5*self.params.backlight['thickness']
        backlight = Translate(backlight,v=(0,0,z_shift))

        # Shift diffuser standoffs into position
        z_shift = 0.5*self.params.diffuser_standoff['length']
        z_shift += self.params.backlight_standoff['length']
        z_shift += self.params.backlight['thickness']
        x_shift = 0.5*self.params.backlight['mount_hole_space']
        for k,obj in diffuser_standoff.iteritems():
            sign = 1 if k=='pos' else -1
            diffuser_standoff[k] = Translate(obj,v=(sign*x_shift,0,z_shift))

        # Shift diffuser into position
        z_shift = 0.5*self.params.diffuser['thickness']
        z_shift += self.params.diffuser_standoff['length']
        z_shift += self.params.backlight_standoff['length']
        z_shift += self.params.backlight['thickness']
        diffuser = Translate(diffuser,v=(0,0,z_shift))

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
