"""
Creates hallway assembly - for holding arena
"""
from py2scad import *
from assembly import Assembly
from hallway_plate_assembly import Hallway_Plate_Assembly
from standoff_grommet_assembly import Standoff_Grommet_Assembly
from pager_motor import Pager_Motor
from pager_motor_holder import Pager_Motor_Holder
from arena_tube import Arena_Tube

class Hallway_Assembly(Assembly):

    def make(self):
        # Get componets
        plate_assembly = Hallway_Plate_Assembly(params=self.params)
        standoff_assembly_pos = Standoff_Grommet_Assembly(params=self.params,standoff_name='hallway_standoff')
        standoff_assembly_neg = Standoff_Grommet_Assembly(params=self.params,standoff_name='hallway_standoff')
        pager_motor_pos = Pager_Motor(**self.params.pager_motor)
        pager_motor_neg = Pager_Motor(**self.params.pager_motor)
        pager_motor_holder_pos = Pager_Motor_Holder(**self.params.pager_motor_holder)
        pager_motor_holder_neg = Pager_Motor_Holder(**self.params.pager_motor_holder)
        arena_tube = Arena_Tube(**self.params.arena_tube)

        # Translate plate assemby into possition
        plate_z_shift = standoff_assembly_pos.z_max
        plate_assembly.translate(v=(0,0,plate_z_shift))

        # Translate standoffs into position
        standoff_x_shift = 0.5*self.params.hallway_bottom_plate['mount_hole_space'] 
        standoff_assembly_pos.translate(v=(standoff_x_shift, 0, 0))
        standoff_assembly_neg.translate(v=(-standoff_x_shift, 0, 0))

        # Rotate and translate pager motors into positon
        pager_motor_pos.rotate(a=90,v=(1,0,0))
        pager_motor_neg.rotate(a=90,v=(1,0,0))

        motor_x_shift = 0.5*self.params.hallway_bottom_plate['mount_hole_space']
        motor_x_shift += self.params.hallway_bottom_plate['motor_mount_hole_gap']

        motor_z_shift = self.params.hallway_standoff['length'] 
        motor_z_shift += self.params.vibration_grommet['height']
        motor_z_shift -= 0.5*self.params.pager_motor['body_diam']
        motor_z_shift -= self.params.pager_motor_holder['thickness']
        motor_z_shift += self.params.pager_motor_holder['cutout_depth']

        pager_motor_pos.translate(v=(motor_x_shift,0,motor_z_shift))
        pager_motor_neg.translate(v=(-motor_x_shift,0,motor_z_shift))
        pager_motor_pos.color(rgba=self.params.pager_motor['color'])
        pager_motor_neg.color(rgba=self.params.pager_motor['color'])

        # Translate pager motor holders into position
        holder_z_shift = self.params.hallway_standoff['length'] 
        holder_z_shift += self.params.vibration_grommet['height']
        pager_motor_holder_pos.translate(v=(motor_x_shift,0,holder_z_shift))
        pager_motor_holder_neg.translate(v=(-motor_x_shift,0,holder_z_shift))
        
        pager_motor_holder_pos.color(rgba=self.params.pager_motor_holder['color'])
        pager_motor_holder_neg.color(rgba=self.params.pager_motor_holder['color'])

        # Translate arena tube into position
        arena_z_shift = 0.5*self.params.arena_tube['height']
        arena_z_shift += self.params.vibration_grommet['height']
        arena_z_shift += self.params.hallway_standoff['length']
        arena_z_shift += self.params.hallway_bottom_plate['thickness']
        arena_tube.translate(v=(0,0,arena_z_shift))
        arena_tube.color(rgba=self.params.arena_tube['color'])

        # Create new parts dictionary
        self.parts = {
                'plate_assembly'          : plate_assembly,
                'standoff_assembly_pos'   : standoff_assembly_pos, 
                'standoff_assembly_neg'   : standoff_assembly_neg,
                'pager_motor_pos'         : pager_motor_pos,
                'pager_motor_neg'         : pager_motor_neg,
                'pager_motor_holder_pos'  : pager_motor_holder_pos,
                'pager_motor_holder_neg'  : pager_motor_holder_neg,
                'arena_tube'              : arena_tube,
                }

# -----------------------------------------------------------------------------
if __name__ == '__main__':

    import params
    assem = Hallway_Assembly(params=params)
    prog = SCAD_Prog()
    prog.fn = 50
    prog.add(assem)
    prog.write('hallway_assembly.scad')
