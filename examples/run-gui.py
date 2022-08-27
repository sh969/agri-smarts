import tkinter as tk
import sys
from datetime import datetime
from tkinter import messagebox
from scd4x import SCD4X
import explorerhat
from tkinter import StringVar
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
    return 1000*value

############################# function for ph sensor
def read_PH(voltage):
    pH_offset = 0
    return 3.5*voltage+pH_offset

############################# get functions
def get_EC():   
    ecVoltage = explorerhat.analog.three.read()
    return round(readEC(ecVoltage, 25), 2)

def get_pH():
   phVoltage = explorerhat.analog.four.read()
   return round(read_PH(phVoltage), 2)

def get_co2():
    return device.measure() # co2, temperature, relative_humidity, timestamp


############################# function to show window
def helloCallBack():
   messagebox.showinfo("Data", "Saved as "+filename)

############################# button functions
def exitApp():
   print("Bye bye...")
   sys.exit()

def measure():
    ec = get_EC()
    ph = get_pH()
    scd41 = get_co2()
    ec_var.set("EC: "+str(ec)+" mS/cm")
    ph_var.set("pH: "+str(ph))
    co2.set("CO2: "+str(scd41[0])+" ppm")
    trh.set(str(round(scd41[1],1))+" C at "+str(round(scd41[2]))+" %")
    save(ec, ph, scd41)

def calibrate():
    print("Calibrating sensor")
    
def save(ec, ph, scd41):
    # save line to csv file after measurement
    with open("data/"+filename, "a", newline="") as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=' ')
        spamwriter.writerow([scd41[3], ec, ph, scd41[0], scd41[1], scd41[2]])

############################# main code

# init co2 sensor
device = SCD4X(quiet=False)
device.start_periodic_measurement()

# set file name
filetime = datetime.now()
filename = filetime.strftime("%y%m%d_%H%M%S")+".csv"

# create tk object
root = tk.Tk()
root.attributes("-fullscreen", True)

# add frame
frame = tk.Frame(root, bg="white")
frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.5)

# add buttons with function
button_exit = tk.Button(root, text="Exit", command=exitApp)
button_exit.pack()

button_measure = tk.Button(root, text="Measure", bg='white', command=measure)
button_measure.place(relx=0.1, rely=0.65, relwidth=0.2, relheight=0.1)

button_calibrate = tk.Button(root, text="Calibrate", bg='white', command=calibrate)
button_calibrate.place(relx=0.35, rely=0.65, relwidth=0.2, relheight=0.1)

button_save = tk.Button(root, text="Save", bg='white', command=helloCallBack)
button_save.place(relx=0.6, rely=0.65, relwidth=0.2, relheight=0.1)

# add label
# ec = get_EC()
ec_var = StringVar()
# ec_var.set("EC: "+str(ec)+" mS/cm")

# ph = get_pH()
ph_var = StringVar()
# ph_var.set("pH: "+str(ph))

# scd41 = get_co2()
co2 = StringVar()
# co2.set("CO2: "+str(scd41[0])+" ppm")
trh = StringVar()
# trh.set(str(round(scd41[1],1))+" C at "+str(round(scd41[2]))+" %")
measure()

label_EC = tk.Label(frame, textvariable=ec_var, bg='#80c1ff')
label_EC.place(relx=0.1, rely=0.2, relwidth=0.2, relheight=0.2)
label_pH = tk.Label(frame, textvariable=ph_var, bg='#80c1ff')
label_pH.place(relx=0.1, rely=0.5, relwidth=0.2, relheight=0.2)

label_co2 = tk.Label(frame, textvariable=co2, bg='#ebb134')
label_co2.place(relx=0.4, rely=0.2, relwidth=0.2, relheight=0.2)
label_trh = tk.Label(frame, textvariable=trh, bg='#ebb134')
label_trh.place(relx=0.4, rely=0.5, relwidth=0.2, relheight=0.2)

label_k = tk.Label(frame, text="K: "+str(318)+" ppm", bg='#7aeb34')
label_k.place(relx=0.7, rely=0.2, relwidth=0.2, relheight=0.2)
label_ca = tk.Label(frame, text="Ca: "+str(198)+" ppm", bg='#7aeb34')
label_ca.place(relx=0.7, rely=0.5, relwidth=0.2, relheight=0.2)

# add images
imagetk = tk.PhotoImage(file="images/logo.png")
image_label = tk.Label(root, image=imagetk)
image_label.place(relx=-0.05, rely=0.8, relwidth=0.5, relheight=0.2)

# run the gui loop
root.mainloop()