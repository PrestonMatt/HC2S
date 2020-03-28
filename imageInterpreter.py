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
def main():
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
    try:
        #img.show()
        return img
    except:
        print("Image not yet retrieved!")
        return None

main()
try:
    return_image().show()
except:
    print("Image still not retrieved...")

