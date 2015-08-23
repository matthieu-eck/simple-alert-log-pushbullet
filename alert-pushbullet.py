#!/usr/bin/env python
import time
import os
import pushbulletmodule
myvar = "Accepted"
f = open('/var/log/auth.log')
f.read()
#Find the number of byte of the file
p = f.tell()
while True:
    time.sleep( 0.2 )
    #Go to the last Byte of the file
    f.seek(p)
    my_data = f.read()
    #Update the position
    p = f.tell()
    my_data = str(my_data)
    #Check if myvar is in the log file
    if myvar in my_data:
        my_data = my_data.splitlines()
        for line in my_data:
            if myvar in line:
                pushbulletmodule.send_notification_via_pushbullet("Alert", line)
