"""
Create stl part for the breadboard 

"""
import sys
from py2scad import * 
from breadboard import Breadboard

if __name__ == '__main__':
    import params
    part = Breadboard(params=params)
    if 'stl' in sys.argv[1:]:
        assem.convert2stl()
    if 'vconfig' in sys.argv[1:]:
        assem.write_vconfig('breadboard')
