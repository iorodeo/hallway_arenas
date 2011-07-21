""" Parameters for hallway arena CAD model
"""
import copy

INCH2MM = 25.4

# -----------------------------------------------------------------------------
# Utilty funcitons - for dependent parameters

def get_panels_pcb_offset():
    """
    Computes the mount hole offset for the panels pcb based on 
    """
    mount_hole_offset = arena_assembly['panels_to_hallway_gap']
    mount_hole_offset -= arena_assembly['panels_assembly_offset']
    mount_hole_offset += 0.5*hallway_bottom_plate['width']
    mount_hole_offset += 0.5*panels_pcb['width']
    return mount_hole_offset

# -----------------------------------------------------------------------------
# Hallway arena parameters

two_arena_assembly = {
        'arena_y_offset'       : 2.5*INCH2MM, 
        'camera_post_y_offset' : 5.5*INCH2MM,
        'camera_post_x_offset' : -1.5*INCH2MM,
        'camera_plate_z_frac'  : 0.95, 
        }

arena_assembly = {
        'panels_to_hallway_gap'       : 1.0, 
        'panels_assembly_offset'      : 1.0*INCH2MM,
        }

arena_tube = {
        'length'    : 200.0,
        'width'     : 0.5*INCH2MM,
        'height'    : 0.5*INCH2MM,
        'thickness' : (1.0/16)*INCH2MM,
        'color'     : (0.9, 0.9, 0.9, 0.6),
        } 

vibration_grommet = {
        'outer_diameter' : 0.625*INCH2MM, 
        'hole_diameter'  : 0.270*INCH2MM,
        'height'         : 0.325*INCH2MM,
        'inner_height'   : 0.062*INCH2MM,
        'inner_diameter' : 0.375*INCH2MM,
        'color'          : (0.8, 0.0, 0.0, 1.0), 
        }

hallway_bottom_plate = {
        'length'                  : 13.5*INCH2MM,  
        'thickness'               : 6.0, 
        'width'                   : 0.9*INCH2MM, 
        'radius'                  : 0.25*INCH2MM,
        'mount_hole_diam'         : 0.2570*INCH2MM, 
        'mount_hole_space'        : 11.0*INCH2MM, 
        'motor_mount_hole_diam'   : 0.088*INCH2MM, # 4-40 tap hole
        'motor_mount_hole_gap'    : 0.75*INCH2MM,
        'color'                   : (0.2, 0.2, 1.0, 0.25), 
        }

hallway_top_plate = copy.copy(hallway_bottom_plate)
hallway_top_plate['thickness'] = (1/16.0)*INCH2MM
hallway_top_plate['cutout_width'] = arena_tube['width'] + 0.002*INCH2MM 
hallway_top_plate['cutout_length'] = arena_tube['length'] + 0.1*INCH2MM #0.002*INCH2MM 
hallway_top_plate['color'] = (1.0, 0.2, 0.2, 0.25)

pager_motor = {
        'body_diam'     : 0.2775*INCH2MM, 
        'body_length'   : 0.6530*INCH2MM,
        'weight_diam'   : 0.2345*INCH2MM,
        'weight_length' : 0.1590*INCH2MM,
        'weight_offset' : 0.046*INCH2MM,
        'shaft_diam'    : 0.08*INCH2MM,
        'color'         : (0.8,0.8,0,1.0)
        }

pager_motor_holder = {
        'length'                : 13.78, 
        'width'                 : 8.64, 
        'thickness'             : 6.12,
        'cutout_length'         : 8.56,
        'cutout_depth'          : 3.0,
        'mount_hole_diam'       : 0.1285*INCH2MM, # 4-40
        'counter_bore_diam'     : 0.25*INCH2MM,
        'counter_bore_depth'    : 2.0,
        'tie_slot_height'       : 1.3,
        'tie_slot_width'        : 2.93,
        'tie_slot_offset'       : 1.54,
        'color'                 : (0.4, 0.8, 0.8, 1.0),
}

backlight = {
        'length'             : 9.5*INCH2MM,
        'width'              : 2.0*INCH2MM,
        'thickness'          : 0.064*INCH2MM,
        'mount_hole_diam'    : 0.257*INCH2MM,
        'mount_hole_space'   : 9.0*INCH2MM, 
        'color'              : (0.0, 1.0, 0.0, 1.0),
        }

diffuser = {
        'length'           : backlight['length'],
        'width'            : backlight['width'],
        'thickness'        : (1.0/16)*INCH2MM,
        'mount_hole_diam'  : backlight['mount_hole_diam'],
        'mount_hole_space' : backlight['mount_hole_space'],
        'color'            : (0.0, 1.0, 1.0, 1.0),
        }

hallway_standoff =  {
        'diameter'      : 0.5*INCH2MM, 
        'length'        : 2.0*INCH2MM,
        'hole_diameter' : 0.2*INCH2MM,  # 1/4-20
        'type'          : 'male-female',
        'male_length'   : 0.5*INCH2MM,
        'color'         : (0.5, 0.5, 0.5, 1.0),
        }

panels_standoff =  {
        'diameter'      : 0.5*INCH2MM, 
        'length'        : 2.0*INCH2MM,
        'hole_diameter' : 0.2*INCH2MM,  # 1/4-20
        'type'          : 'male-female',
        'male_length'   : 0.5*INCH2MM,
        'color'         : (0.5, 0.5, 0.5, 1.0),
        }

backlight_standoff = {
        'diameter'      : 0.5*INCH2MM,
        'length'        : 0.75*INCH2MM,
        'hole_diameter' : 0.2*INCH2MM,  # 1/4-20
        'type'          : 'male-female',
        'male_length'   : 0.5*INCH2MM, 
        'color'         : (0.5, 0.5, 0.5, 1.0),
        }

diffuser_standoff = {
        'diameter'      : 0.5*INCH2MM,
        'length'        : 0.5*INCH2MM,
        'hole_diameter' : 0.2*INCH2MM,  # 1/4-20
        'type'          : 'male-female',
        'male_length'   : 0.5*INCH2MM,
        'color'         : (0.5, 0.5, 0.5, 1.0),
        }

panels_pcb = {
        'length'                : 13.5*INCH2MM,
        'width'                 : 1.25*INCH2MM,
        'thickness'             : 0.064*INCH2MM,
        'mount_hole_diameter'   : 0.26*INCH2MM, # 1/4 through hole
        'mount_hole_space'      : hallway_bottom_plate['mount_hole_space'],
        'num_panels'            : 7,
        'panel_space_tol'       : 0.005*INCH2MM,
        'panel_header_overlap'  : 0.11*INCH2MM,
        'panel_header_offset'   : 0.129*INCH2MM,
        'color'                 : (0.0, 1.0, 0.0, 1.0),
        }
panels_pcb['mount_hole_offset'] = get_panels_pcb_offset()

header = {
        'length'   : 0.822*INCH2MM, 
        'height'   : 0.333*INCH2MM, 
        'width'    : 0.0975*INCH2MM, 
        'color'    : (0,0,0,1.0),
        }

panel = {
        'length'   : 1.26*INCH2MM, 
        'height'   : 1.26*INCH2MM,
        'width'    : 0.458*INCH2MM,
        'color'    : (0.0, 0.0, 1.0, 1.0),
        }

breadboard = {
        'length'           : 12.0*INCH2MM,
        'width'            : 12.0*INCH2MM,
        'thickness'        : 0.5*INCH2MM, 
        'hole_spacing'     : 1.0*INCH2MM,
        'hole_diameter'    : 0.25*INCH2MM,
        'hole_offset'      : 0.5*INCH2MM,
        'color'            : (0.2, 0.2, 0.2, 1.0),
        }

camera_post = {
        'dxf_profile'  : '1010.dxf',
        'length'       : 24.0*INCH2MM,
        'width'        : 1.0*INCH2MM,
        'color'        : (0.5, 0.5, 0.5, 1.0),
        } 
        
camera_plate = {
        'length'                  : 12.0*INCH2MM,   
        'width'                   : 59.0,
        'thickness'               : 6.0, 
        'mount_hole_diam'         : 0.26*INCH2MM,
        'mount_hole_x_space'      : 11.0*INCH2MM,
        'mount_hole_y_space'      : 1.5*INCH2MM,
        'camera_mount_hole_diam'  : 3.2, 
        'camera_mount_x_space'    : 26.0,
        'camera_mount_y_space'    : 50.0,
        'color'                   : (0.2,0.2,0.2,0.25),
        }

camera = {
        'body_length'        : 59.0,
        'body_width'         : 44.0, 
        'body_thickness'     : 29.0,
        'body_radius'        : 3.0,
        'lens_shaft_diam'    : 27.0, 
        'lens_shaft_length'  : 8.0,
        'lens_diam'          : 33.6, 
        'lens_length'        : 38.0, 
        'color'              : (0.2, 0.2, 0.2, 1.0),
        }
        

