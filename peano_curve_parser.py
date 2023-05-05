"""
try:
    from PIL import Image, ImageColor
    import imageInterpreter
except ModuleNotFoundError:
    print("Import failed; module not found.\nTry running the following command:\npip3 install -r requirements.txt")
"""

#goal of this file:
#given an Image object,
#return 1d array of rgbval and brighness in an hilbert curve path pixel to pixel
#-------------------------------------------------------------------------------------------#
#we will get the peano curve by computing up
#mapping bits to cartesian coordinates

#go through an image, pixel to pixel
#in a peano curve way
#this will effectively be mapping curve corners to
#the cartesian coordinates that our computer needs.
#given N as height and width of image...
def iterative_pc(pea_index, N):
    #Starting point is always 0,0
    x, y = 0, 0
    index = 1
    while index < N:

        #
        step = pea_index % 9

        #calculate where x should go to:
        #first, where are we on the base peano 3 by 3?
        diff_x = int(step / 3)
        diff_y = step % 3
        if(diff_x == 1):
            diff_y = 2 - diff_y
        
        if(index > 1):



        pea_index = int(pea_index / 3)
        index = index * 3
    return x, y

def position_pc(x,y,step):
    """
        Given the step, returns the changed position of x and y

        base = np.array([[0, 0],
                     [0, 1],
                     [0, 2],
                     [1, 2],
                     [1, 1],
                     [1, 0],
                     [2, 0],
                     [2, 1],
                     [2, 2]])
        
        Steps along the peano curve:
          3
        []-[] []
        |2 4| 8|
        [] [] []
        |1 5| 7|
        [] []-[]
             6
        
        [3]-[4] [9]
         |   |   |
        [2] [5] [8]
         |   |   |
        [1] [6]-[7]
        Sometimes we may need to flip it:
        [9] [4]-[3]
         |   |   |
        [8] [5] [2]
         |   |   |
        [7]-[6] [1]

        Given the previous point, this function should return the next point.
        We can break this down into sub functions. For example, given point 1,
        we can say "go up by one". This can be translated into computer code to be
        y += 1.
        The only difference is that for 3 to 4, and 6 to 7, the direction is flipped
        each time.
        So if [something] %2 == 0, we go with the original direction of right (x+=1), otherwise, left.

        Enumerating/outlining the options here (a switch/case would be best here):
        step = peano_curve_index % 9
        flipped = ?

        if step == 1, "Go up by one" -> y += 1
        if step == 2, "Go up by one" -> y += 1
        if step == 3, 
            if flipped is even, "Go right by one" -> x += 1
            if flipped is odd, "Go left by one" -> x -= 1
        if step == 4, "Go down by one" -> y += 1
        if step == 5, "Go down by one" -> y += 1
        if step == 6,
            if flipped is even, "Go right by one" -> x += 1
            if flipped is odd, "Go left by one" -> x -= 1
        if step == 7, "Go up by one" -> y += 1
        if step == 8, "Go up by one" -> y += 1
        if step == 9,
            This one is a special case because it connects the next curve.
            However, it actually follows the peano curve itself!
            So to calculate where x or y should go, we can think about zooming out 
            (or up if you think about it that way) an order and then doing the
            same code as above.
        
    """
    #TODO: impliment this code!
    return(None)

#TODO: make sure this works    
#initial goal, we need an image of power of 3 in area
def check_image(N):
    """
    dim = float(N)
    while(dim > 1.0):
        dim = (dim / 3.0)
        #test: print(dim)
    if(dim == 1.0): #we have a power of 3 & square image
        #print("Image fine")
        return True
    
    #otherwise, area will be less than 1 as a decimal
    raise ValueError("Image will not be fit to a hilbert curve")
    return False
    """
    return(True)

def pea_curve_list(photo_dim):
    pc2c = []
    if(check_image(photo_dim)):
        for x in range(photo_dim*photo_dim):
            curnt = iterative_pc(x,photo_dim)
            #print(curnt)
            pc2c.append(curnt)
    return(pc2c)