from numpy import True_
import pandas as pd
import time
import requests
from datetime import datetime as dt

filename = "no-time_"

# recursive method to try and get data even if node does not respond at first try
def requestData():
    try:
        json = requests.get("http://192.168.1.101/").json()
    except:
        time.sleep(1)
        requestData()
    return json

def getFilename():
    try:
        # set file name
        filetime = dt.now()
        filename = filetime.strftime("%y%m%d_%H%M%S")+".csv"
    except:
        print("No_time_found.csv")
    return filename

filename = getFilename()
output_path = "~/agri-sense/data/"+filename
header = True
while True:
    json = requestData()
    df = pd.DataFrame([json])
    df.to_csv(output_path, index=False, mode="a", header=header)
    header = False
    print(df.to_string())
    time.sleep(5)