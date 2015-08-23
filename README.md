# simple-alert-log-pushbullet
simple-pushbullet-alert

I've recently suscribed to a new VPS provider and I realised that some public keys was already existing in the /root/.ssh/authorized_keys file.
As a new user of PushBullet, I decided to create a quick python script that check the auth log file and send a PushBullet notification when someone connect to the server.

I could have simply deleted these public keys, but instead I found more interesting to check if my provider tries to connect to my VPS, and take action if it happens.


