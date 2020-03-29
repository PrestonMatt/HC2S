try:
    from PIL import Image, ImageColor
    import imageInterpreter
    from matplotlib.pyplot import plot
except ModuleNotFoundError:
    print("Import failed; module not found.")

#goal of this file:
#given an Image object,
#return 1d array of rgbval and brighness in an hilbert curve path pixel to pixel
#-------------------------------------------------------------------------------------------#
#we will get the hilbert curve by computing up
#mapping bits to cartesian coordinates
#therefore for the first psuedo hilbert curve we need
#a function that gives the last two bits
#returning n & 3 will do this: https://www.tutorialspoint.com/python3/python_basic_operators.htm
def order2HCbits(hil_index):
    return (hil_index & 3)

def pos_in_order2():
    return [[0,0], [0,1], [1,1], [1,0]]
    #notably, the order in hilbert curve will be like this
    #not 00 01 10 11

#go through an image, pixel to pixel
#in a hilbert curve way
#this will effectively be mapping curve corners to
#the cartesian coordinates that our computer needs.
#given N as height and width of image...
def iterative_hc(hil_index, N):
    temp = pos_in_order2()[order2HCbits(hil_index)]
    hil_index = (hil_index >> 2);

    #print(temp)

    x = temp[0]
    y = temp[1]

    
    #print(x)
    #print(y)

    for n in range(4, N+1):
        prev_n = n / 2
        #four cases:

        #0 & 3 is last two bits of 0000
        #therefore this position is: bottom left
        if(order2HCbits(hil_index) == 0):
            temp = x
            x = y
            y = temp
            #return None
        #1 & 3 is last two bits of 0001
        #therefore this position is: top left
        if(order2HCbits(hil_index) == 1):
            x = x
            y = y + prev_n
            #return None
        #0 & 3 is last two bits of 0010
        #therefore this position is: top right
        if(order2HCbits(hil_index) == 2):
            x = x + prev_n
            y = y + prev_n
            #return None
        #0 & 3 is last two bits of 0011
        #therefore this position is: bottom right
        if(order2HCbits(hil_index) == 3):
            temp = y
            y = (prev_n - 1) - x
            x = (prev_n - 1) - temp
            x = x + prev_n
            #return None
            
        hil_index >> 2
        n = n*2
    return [x,y]

#initial goal, we need an image of power of 2 in area
def check_image(N):
    dim = float(N)
    while(dim > 1.0):
        dim = (dim / 2.0)
        #test: print(dim)
    if(dim == 1.0): #we have a square image
        print("Image fine")
        return True
    
    #otherwise, area will be less than 1 as a decimal
    print("Image will not be fit to a hilbert curve")
    return False

def hil_curve_list(photo_dim):
    hc2c = []
    if(check_image(photo_dim)):
        for x in range((photo_dim*photo_dim)+1):
            curnt = iterative_hc(x,photo_dim)
            hc2c.append(curnt)
    return hc2c

#get img:
img = imageInterpreter.return_image()
wid_hig = imageInterpreter.image_data(img)
print(wid_hig)

#try:
    #get img:
#    img = imageInterpreter.return_image()
#    wid_hig = imageInterpreter.image_data(img)
#    print(wid_hig)
    #wid_hig = imageInterpreter.image_data()
#    if(wid_hig[0] != wid_hig[1]):
#        raise ValueError("Image is not square!")
    #assumeing image is square
    #iterative_hc(image_data()[0])
#except ValueError:
#    print(ValueError)
#except AttributeError:
#    print(AttributeError)
#else:
#    print("error unknown")
