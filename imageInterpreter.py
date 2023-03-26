try:
    #import sys
    import tkinter as tk
    from tkinter import filedialog
    import os
    #import matplotlib image capabilities
    import matplotlib.image as mpimg
    import matplotlib.pyplot as plt
    #image handling
    from PIL import Image, ImageColor, ImageTk
    #functions needed to compress the image
    from numpy import ceil, log2
    #from cv2 import resize, imwrite
except ModuleNotFoundError:
    print("Import failed; module not found.\nTry running the following command:\npip3 install -r requirements.txt")

class ImageIngestApp(tk.Tk):

    #Initialize the class
    def __init__(self):
            super().__init__()
            self.title("HC2L")
            #Dimensions of the window
            self.maxsize( 1920,1080 )
            self.minsize(int((.5)*1920), int( (.5)* 1080 ))

            #images_array = []
            image_inputed = 0
            #compressed_image = 0
            #To protect against DOS (if I put this on a website), I need to specify a max image size
            #Anything above a 4096 by 4096 image will be denied.
            #4096 * 4096 = 16,777,216 (max pixels)
            Image.MAX_IMAGE_PIXELS = 16777216
            
            #order of functions to execute:
            self.userInterface()
            #image = self.open_image(image_file_name)
            #width, height = self.image_data(image)
            #self.write_resized_image_to_filesys(image, (width, height))

    #import image, create a window 
    #Use window to import your own images
    def userInterface(self):
        import_button = tk.Button(self,
                           text = "Import Picture",
                           fg = "green",
                           command = self.picture_import)
        import_button.pack()
        #Put the button in the center
        import_button.place(relx=0.1, rely=0.1, anchor="center")
        #now after clicking the button, we should have the image
        #root.mainloop() <- this has been moved to main
        #after we exit the window, image should appear.

        #If you want to just use the default testing images:
        test_images_button = tk.Button(self,
                                       text = "Generate Test Pictures",
                                       fg = "green",
                                       command = self.test_images)
        test_images_button.pack()
        #Put the button in the center
        test_images_button.place(relx=0.1, rely=0.2, anchor="center")

        
        #If you want to just use the default testing images:
        make_compressed_image_button = tk.Button(self,
                                       text = "Save Compressed Image",
                                       fg = "green",
                                       command = self.write_resized_image_to_filesys)
        make_compressed_image_button.pack()
        #Put the button in the center
        make_compressed_image_button.place(relx=0.1, rely=0.3, anchor="center")

        #Display the images
        #Original Image:
        self.original_label = tk.Label(self)
        self.original_label.pack()
        #Compressed Image:
        self.compressed_label = tk.Label(self)
        self.compressed_label.pack()

        #test images
        #Mandelbrot
        self.mandelbrot_label = tk.Label(self)
        self.mandelbrot_label.pack()
        #Gaussian noise
        self.Gaussian_label = tk.Label(self)
        self.Gaussian_label.pack()
        #Linear Gradient
        self.linear_gradient_label = tk.Label(self)
        self.linear_gradient_label.pack()
        #Radial Gradient
        self.radial_gradient_label = tk.Label(self)
        self.radial_gradient_label.pack()

    def picture_import(self):
        #get the directory of this file to be able to locate the image quicker.
        initial_directory = os.path.dirname(os.path.abspath(__file__))
        #Actually upload the image:
        filename = filedialog.askopenfilename(initialdir = initial_directory,
                                              title = "Select file",
                                              filetypes = (
                                                  ("all files","*.*"),
                                                  ("jpeg files","*.jpeg"),
                                                  ("png files","*.png"),
                                                  ("jpg files","*.jpg")))
        #print("Image File Name: \"%s\"" % filename)
        self.open_image(filename)
        #From line self.image_inputed = img in open_image, we set the image

        #Display the images:
        #Display original image:
        print("MODE %s\n\n\n" % self.image_inputed.mode)
        #original_image = Image.fromarray(self.image_inputed)
        original_photo = ImageTk.PhotoImage(image=self.image_inputed)
        self.original_label.configure(image=original_photo)
        self.original_label.image = original_photo

        #Display Compressed image:
        compressed_image = self.compress_image(self.image_inputed,
                                               self.image_data(self.image_inputed))
        #compressed_image = Image.fromarray(compressed_image)
        compressed_photo = ImageTk.PhotoImage(compressed_image)
        self.compressed_label.configure(image=compressed_photo)
        self.compressed_label.image = compressed_photo

    def open_image(self, filename):
        #now we have the file name and location
        #time to import the picture.
        try:
            #Try Pillow's image open first:
            img = Image.open(filename)
            #img.show()
        #This will be raised if:
        #"the mode is not “r”, or if a StringIO instance is used for fp"
        #https://pillow.readthedocs.io/en/stable/reference/Image.html
        except ValueError:
            print("Some value error occured.\n\n\n")
            img = mpimg.imread(filename)
            #plt.imshow(img)
        except FileNotFoundError:
            print("The file cannot be found.")
        except PIL.UnidentifiedImageError:
            print("The image cannot be opened and identified.")
        except TypeError:
            img = mpimg.imread(filename,0)
            #plt.imshow(img)
        #else:
        #    img = mpimg.imread(filename,0)
            #plt.imshow(img)
        #Now there should be a variable named img containing the loaded image
        #There *should* be no further processing done on the image here
        self.image_inputed = img
        #print(self.image_inputed)

    #def return_image():
    #    wind()
    #    try:
            #img.show()
    #        return img
    #    except:
    #        print("Image not yet retrieved!")
    #        return None

    #uses Pillow (PIL) to get various data about the image
    def image_data(self, image) -> tuple[int,int]:
        if(image == 0):
            #haven't put in an image
            raise ValueError("Please put in an image!!")
        #DEPRICATED
        #print(image[0])#.width)
        #print(image[1])#.height)
        #return(image.size)
        #print(image.width())
        #print(image.height())
        #width = img.width
        #height = img.height
        #print('width: ', width)
        #print('height:', height)
        #return(width,height)
        #return(0,0)
        width = image.width
        height = image.height
        
        return(width,height)

    """
        Given the image as an array of color values, the original image height & width
        return a compressed image that is the original image shrunken down
        to the nearest power of 2 (under it)
        This works best for already square images.
    """
    def compress_image(self, image, dims:tuple[int, int]):
        #find the nearest (lower) power of 2 for the smaller dimension
        #dims = (current_width,current_height)
        current_width = dims[0]
        current_height = dims[1]
        
        lower_dimension = current_width
        #if the length is smaller, then set to length
        #otherwise defaults to width (which is smaller)
        #Don't care about equality case, since that is square.
        if(lower_dimension > current_height): 
            lower_dimension = current_height

        #Find the nearest lower power of 2, efficiently.
        #This is the highest (ceiling) log power, with log being base 2
        #Need int to round down to the nearest int so we're not getting a decimal
        #grabs the exponent e
        e = int(ceil(log2(lower_dimension)))
        #get our new width/height, by raising to that power
        new_high_wid = 2**e

        resized_image = image.resize((new_high_wid, new_high_wid))
        #cv2 resize function to resize the image
        #resized_image = image.transform(size=(new_high_wid, new_high_wid),
        #                                method=Image.AFFINE)
                                        #data=(0, 0, current_width, current_height))
        #resized_image = image.resize((new_high_wid, new_high_wid))
        return(resized_image)

    """
        Scaffolding for the function above.
        Call once picture_import/return_image gives us an img variable.
    """
    def write_resized_image_to_filesys(self):
        image = self.image_inputed
        if(image == 0):
            raise ValueError("No image input yet, please put in an image and try again!")
        image_prime = self.compress_image(image,self.image_data(image))
        image_prime.save(os.path.dirname(os.path.abspath(__file__)) + "resized.jpg")
        #cv2 function to write the image
        #imwrite("compressed_image.png", image_prime)

    #Create some nice looking test images from the Pillow library
    #See here for details:
    #https://pillow.readthedocs.io/en/stable/reference/Image.html
    def test_images(self):
        #size, extent, quality
        mandelbrot_ex = Image.effect_mandelbrot(size=(256,256),
                                                extent=(0,0,256,256),
                                                quality=100)
        gaussian_noise = Image.effect_noise(size=(256,256), sigma=99)
        linear_grad = Image.linear_gradient(mode = "1")
        rad_grad = Image.radial_gradient(mode = "1")

        #self.images_array.append(mandelbrot_ex)
        #self.images_array.append(gaussian_noise)
        #self.images_array.append(linear_grad)
        #self.images_array.append(rad_grad)

        #Display them:
        #Mandelbrot
        mandelbrot_photo = ImageTk.PhotoImage(mandelbrot_ex)
        self.mandelbrot_label.configure(image=mandelbrot_photo)
        self.mandelbrot_label.image = mandelbrot_photo
        #Place it at 30%, 30%
        self.mandelbrot_label.place(relx=0.3, rely=0.3)
        
        #Gaussian Noise
        gaussian_photo = ImageTk.PhotoImage(gaussian_noise)
        self.Gaussian_label.configure(image=gaussian_photo)
        self.Gaussian_label.image = gaussian_photo
        #Place it at 30%, 40%
        self.Gaussian_label.place(relx=0.3, rely=0.8)
        
        #Linear Gradiant
        linear_gradient_photo = ImageTk.PhotoImage(linear_grad)
        self.linear_gradient_label.configure(image=linear_gradient_photo)
        self.linear_gradient_label.image = linear_gradient_photo
        #Place it at 60%, 30%
        self.linear_gradient_label.place(relx=0.6, rely=0.3)
        
        #Radial Gradiant
        radial_gradient_photo = ImageTk.PhotoImage(rad_grad)
        self.radial_gradient_label.configure(image=radial_gradient_photo)
        self.radial_gradient_label.image = radial_gradient_photo
        #Place it at 60%, 60%
        self.radial_gradient_label.place(relx=0.8, rely=0.6)
