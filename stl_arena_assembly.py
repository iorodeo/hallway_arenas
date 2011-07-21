"""
Create stl parts for the arena assembly

"""
import sys
from py2scad import * 
from arena_assembly import Arena_Assembly

if __name__ == '__main__':
    import params
    assem = Arena_Assembly(params=params)
    if 'stl' in sys.argv[1:]:
        assem.convert2stl()
    if 'vconfig' in sys.argv[1:]:
        assem.write_vconfig('system_assembly')
