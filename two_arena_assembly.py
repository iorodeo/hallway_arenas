from py2scad import *
from assembly import Assembly
from arena_assembly import Arena_Assembly
from breadboard import Breadboard

class Two_Arena_Assembly(Assembly):

    def make(self):

        # Extract paramaters
        arena_offset = self.params.two_arena_assembly['arena_offset']
        breadboard_thickness = self.params.breadboard['thickness']

        # Create components
        arena_pos = Arena_Assembly(params=self.params)
        arena_neg = Arena_Assembly(params=self.params)
        breadboard = Breadboard(**self.params.breadboard)

        # Translate breadboard into position
        breadboard.translate(v=(0,0,-0.5*breadboard_thickness))

        # Translate arenas into position
        arena_pos.translate(v=(0,arena_offset,0))
        arena_neg.translate(v=(0,-arena_offset,0))

        # Create parts dictionary
        self.parts = {
                'breadboard' : breadboard,
                'arena_pos'  : arena_pos,
                'arena_neg'  : arena_neg,
                }



# -----------------------------------------------------------------------------
if __name__ == '__main__':
    import params
    assem = Two_Arena_Assembly(params=params)
    prog = SCAD_Prog()
    prog.fn = 50
    prog.add(assem)
    prog.write('two_arena_assembly.scad')
