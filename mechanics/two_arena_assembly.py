from py2scad import *
from assembly import Assembly
from arena_assembly import Arena_Assembly
from breadboard import Breadboard
from camera_post import Camera_Post
from camera_plate import Camera_Plate
from camera import Camera
from bracket import Bracket

class Two_Arena_Assembly(Assembly):

    def make(self):

        # Extract paramaters
        arena_y_offset = self.params.two_arena_assembly['arena_y_offset']
        camera_post_y_offset = self.params.two_arena_assembly['camera_post_y_offset']
        camera_post_x_offset = self.params.two_arena_assembly['camera_post_x_offset']
        breadboard_thickness = self.params.breadboard['thickness']
        camera_plate_color = self.params.camera_plate['color']
        camera_plate_z_frac = self.params.two_arena_assembly['camera_plate_z_frac']

        # Create components
        arena_pos = Arena_Assembly(params=self.params)
        arena_neg = Arena_Assembly(params=self.params)
        breadboard = Breadboard(**self.params.breadboard)
        camera_post_pos = Camera_Post(**self.params.camera_post)
        camera_post_neg = Camera_Post(**self.params.camera_post)
        camera_plate = Camera_Plate(**self.params.camera_plate)
        camera = Camera(**self.params.camera)
        bracket_dict = {}
        for i in (-1,1):
            for j in (-1,1):
                bracket_dict[(i,j)] = Bracket(**self.params.bracket)

        # Translate breadboard into position
        breadboard.translate(v=(0,0,-0.5*breadboard_thickness))

        # Translate arenas into position
        arena_pos.translate(v=(0, arena_y_offset,0))
        arena_neg.translate(v=(0,-arena_y_offset,0))

        # Translate camera posts into position
        z_shift = 0.5*self.params.camera_post['length']
        camera_post_pos.translate(v=(camera_post_x_offset, camera_post_y_offset,z_shift))
        camera_post_neg.translate(v=(camera_post_x_offset,-camera_post_y_offset,z_shift))

        # Rotate and translate camera plate into position
        camera_plate.rotate(a=90,v=(1,0,0))
        camera_plate.rotate(a=90,v=(0,0,1))

        z_shift = 0.5*self.params.camera_plate['width']
        z_shift += camera_plate_z_frac*self.params.camera_post['length']
        z_shift -= self.params.camera_plate['width']

        x_shift = camera_post_x_offset + 0.5*self.params.camera_post['width']
        x_shift += 0.5*self.params.camera_plate['thickness']

        camera_plate.translate(v=(x_shift,0,z_shift))
        camera_plate.color(rgba=self.params.camera_plate['color'])

        # Rotate and translate camera into position
        camera.rotate(a=90,v=(0,1,0))

        z_shift = camera_plate_z_frac*self.params.camera_post['length']
        z_shift -= 0.5*self.params.camera_plate['width']

        x_shift = camera_post_x_offset + 0.5*self.params.camera_post['width']
        x_shift += self.params.camera_plate['thickness']
        x_shift += 0.5*self.params.camera['body_thickness']

        camera.translate(v=(x_shift,0,z_shift))
        camera.color(rgba=self.params.camera['color'])

        # Rotate and translate brackets into positon
        for k, bracket in bracket_dict.iteritems():
            i,j = k
            if i == 1:
                bracket.rotate(a=180,v=(0,0,1))
                x_shift = 0.5*self.params.bracket['length']
                x_shift += camera_post_x_offset
                x_shift += 0.5*self.params.camera_post['width']
            else:
                x_shift = -0.5*self.params.bracket['length'] 
                x_shift += camera_post_x_offset
                x_shift -= 0.5*self.params.camera_post['width']
            y_shift = j*camera_post_y_offset
            bracket.translate(v=(x_shift,y_shift,0))
            bracket.color(rgba=self.params.bracket['color'])

        # Create parts dictionary
        self.parts = {
                'breadboard'      : breadboard,
                'arena_pos'       : arena_pos,
                'arena_neg'       : arena_neg,
                'camera_post_pos' : camera_post_pos,
                'camera_post_neg' : camera_post_neg,
                'camera_plate'    : camera_plate,
                'camera'          : camera,
                }

        for k, bracket in bracket_dict.iteritems():
            i,j = k
            name  = 'bracket'
            if i == 1:
                name = '%s_posx'%(name,)
            else:
                name = '%s_negx'%(name,)
            if j == 1:
                name = '%s_posy'%(name,)
            else:
                name = '%s_negy'%(name,)
            self.parts[name] = bracket



# -----------------------------------------------------------------------------
if __name__ == '__main__':
    import params
    assem = Two_Arena_Assembly(params=params)
    prog = SCAD_Prog()
    prog.fn = 50
    prog.add(assem)
    prog.write('two_arena_assembly.scad')
