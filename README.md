# simple-alert-log-pushbullet
Simple-pushbullet-alert

Python2.7

I've recently suscribed to a new VPS provider and I realised that some public keys was already existing in the /root/.ssh/authorized_keys file.
As a new user of PushBullet, I decided to create a quick python script that check the auth log file and send a PushBullet notification when someone connect to the server.

I could have simply deleted these public keys, but instead I found more interesting to check if my provider tries to connect to my VPS, and take action if it happens.

Usage :

Replace "YourPushBulletToken" variable in the pushbulletmodule.py file by your token, and start the script with python alert-pushbullet

To run the script as deamon, you can use "nohup python alert-pushbullet &"



Thanks to https://simplypython.wordpress.com/tag/pushbullet/ for the pushbullet module.

