try:
    from PIL import Image, ImageColor
    import imageInterpreter
except ModuleNotFoundError:
    print("Import failed; module not found.\nTry running the following command:\npip3 install -r requirements.txt")

#goal of this file:
#given an Image object,
#return 1d array of rgbval and brighness in an hilbert curve path pixel to pixel
#-------------------------------------------------------------------------------------------#
#we will get the hilbert curve by computing up
#mapping bits to cartesian coordinates

#go through an image, pixel to pixel
#in a hilbert curve way
#this will effectively be mapping curve corners to
#the cartesian coordinates that our computer needs.
#given N as height and width of image...
def iterative_hc(hil_index, N):
    #Starting point is always 0,0
    x, y = 0, 0
    #iteratively calculate the coordinate:
    for n in range(1, N):
        #size:
        prev_n = 1 << (n-1)

        #Determine if its Bottom Left, Top Left, Top Right, or Bottom Right
        quadrent_index = ((hil_index >> (2*(n-1))) & 0x3)

        #I need this to act like a switch
        #Bottom Left
        #0 & 3 is last two bits of 00...'00'
        if(quadrent_index == 0):
            #swap
            x, y = y, x

        #Top Left
        #1 & 3 is last two bits of 00...'01'
        elif(quadrent_index == 1):
            #add size to y and leave x be
            y += prev_n

        #Top Right
        #2 & 3 is last two bits of 00...'10'
        elif(quadrent_index == 2):
            #add size to x AND y
            x += prev_n
            y += prev_n

        #Bottom Right
        #3 & 3 is last two bits of 00...'11'
        elif(quadrent_index == 3):
            #swap and subtract size
            x, y = prev_n - 1 - y, prev_n - 1 - x
            #flip x again
            x += prev_n

        #Place Holder
        else:
            raise ValueError("Invalid quad index")
    return [x, y]

#initial goal, we need an image of power of 2 in area
def check_image(N):
    dim = float(N)
    while(dim > 1.0):
        dim = (dim / 2.0)
        #test: print(dim)
    if(dim == 1.0): #we have a power of 2 & square image
        #print("Image fine")
        return True
    
    #otherwise, area will be less than 1 as a decimal
    raise ValueError("Image will not be fit to a hilbert curve")
    return False

def hil_curve_list(photo_dim):
    hc2c = []
    if(check_image(photo_dim)):
        for x in range(photo_dim*photo_dim):
            curnt = iterative_hc(x,photo_dim)
            print(curnt)
            hc2c.append(curnt)
    return hc2c

#TODO:
def getting_image_and_curve():
    try:
        #get img:
        img = imageInterpreter.return_image()
        wid_hig = imageInterpreter.image_data(img)
        print(wid_hig)
        #wid_hig = imageInterpreter.image_data()
        #This should already be taken care of by the compression function
        #if(wid_hig[0] != wid_hig[1]):
            #raise ValueError("Image is not square!")
        #assumeing image is square
        #iterative_hc(image_data()[0])
    except ValueError:
        print(ValueError)
    except AttributeError:
        print(AttributeError)
    else:
        print("error unknown")
