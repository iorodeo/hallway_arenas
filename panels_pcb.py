"""
CAD model of panels pcb for hallway arenas
"""
from py2scad import *
from part import Part

class Panels_PCB(Part):

    def make(self):
        length = self.params['length']
        width = self.params['width']
        thickness = self.params['thickness']
        hole_diameter = self.params['mount_hole_diameter']
        hole_offset = self.params['mount_hole_offset']
        hole_space = self.params['mount_hole_space']

        # Create part and add mounting holes
        self.part = Cube(size=(length,width,thickness))
        hole_r = 0.5*hole_diameter
        cut_cyl_base = Cylinder(h=2*thickness, r1=hole_r, r2=hole_r)
        for i in (-1,1):
            x_pos = i*0.5*hole_space
            y_pos = hole_offset
            cut_cyl = Translate(cut_cyl_base,v=(x_pos,y_pos,0))
            self.part = Difference([self.part, cut_cyl])

        # Center part on mount holes
        self.part = Translate(self.part, v=(0,-hole_offset,0))


# -----------------------------------------------------------------------------
if __name__ == '__main__':

    import params
    part = Panels_PCB(**params.panels_pcb)
    prog = SCAD_Prog()
    prog.fn = 50
    prog.add(part)
    prog.write('panels_pcb.scad')
