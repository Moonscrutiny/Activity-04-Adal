import cv2
import numpy

print ("Please choose an option!")
print ("[1]Fixed\n[2]Provide")
x = int(input ("Answer: "))

if (x == 1 ):
	filePath='drip.jpg'
	hot = cv2.imread(filePath, 1)
	cv2.imshow("Best Fashion Ever Created!", hot)
	cv2.waitKey(0)
	cv2.destroyAllWindows()

elif (x == 2):
	path = str(input("===================File Path===================\nNOTE:THE IMAGE MUST BE INSIDE THE FOLDER\nNOTE: BE SURE TO RIGHT THE CORRECT NAME AND FILE TYPE OK?\nDefault = drip.jpg\nAnswer: "))
	flag = int(input("===================Enter Flag===================\n[1]Color	[0]Grayscale	[-1]Unchanged\nDefault = 1\nAnswer: "))
	heh = cv2.imread(path,flag)
	if (flag == 1 or flag == 0 or flag == -1):
		
		cv2.imshow("User Provided Option", heh)
		cv2.waitKey(0)
		cv2.destroyAllWindows()
	else:
		print("============================================================\nThere were choices\nall you need to do was to choose\nand you messed it up SMH\n============================================================")
		exit()
else:
	print("============================================================\nThe only options are 1 and 2,IDK if you typo or just high\n============================================================")