import os
import time
import subprocess, sqlite3
"""Log Current Time, Temperature in Celsius and Fahrenheit
    Returns a list [time, tempC, tempF]"""

def readTemp():
    tempfile = open("/sys/bus/w1/devices/28-00000698107d/w1_slave")
    tempfile_text = tempfile.read()
    currentTime=time.strftime('%Y-%m-%d %X %p')
    tempfile.close()
    tempC=float(tempfile_text.split("\n")[1].split("t=")[1])/1000
    tempF=tempC*9.0/5.0+32.0
    return [currentTime, tempC, tempF] 

print(readTemp())


def logTemp():
    con = sqlite3.connect("OutsideTemperature.db")
    with con:
        try:
            [t,C,F]=readTemp()
            C = str(C) +" Degrees Celcius"
            F = str(F) + " Degrees Farenheight"
            print("Current temperature is: %s" %F)
            cur = con.cursor()
            cur.execute("""INSERT INTO Temperature(Date_Time, Temperature_C, Temperature_F) VALUES (?, ?, ?)""", (t, C, F))
#sql = "insert into TempData values(?,?,?)" cur.execute('insert into TempData values(?,?,?)', (t,C,F)) print "Temperature logged"
        except:
            print("Error!!")

logTemp()