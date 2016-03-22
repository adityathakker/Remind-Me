import subprocess
from os.path import expanduser
import os


home_dir = expanduser("~")
path_to_main_dir = home_dir + "/.next_boot_reminder"
path_to_main_file = path_to_main_dir + "/reminders"

def does_it_exists(path_to_file):
	if os.path.exists(path_to_file):
		return True
	else:
		return False

def is_file_empty():
	return os.stat(path_to_main_file).st_size==0

if not does_it_exists(path_to_main_dir):
	subprocess.Popen("notify-send --urgency=normal --expire-time=1000 \"Andy\'s Next Boot Reminder\" \"Required Files Missing. Please execute the \"setup.py\" first.\"", shell=True, stdout=subprocess.PIPE)
	exit()

if is_file_empty():
	subprocess.Popen("notify-send --urgency=normal -i /usr/share/icons/gnome/32x32/devices/drive-multidisk.png --expire-time=1000 \"Andy\'s Next Boot Reminder\" \"No Remiders For Now!\"", shell=True, stdout=subprocess.PIPE)
	exit()


reminders_file = open(path_to_main_file,"r")
reminders = reminders_file.readlines()
reminders_file.close()

zenity_string = "zenity --list --checklist --separator=\"|\" --editable --text=\"Select all the completed tasks...\" --title=\"Reminders For Now...\" --column=\"Done?\" --width=400  --height=380 --column=\"Reminders\" --ok-label=\"Save\" "
for each_reminder in reminders:
	if len(each_reminder) > 0:
		zenity_string  = zenity_string + "FALSE " + "\"" + each_reminder.strip() + "\""+ " "

try:
	reminders_done = subprocess.check_output(zenity_string, shell=True).strip().split("|")
except subprocess.CalledProcessError, e:
	reminders_done = list()
	pass

reminders_file = open(path_to_main_file,"w")
for each_reminder in reminders:
	if each_reminder.strip() in reminders_done:
		continue
	else:
		reminders_file.write(each_reminder)
reminders_file.close()






