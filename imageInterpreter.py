try:
    #import sys
    import tkinter as tk
    from tkinter import filedialog
    import os
    #import matplotlib image capabilities
    import matplotlib.image as mpimg
    import matplotlib.pyplot as plt
    #image handling
    from PIL import Image, ImageColor
except ModuleNotFoundError:
    print("Import failed; module not found.")

#import image
#create a window 
#where you can import your own images
def wind():
    #print("Starting program...")
    root = tk.Tk()
    root.title("HC2L")
    root.maxsize(1000,1000)
    root.minsize(300,300)

    button = tk.Button(root,
                       text = "Import Picture",
                       fg = "green",
                       command = picture_import)
    button.pack()
    
    #now after clicking the button, we should have the image
    
    root.mainloop()
    #after we exit the window, image should appear.

def picture_import():
    filename = filedialog.askopenfilename(initialdir = "/",
                                          title = "Select file",
                                          filetypes = (
                                              ("all files","*.*"),
                                              ("jpeg files","*.jpeg"),
                                              ("png files","*.png"),
                                              ("jpg files","*.jpg")))
    #now we have the file name and location
    #time to import the picture.
    global img
    try:
        img = mpimg.imread(filename)
        #plt.imshow(img)
    except ValueError:
        img = Image.open(filename)
        #img.show()
    else:
        img = mpimg.imread(filename,0)
        #plt.imshow(img)

    #now there should be a global variable named image

def return_image():
    wind()
    try:
        #img.show()
        return img
    except:
        print("Image not yet retrieved!")
        return None

#uses Pillow (PIL) to get various data about the image
def image_data(image):
    print(image[0])#.width)
    print(image[1])#.height)
    return(image.size)
    #print(return_image().width())
    #print(return_image().height())
    #width = img.width
    #height = img.height
    #print('width: ', width)
    #print('height:', height)
    #return(width,height)
    return(0,0)

