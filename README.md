roomBook

rooms rooms rooms

I wrote this after a frustrating day of mindless study space searching. This repo is the answer. It contains three files

optim.py: the selenium script that goes and books the room
config.ini: an easier way to change config settings, in the future I think I will add more rooms, if this proves valuable
roomBook.bat: small script that to use in windows task scheduler
Extra considerations:

This is hilariously insecure, I had to delete a previous repo because I couldn't hide the prior commits which contained my plaintext auth info. Run this locally!

As implied, I have this running through windows task scheduler everyday at 10am (when new availability drops) to get it right you need to change some settings I think.

A better way to do this would be to use a server, if you find a good way to do this I am all ears.

This script contains necessary sleeps to allow stuff to load, I have ~optimised these, but I guarantee they are not optimal. There are doubtless many obvious (and less obvious) tricks to make it faster.

Happy Studying :) -J
