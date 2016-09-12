import subprocess
from os.path import expanduser
import os
import sys

home_dir = expanduser("~")
path_to_main_dir = home_dir + "/.remind_me"
path_to_main_file = path_to_main_dir + "/reminders"

def does_it_exists(path_to_file):
	if os.path.exists(path_to_file):
		return True
	else:
		return False

if not does_it_exists(path_to_main_dir):
	subprocess.Popen("notify-send --urgency=normal --expire-time=1000 \"Next Boot Reminder\" \"Required Files Missing. Please execute the \"setup.py\" first.\"", shell=True, stdout=subprocess.PIPE)
	exit()

if len(sys.argv) >= 2:
	remind_text = sys.argv[1]
	reminder_file = open(path_to_main_file,"a")
	reminder_file.write(remind_text+"\n")
	subprocess.Popen("notify-send --urgency=normal -i /usr/share/icons/gnome/32x32/status/mail-attachment.png --expire-time=1000 \"Next Boot Reminder\" \"New Reminder Added To The List!\"", shell=True, stdout=subprocess.PIPE)
	reminder_file.close()
else:
	print("Please Enter Some String After The Command\nExample: remindme \"To mail Arya Stark\"")

