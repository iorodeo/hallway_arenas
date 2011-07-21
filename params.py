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
        'arena_offset' : 2.5*INCH2MM, 
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
        #'length'                  : 12.5*INCH2MM,  
        'length'                  : 13.5*INCH2MM,  
        'thickness'               : 6.0, 
        'width'                   : 0.9*INCH2MM, 
        'radius'                  : 0.25*INCH2MM,
        'mount_hole_diam'         : 0.2570*INCH2MM, 
        'mount_hole_space'        : 11.0*INCH2MM, 
        'motor_cutout_width'      : 0.28*INCH2MM,
        'motor_cutout_length'     : 1.0*INCH2MM, 
        'motor_cutout_gap'        : 0.4*INCH2MM,
        'motor_mount_hole_diam'   : 0.088*INCH2MM, # 4-40
        'motor_mount_hole_space'  : 0.65*INCH2MM, 
        'color'                   : (0.2, 0.2, 1.0, 0.35), 
        }

hallway_top_plate = copy.copy(hallway_bottom_plate)
hallway_top_plate['thickness'] = (1/16.0)*INCH2MM
hallway_top_plate['cutout_width'] = arena_tube['width'] + 0.002*INCH2MM 
hallway_top_plate['cutout_length'] = arena_tube['length'] + 0.1*INCH2MM #0.002*INCH2MM 
hallway_top_plate['color'] = (1.0, 0.2, 0.2, 0.35)

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
}

pager_motor_plate = {
        'length'     : hallway_bottom_plate['width'],
        'width'      : 0.35*INCH2MM,
        'thickness'  : (1.0/16.0)*INCH2MM,
        'hole_diam'  : 0.12*INCH2MM,
        'hole_space' : hallway_bottom_plate['motor_mount_hole_space'],
        'color'      : (0.6, 0.7, 0.8, 1.0),
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
        #'length'                : 12.5*INCH2MM,
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


        


