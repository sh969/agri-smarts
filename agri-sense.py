#!/usr/bin/env python
# written by sh969 on 24 June 2022

import time
from datetime import datetime
import explorerhat
import csv

############################# default variables for EC sensor
_kvalue                 = 1.0
_kvalueLow              = 1.0
_kvalueHigh             = 1.0

############################# default variables for pH sensor
_acidVoltage      = 2032.44
_neutralVoltage   = 1500.0

############################# function for EC sensor
def readEC(voltage,temperature):
    global _kvalueLow
    global _kvalueHigh
    global _kvalue
    rawEC = 1000*voltage/820.0/200.0
    valueTemp = rawEC * _kvalue
    if(valueTemp > 2.5):
        _kvalue = _kvalueHigh
    elif(valueTemp < 2.0):
        _kvalue = _kvalueLow
    value = rawEC * _kvalue
    value = value / (1.0+0.0185*(temperature-25.0))
    return value

############################# function for pH sensor
def read_PH(voltage):
    global _acidVoltage
    global _neutralVoltage
    slope     = (7.0-4.0)/((_neutralVoltage-1500.0)/3.0 - (_acidVoltage-1500.0)/3.0)
    intercept = 7.0 - slope*(_neutralVoltage-1500.0)/3.0
    _phValue  = slope*(voltage-1500.0)/3.0+intercept
    round(_phValue,2)
    return _phValue

############################# main code
filetime = datetime.now()
filename = filetime.strftime("%y%m%d_%H%M%S")+".csv"
while True:
    ecVoltage = explorerhat.analog.three.read()
    phVoltage = explorerhat.analog.four.read()
    ec  = round(readEC(ecVoltage, 25), 4)
    ph = round(read_PH(phVoltage), 2)
    
    with open("data/"+filename, "a", newline="") as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=' ')
        spamwriter.writerow([ec, ph])
    print("EC: %.4f mS/cm \t pH: %.2f" % (ec, ph))
    time.sleep(1.0)
