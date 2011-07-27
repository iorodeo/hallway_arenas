"""
CAD model for panel pcb assembly
"""
import scipy
from py2scad import *
from assembly import Assembly
from panel import Panel
from header import Header
from panels_pcb import Panels_PCB

class Panels_PCB_Assembly(Assembly):

    def make(self):
        num_panels = self.params.panels_pcb['num_panels']
        space_tol = self.params.panels_pcb['panel_space_tol']
        panel_length = self.params.panel['length']
        panel_height = self.params.panel['height']
        panel_width = self.params.panel['width']
        panels_pcb_thickness = self.params.panels_pcb['thickness']
        panels_pcb_width = self.params.panels_pcb['width']
        header_height = self.params.header['height']
        panel_header_overlap = self.params.panels_pcb['panel_header_overlap']
        panel_header_offset = self.params.panels_pcb['panel_header_offset']
        mount_hole_offset = self.params.panels_pcb['mount_hole_offset']
        explode_z = self.params.explode_z

        panels_pos = scipy.arange(0.0,num_panels)*(panel_length + space_tol)
        panels_pos -= 0.5*(num_panels-1)*(panel_length + space_tol)

        # Create components
        panels_pcb = Panels_PCB(**self.params.panels_pcb)
        panels_pcb.color(self.params.panels_pcb['color'])
        header_list = []
        panel_list = []
        panel_offset = 0.5*panels_pcb_width - (0.5*panel_width + panel_header_offset + mount_hole_offset) 

        z_pos_header = 0.5*header_height + 0.5*panels_pcb_thickness

        z_pos_panels = 0.5*panel_height 
        z_pos_panels += panels_pcb_thickness 
        z_pos_panels += header_height 
        z_pos_panels -= panel_header_overlap
        z_pos_panels += explode_z

        y_pos_header = panel_offset
        y_pos_panels = panel_header_offset + panel_offset

        for x_pos in panels_pos:
            print 8+x_pos/INCH2MM, 3+y_pos_header/INCH2MM
            # Create header
            header_temp = Header(**self.params.header)
            header_temp.translate(v=(x_pos,y_pos_header,z_pos_header))
            header_temp.color(rgba=self.params.header['color'])
            header_list.append(header_temp)

            # Create panel
            panel_temp = Panel(**self.params.panel)
            panel_temp.translate(v=(x_pos,y_pos_panels,z_pos_panels))
            panel_temp.color(rgba=self.params.panel['color'])
            panel_list.append(panel_temp)

        # Create parts dictionary
        self.parts = {'panels_pcb' : panels_pcb}
        for i,h in enumerate(header_list):
            self.parts['header_%d'%(i,)] = h
        for i,p in enumerate(panel_list):
            self.parts['panel_%d'%(i,)] = p


# -----------------------------------------------------------------------------
if __name__ == '__main__':

    import params
    assem = Panels_PCB_Assembly(params=params)
    prog = SCAD_Prog()
    prog.fn = 50
    prog.add(assem)
    prog.write('panels_pcb_assembly.scad')
