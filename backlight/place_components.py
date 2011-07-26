from brd_tools import ComponentPlacer

MM2INCH = 1.0/25.4

yNum = 16 
xNum = 6 
xStart = 5.0 - 0.25
yStart = 3.0  
xStep = 0.25 
yStep = 0.25 
ang = 0.0 

placer = ComponentPlacer('hallway_backlight.brd')
for i in range(0,yNum):
    for j in range(0,xNum/2):
        name = 'D%d,%d'%(j,i)
        x = xStart + j*xStep
        y = yStart + i*yStep
        placer.setModulePos(name,x,y,ang)

for i in range(0,yNum):
    for j in range(xNum/2,xNum):
        name = 'D%d,%d'%(j,i)
        x = xStart + (j-xNum/2)*xStep
        y = yStart + i*xStep + yNum*yStep
        placer.setModulePos(name,x,y,ang)
placer.write()
