"""
Creates an enclosure
"""
from py2scad import *

INCH2MM = 25.4

# Inside dimensions
x,y,z = 7*INCH2MM, 5.0*INCH2MM, 2.0*INCH2MM
hole_list = []

# Holes for mounting PCB
pcb_hole_spacing_x = 129.540
pcb_hole_spacing_y = 72.390
pcb_hole_diameter = 0.12*INCH2MM    
pcb_offset = 15.0
for i in (-1,1):
    for j in (-1,1):
        x_pos = 0.5*i*pcb_hole_spacing_x 
        y_pos = 0.5*(j+1)*pcb_hole_spacing_y - 0.5*y  + pcb_offset 
        hole = {
                'panel'      : 'bottom', 
                'type'       : 'round',
                'location'   : (x_pos, y_pos),
                'size'       : pcb_hole_diameter,
                }
        hole_list.append(hole)

# Holes for USB connector
usb_pos_x = 29.845
usb_pos_z = 29.0 - 0.5*z
usb_size_x = 14.0
usb_size_z = 12.0 
usb_radius = 1.0 
hole = {
        'panel'     : 'front',
        'type'      : 'rounded_square',
        'location'  : (usb_pos_x, usb_pos_z),
        'size'      : (usb_size_x, usb_size_z, usb_radius),
        }
hole_list.append(hole)

# Holes for 2.1mm DC jacks
jack_hole_diameter = 8.0
jack_hole_x_list = [0.5*x*val for val in (0.7,0.4,-0.7)] 
for x_pos in jack_hole_x_list:
    hole = {
            'panel'     : 'back',
            'type'      : 'round',
            'location'  : (x_pos, 0.0),
            'size'      : jack_hole_diameter,
            }
    hole_list.append(hole)

params = {
        'inner_dimensions'        : (x,y,z), 
        'wall_thickness'          : (1.0/8.0)*INCH2MM, 
        'lid_radius'              : 0.25*INCH2MM,  
        'top_x_overhang'          : 0.2*INCH2MM,
        'top_y_overhang'          : 0.2*INCH2MM,
        'bottom_x_overhang'       : 0.2*INCH2MM,
        'bottom_y_overhang'       : 0.2*INCH2MM, 
        'lid2front_tabs'          : (0.2,0.5,0.8),
        'lid2side_tabs'           : (0.25, 0.75),
        'side2side_tabs'          : (0.5,),
        'lid2front_tab_width'     : 0.75*INCH2MM,
        'lid2side_tab_width'      : 0.75*INCH2MM, 
        'side2side_tab_width'     : 0.5*INCH2MM,
        'standoff_diameter'       : 0.25*INCH2MM,
        'standoff_offset'         : 0.05*INCH2MM,
        'standoff_hole_diameter'  : 0.116*INCH2MM, 
        'hole_list'               : hole_list,
        }

enclosure = Basic_Enclosure(params)
enclosure.make()

part_assembly = enclosure.get_assembly(
        explode=(0,0,0),
        show_top=True,
        )
part_projection = enclosure.get_projection()

prog_assembly = SCAD_Prog()
prog_assembly.fn = 50
prog_assembly.add(part_assembly)
prog_assembly.write('enclosure_assembly.scad')

prog_projection = SCAD_Prog()
prog_projection.fn = 50
prog_projection.add(part_projection)
prog_projection.write('enclosure_projection.scad')
