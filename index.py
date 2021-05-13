import pyautogui #pip install pyautogui
import time
from datetime import datetime
from tkinter import *
import tkinter as tk
from tkinter import filedialog
import os
import cv2
from tkinter import * 
from tkinter.ttk import *
from PIL import Image
import numpy as np
from PIL import Image
from PIL import Image, ImageFilter

def UploadAction():
    filename = filedialog.askopenfilename()
    global fp
    fp=filename.replace("/", "//")
#print(fp)

def screenshot():
	root.withdraw()
	dt=datetime.now()
	filename=int(dt.strftime("%Y%m%d%H%M%S"))
	filename='E:\\Numpy\\ScreenshotData/{}.png'.format(filename)
	time.sleep(1)
	img=pyautogui.screenshot(filename)
	img.show()
	root.deiconify()

def grey(event=None):
	print(fp)
	#im = np.array(Image.open("E:\\PythonProject\\shiva.jpg"))
	im = np.array(Image.open(fp))
	im_i = 255 - im
	Image.fromarray(im_i).save('E:\\Numpy\\Image\\Grey.jpg')


def Black_white():
	im = np.array(Image.open(fp).convert('L')) #you can pass multiple arguments in single line
	gr_im= Image.fromarray(im).save('E:\\Numpy\\Image\\Black White.png')

def red():
	im = np.array(Image.open(fp))
	im_R = im.copy()
	im_R[:, :, (1, 2)] = 0
	pil_img = Image.fromarray(im_R)
	pil_img.save('E:\\Numpy\\Image\\Red.jpg')

def green():
	im = np.array(Image.open(fp))
	im_G = im.copy()
	im_G[:, :, (0, 2)] = 0
	pil_img = Image.fromarray(im_G)
	pil_img.save('E:\\Numpy\\Image\\Green.jpg')

def blue():
	im = np.array(Image.open(fp))
	im_B = im.copy()
	im_B[:, :, (0, 1)] = 0
	pil_img = Image.fromarray(im_B)
	pil_img.save('E:\\Numpy\\Image\\Blue.jpg')


def color_reduction1():
	im = np.array(Image.open(fp))
	im_32 = im // 32 * 32
	Image.fromarray(im_32).save('E:\\Numpy\\Image\\color_reduction1.jpg')

def color_reduction2():
	im = np.array(Image.open(fp))
	im_64 = im // 64 * 64
	Image.fromarray(im_64).save('E:\\Numpy\\Image\\color_reduction2.jpg')

def color_reduction3():
	im = np.array(Image.open(fp))
	im_128 = im // 128 * 128
	Image.fromarray(im_128).save('E:\\Numpy\\Image\\color_reduction3.jpg')


def paste_with_slice():
	src = np.array(Image.open(fp).resize((128, 128)))
	dst = np.array(Image.open(fp).resize((256, 256)))
	dst_copy = dst.copy()
	dst_copy[64:192, 64:192] = src
	Image.fromarray(dst_copy).save('E:\\Numpy\\Image\\paste_with_slice.jpg')

def rotate_clockwise_90():
	img = cv2.imread(fp)
	img_rotate_90_clockwise = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
	cv2.imwrite('E:\\Numpy\\Image\\rotate_clockwise_90.jpg', img_rotate_90_clockwise)

def rotate_clockwise_270():
	img = cv2.imread(fp)
	img_rotate_90_counterclockwise = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)
	cv2.imwrite('E:\\Numpy\\Image\\rotate_clockwise_270.jpg', img_rotate_90_counterclockwise)

def rotate_clockwise_180():
	img = cv2.imread(fp)
	img_rotate_180 = cv2.rotate(img, cv2.ROTATE_180)
	cv2.imwrite('E:\\Numpy\\Image\\rotate_clockwise_180.jpg', img_rotate_180)

def rotate_normal():
	im = np.array(Image.open(fp))
	Image.fromarray(im).save('E:\\Numpy\\Image\\rotate_normal.jpg')

def red_green_blue():
	im_gray = np.array(Image.open(fp).convert('L'))
	im_bool = im_gray > 128
	im_dst = np.empty((*im_gray.shape, 3))
	r, g, b = 255, 128, 32
	im_dst[:, :, 0] = im_bool * r
	im_dst[:, :, 1] = im_bool * g
	im_dst[:, :, 2] = im_bool * b
	Image.fromarray(np.uint8(im_dst)).save('E:\\Numpy\\Image\\red_green_blue.jpg')


def blur():
	OriImage = Image.open(fp)
	OriImage.show()

	blurImage = OriImage.filter(ImageFilter.BLUR)
	blurImage.show()
	#Save blurImage
	blurImage.save('E:\\Numpy\\Image\\BlurImage.jpg')

def box_blur():
	#Open existing image
	OriImage = Image.open(fp)
	OriImage.show()
	#Applying BoxBlur filter
	boxImage = OriImage.filter(ImageFilter.BoxBlur(5))
	boxImage.show()
	#Save Boxblur image
	boxImage.save('E:\\Numpy\\Image\\BlurImageBox.jpg')

def curve_blur():
	OriImage = Image.open(fp)
	OriImage.show()
	gaussImage = OriImage.filter(ImageFilter.GaussianBlur(5))
	gaussImage.show()
	gaussImage.save('E:\\Numpy\\Image\\BlurImageCurve.jpg')


def grey_black():
	im = cv2.imread(fp)
	im_gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
	th, im_gray_th_otsu = cv2.threshold(im_gray, 128, 192, cv2.THRESH_OTSU)
	cv2.imwrite('E:\\Numpy\\Image\\grey_black.jpg', im_gray_th_otsu)



root = tk.Tk()

root.geometry("600x900")
root.title("PLAY WITH IMAGES....")


my_label=Label(root, text="SCREENSHOT", width=25, background="pink",font=('bold',16))
my_label.configure(anchor=CENTER)
my_label.pack()
my_button1=tk.Button(root, text="TAKE SCREENSHOT",width=20, command=screenshot,font=('bold',10),bg='lightgreen')
my_button1.pack(pady=15)
my_button2=tk.Button(root, text="QUIT",width=20,command=quit,font=('bold',10),bg='skyblue')
my_button2.pack()




canvas_width = 500
canvas_height = 40
w = Canvas(root, width=canvas_width,height=canvas_height)
w.pack()
y = int(canvas_height / 2)
w.create_line(0, y, canvas_width, y, fill="#476042")


my_label=Label(root, text="IMAGE PROCESSING", width=25, background="yellow",font=('Helvtica',16))
my_label.configure(anchor=CENTER)
my_label.pack()
button = tk.Button(root, text='Select Image from Galary.', command=UploadAction, fg='white', bg='blue',width=25, font=('Helvtica'))
button.pack(pady=10)


button = tk.Button(root, text='GREY',width=20, bg='grey',fg='white',command=grey,font=('bold',10))
button.pack()
#button.pack(pady=10)

button = tk.Button(root, text='BLACK_WHITE', bg='black',fg='white',width=20, command=Black_white,font=('bold',10))
button.pack() 

button = tk.Button(root, text='RED', width=20, bg='red',fg='white',command=red,font=('bold',10))
button.pack() 

button = tk.Button(root, text='GREEN', width=20, bg='green',fg='white',command=green,font=('bold',10))
button.pack()  

button = tk.Button(root, text='BLUE', width=20,bg='blue',fg='white',command=blue,font=('bold',10))
button.pack() 
button = tk.Button(root, text='RED_GREEN_BLUE', bg='lime',fg='white',width=20, command=red_green_blue,font=('bold',10))
button.pack()


button = tk.Button(root, text='COLOR_REDUCTION1', bg='maroon',fg='white',width=20, command=color_reduction1,font=('bold',10))
button.pack() 

button = tk.Button(root, text='COLOR_REDUCTION2', bg='orange',fg='white',width=20, command=color_reduction2,font=('bold',10))
button.pack()
button = tk.Button(root, text='COLOR_REDUCTION#',bg='brown',fg='white', width=20, command=color_reduction3,font=('bold',10))
button.pack()
button = tk.Button(root, text='GREY_BLACK', bg='teal',fg='white',width=20, command=grey_black,font=('bold',10))
button.pack()
button = tk.Button(root, text='PASTE_WITH_SLICE',bg='violet',fg='white', width=20, command=paste_with_slice,font=('bold',10))
button.pack()


button = tk.Button(root, text='ROTATE_90',bg='silver',fg='black', width=20, command=rotate_clockwise_90,font=('bold',10))
button.pack()
button = tk.Button(root, text='ROTATE_270', bg='gold',fg='black',width=20, command=rotate_clockwise_270,font=('bold',10))
button.pack()
button = tk.Button(root, text='ROTATE_180', width=20, bg='orchid',command=rotate_clockwise_180,font=('bold',10))
button.pack()
button = tk.Button(root, text='ROTATENORMAL', width=20, bg='wheat',command=rotate_normal,font=('bold',10))
button.pack()

button = tk.Button(root, text='BLUR', width=20, bg='crimson',command=blur,font=('bold',10))
button.pack()
button = tk.Button(root, text='BOXBLUR', width=20, bg='navy',fg='white',command=box_blur,font=('bold',10))
button.pack()
button = tk.Button(root, text='CURVEBLUR', width=20, bg='coral',fg='black',command=curve_blur,font=('bold',10))
button.pack()

root.mainloop()
