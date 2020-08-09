#!/usr/bin/python3
import os
import sys
import subprocess
import re

tempQuery = "sensors | grep edge | cut -d '+' -f2 | cut -c 1-4"

def getData(command, n):
	subProcess = subprocess.Popen ('echo %s|sudo -S %s' % ("3743", command),
			stdout=subprocess.PIPE,
			stderr=subprocess.PIPE,
			shell= True
			)
	subProcess.wait()

	info = subProcess.stdout.readlines()[n].decode()
	info = re.sub (" +", " ", info)
	return info

temp = float(getData(tempQuery,0).strip())

tempCurve = [[30,30],[55,45],[60,50],[70,80]]
speed = 80
for control in tempCurve:    
    if(temp <= control[0]):
        speed = control[1]
        break

getData("./amdgpu-pro-fans.sh -s "+ str(speed),0)
print("The temp is: ", temp,"The speed is: ", speed)