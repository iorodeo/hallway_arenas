"""
CAD model for camera mounting plate.
"""
from py2scad import *
from part import Part

class Camera_Plate(Part):

    def make(self):
        # Extract parameters
        length = self.params['length']
        width = self.params['width']
        thickness = self.params['thickness']
        mount_hole_diam = self.params['mount_hole_diam']
        mount_hole_x_space = self.params['mount_hole_x_space']
        mount_hole_y_space = self.params['mount_hole_y_space']
        camera_mount_hole_diam = self.params['camera_mount_hole_diam']
        camera_mount_x_space = self.params['camera_mount_x_space']
        camera_mount_y_space = self.params['camera_mount_y_space']

        # Create holes for plate
        hole_list = []
        for i in (-1,1):
            for j in (-1,1):
                pos_x = i*0.5*mount_hole_x_space
                pos_y = j*0.5*mount_hole_y_space
                hole_list.append((pos_x, pos_y, mount_hole_diam))

        # Create holes for mounting camera
        for i in (-1,1):
            for j in (-1,1):
                pos_x = i*0.5*camera_mount_x_space
                pos_y = j*0.5*camera_mount_y_space
                hole_list.append((pos_x,pos_y,camera_mount_hole_diam))

        # Create part
        self.part = plate_w_holes(length,width,thickness,hole_list)


# -----------------------------------------------------------------------------
if __name__ == '__main__':

    import params
    part = Camera_Plate(**params.camera_plate)
    prog = SCAD_Prog()
    prog.fn = 50
    prog.add(part)
    prog.write('camera_plate.scad')
