"""
Create stl parts for the systems assembly

"""
from py2scad import * 
from system_assembly import System_Assembly

if __name__ == '__main__':
    import params
    assem = System_Assembly(params=params)
    #assem.convert2stl()
    assem.write_vconfig('system_assembly')
