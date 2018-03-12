import subprocess, sqlite3
import json
import sys
import os
import time

message = sys.argv[1]

start = message[0:10]

end = message[11:22]
def retrieveTemperature(start, end):
    con = sqlite3.connect("OutsideTemperature.db")
    cur = con.cursor()
    for row in cur.execute("SELECT * FROM Temperature WHERE Date_Time BETWEEN ? AND ?",(start, end)):
        print(row)

        
retrieveTemperature(start, end)
sys.stdout.flush()
    

