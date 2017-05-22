import sys, os, subprocess
from time import sleep

print ("Welcome to Byte Camp's Video Encoder.\n")
filepath = raw_input("Drag-n-Drop the first JPG or PNG image ending in '0000.jpg' or similar\nAnd press ENTER to make your video!\n")
if (filepath[0] == "\"" and filepath[-1] == "\""):
	filepath = filepath[1:-1]

seq = filepath[-5]; c = 0; i = 1;
while seq.isdigit():
	c += 1
	try:
		seq = filepath[-5-c]
	except Exception:
		filepath = filepath[:-4-c]+"student"+filepath[-4-c:]

try:
	startNum = int(filepath[-5])
except Exception:
	startNum = -1

if (startNum >= 0):
	if (filepath[-4:] == ".png" or filepath[-4:] == ".jpg"):
		if (filepath[-4:] == ".png"):
			filename = filepath[:-4-c]+"%0"+str(c)+"d.png"
		else:
			filename = filepath[:-4-c]+"%0"+str(c)+"d.jpg"
		subprocess.call(["ffmpeg","-f","image2","-r","12","-start_number",str(startNum),"-i",filename,"-vcodec","libx264",filepath[:-8]+".mp4", "-y"])
		print ("Conversion Completed Successfully! Enjoy your Video :D")
		sleep(5)
	else:
		print ("The filetype is not PNG or JPG. Exiting Program.")
		sleep(5)
		
else:
	print ("The filename does not end in a beginning sequence (ex: example0001.png)")
	sleep(5)
