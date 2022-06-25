#!/usr/bin/env python
# created 22 June 2022 by sh969@cam.ac.uk
# example C code: https://wiki.dfrobot.com/PH_meter_SKU__SEN0161_ 

import time
import explorerhat

pH_offset = 0

print("""
Explorer HAT pro needs to be connected to Pi (i2c enabled)
Testing pH meter v1.1 (SEN0161) with GND, 5V and A1 connected

Press CTRL+C to exit.
""")

while True:
    four = explorerhat.analog.four.read()
    pHValue = 3.5*four+pH-offset # formula from example code
    print(pHValue)
    time.sleep(1.0)
