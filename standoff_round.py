"""
Creates a round standoff with a hole through :it.
"""
from py2scad import *
from part import Part

class Standoff_Round(Part):

    def make(self):
        diameter = self.params['diameter']
        length = self.params['length']
        hole_diameter = self.params['hole_diameter']
        standoff_type = self.params['type']

        # Create body cylinder
        r = 0.5*diameter
        body_cyl = Cylinder(h=length, r1=r, r2=r)

        cut_r = 0.5*hole_diameter
        if standoff_type == 'female-female':
            # Cut female holes  
            cut_cyl = Cylinder(h=2*length, r1=cut_r, r2=cut_r)
            self.part = Difference([body_cyl, cut_cyl])
        else:
            # Cut female holes
            cut_cyl = Cylinder(h=length, r1=cut_r, r2=cut_r)
            z_shift = 0.5*length 
            cut_cyl = Translate(cut_cyl,v=(0,0,z_shift))
            self.part = Difference([body_cyl, cut_cyl])

            # Create make end male holes
            male_length = self.params['male_length']
            male_cyl = Cylinder(h=male_length, r1=cut_r, r2=cut_r)
            z_shift = -0.5*length - 0.5*male_length
            male_cyl = Translate(male_cyl,v=(0,0,z_shift))
            self.part = Union([self.part,male_cyl])
            
# -----------------------------------------------------------------------------
if __name__ == '__main__':

    import params
    standoff = Standoff_Round(**params.hallway_standoff)
    prog = SCAD_Prog()
    prog.fn = 50
    prog.add(standoff)
    prog.write('standoff.scad')



