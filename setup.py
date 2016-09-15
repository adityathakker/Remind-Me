import subprocess
from os.path import expanduser
import os

home_dir = expanduser("~")
path_to_main_dir = home_dir + "/.remind_me"
path_to_aliases = home_dir + "/.bash_aliases"
path_to_cwd = os.getcwd()

def does_it_exists(path_to_file):
	if os.path.exists(path_to_file):
		return True
	else:
		return False

if not does_it_exists(path_to_main_dir):
	print "Creating Required Folders And Files.."
	os.mkdir(path_to_main_dir,0755)
	os.system("touch " + path_to_main_dir + "/reminders")
	print "Files Creation Process Finished"

if not does_it_exists(path_to_aliases):
	os.system("touch " + path_to_aliases)
	print "Alias File Created"

if does_it_exists(path_to_aliases):
	aliases_file = open(path_to_aliases,"a")
	aliases_file.write("\nalias remindme=\"python " + path_to_cwd.replace(" ", "\ ") + "/remind_me.py $1\"")
	aliases_file.close()
	print "Alias Created"

print "\nNow You Can Use \"remindme\" command to add reminders to your list.\n\tExample: remindme \"To send mail to Arya Stark\""
print "Restart the Terminal Once To Complete The Installation"

try:
	output = len(subprocess.check_output("which zenity",shell=True).strip())
except subprocess.CalledProcessError, e:
	print "Missing Dependencies: Zenity must be installed in order for this program to work.\n\tRun \"sudo apt-get install zenity\" to install it."
	pass