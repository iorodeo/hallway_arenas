"""
build.py - automates the building of scad and stl parts and assemblies for the 
hallway arenas.

Will Dickson IO Rodeo Inc.
"""
import os
import os.path
import sys

cmd = sys.argv[1].lower()

if cmd == 'scad':
    """
    Run all python scripts to build all scad files
    """
    dirList = os.listdir(os.curdir)
    for fname in dirList:
        if fname == sys.argv[0]:
            continue
        dummy, ext = os.path.splitext(fname)
        if ext == '.py':
            systemCmd = 'python %s'%(fname,)
            print 'running: %s'%(systemCmd,)
            os.system(systemCmd) 

elif cmd == 'stl_arena':
    """
    Build the stl files and visual configuration for the arena assembly
    """
    os.system('python stl_arena_assembly.py stl vconfig')

elif cmd == 'vconfig_arena':
    """
    Create visual configuration file for arena assembly
    """
    os.system('python stl_arena_assembly.py vconfig')

elif cmd == 'stl_two_arena':
    """
    Build the stl files and visual configuration for the two arena assembly
    """
    os.system('python stl_two_arena_assembly.py stl vconfig')

elif cmd == 'vconfig_two_arena':
    """
    Build the visual configuration for the two arena assembly
    """
    os.system('python stl_two_arena_assembly.py vconfig')

elif cmd == 'clean':
    """
    Clean build directory
    """
    os.system('rm *.pyc')
    os.system('rm *.scad')
    os.system('rm *~')
    os.system('rm *.pkl')
    os.system('rm *.stl')

else:
    print 'Error: uknown command %s'%(cmd,)



