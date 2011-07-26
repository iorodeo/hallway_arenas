from led_schem_array import LEDSchemArray

params = {
         'name'              : 'hallway_backlight',
         'numSeries'         : 16, 
         'numParallel'       : 6,
         'upperLeft'         : (2500,1000),
         'spacing'           : (600,400), 
         'annotationOffset'  : (0,-100), 
         'labelOffset'       : (0,100), 
         'stubLength'        : 300,
         'module'            : 'VSMG3700',
         }

ledSchemArray = LEDSchemArray(params)
ledSchemArray.write()
