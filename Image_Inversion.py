# This Program is Written by Abubakr Shafique (abubakr.shafique@gmail.com)
import numpy as np
import cv2 as cv

def Image_Inversion(Image):
	Height = Image.shape[0]
	Width = Image.shape[1]
	Channels = Image.shape[2]
	
	Size = (Height, Width, Channels)
	
	New_Image = np.zeros(Size, np.uint8)
	
	for x in range(0, Height):
		for y in range(0, Width):
			for c in range(0, Channels):
				New_Image[x,y,c] = 255 - Image[x,y,c]
	return New_Image

def main():
	Input_Image = cv.imread("Test_Image.png")
	
	Inverted_Image = Image_Inversion(Input_Image)
	
	cv.imwrite("Inverted_Image.png", Inverted_Image)
	input("Please Enter to Continue...")

if __name__ == '__main__':
	main()