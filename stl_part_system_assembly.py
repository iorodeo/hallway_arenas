"""
Create stl parts for the systems assembly

"""
import sys
from py2scad import * 
from system_assembly import System_Assembly

if __name__ == '__main__':
    import params
    assem = System_Assembly(params=params)
    if 'stl' in sys.argv[1:]:
        assem.convert2stl()
    if 'vconfig' in sys.argv[1:]:
        assem.write_vconfig('system_assembly')
