"""
Create stl parts for the two arena assembly

"""
import sys
from py2scad import * 
from two_arena_assembly import Two_Arena_Assembly

if __name__ == '__main__':
    import params
    assem = Two_Arena_Assembly(params=params)
    if 'stl' in sys.argv[1:]:
        assem.convert2stl()
    if 'vconfig' in sys.argv[1:]:
        assem.write_vconfig('two_arena_assembly')
