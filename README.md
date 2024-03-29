# Agri-SMARTs: A smart Raspberry Pi based sensor for hydroponics applications

The Python code here requires the following:
- [ExplorerHAT Pro](https://github.com/pimoroni/explorer-hat) (i2c enabled!)
- SEN016 pH sensor (on pin A4 on HAT)
- DFR0300 EC sensor (on pin A3 on HAT)
- [SCD41](https://github.com/pimoroni/scd4x-python) CO2 sensor
- 3x Grow capacitive moisture sensors

**Version 1** (June 22 Sensors attached directly to Pi via Explorerhat):
Run run-gui.py for launching the GUI.

**Version 2** (August 22: Sensors attached to Arduino Wifi node):       
Run print-data.py to start recording data every 5s.

<img src="https://github.com/sh969/agri-smarts/blob/master/images/sensor-node.png?raw=true">