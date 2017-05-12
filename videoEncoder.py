import sys, os, subprocess
from time import sleep

print ("Welcome to Byte Camp's Video Encoder.\n")
filepath = raw_input("Drag-n-Drop the first JPG or PNG image ending in '0000.jpg' or similar\nAnd press ENTER to make your video!\n")
if (filepath[0] == "\"" and filepath[-1] == "\""):
	filepath = filepath[1:-1]
print (filepath)

startNumStr = filepath[-8:-4]
startNum = str(int(startNumStr))

if (startNum > -1):
	if (filepath[-4:] == ".png" or filepath[-4:] == ".jpg"):
		if (filepath[-4:] == ".png"):
			filename = filepath[:-8]+"%04d.png"
		else:
			filename = filepath[:-8]+"%04d.jpg"
		print (filepath[:-8])
		sleep(5)
		subprocess.call(["ffmpeg","-f","image2","-r","12","-start_number",startNum,"-i",filename,"-vcodec","libx264",filepath[:-8]+".mp4", "-y"])
		print ("Conversion Completed Successfully! Enjoy your Video :D")
		sleep(5)
	else:
		print ("The filetype is not PNG or JPG. Exiting Program.")
		sleep(5)
		
else:
	print ("The filename does not end in a beginning sequence (ex: example0001.png)")
	sleep(5)
