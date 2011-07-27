from brd_tools import SegmentDrawer

center = 8.0, 3.0
boardX = 13.5
boardY = 1.25

upperRight =  center[0] -  boardX/2.0, center[1] - boardY/2.0
lowerLeft =  upperRight[0] + 13.5, upperRight[1] + 1.25 
lineWidth = 0.015
drawer = SegmentDrawer('hallway_panels_arena.brd')
drawer.addRectangle(upperRight, lowerLeft, lineWidth)
drawer.write()


