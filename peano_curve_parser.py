try:
    #from PIL import Image, ImageColor
    #import imageInterpreter
    import numpy as np
except ModuleNotFoundError:
    print("Import failed; module not found.\nTry running the following command:\npip3 install -r requirements.txt")

"""
    Goal of this file:
    Given a the dimension of an image,
    return 1d array of the Peano curve path,
    which will represent the walking path pixel to pixel.
    #-------------------------------------------------------------------------------------------#
    We will get the Peano curve by iteratively walking from point to point.
"""
def iterative_pc(N:int): # -> np.array():
    """
        This function will create the array to instruct how to 
        go through an image, pixel to pixel in a Peano curve way.
        
        This will effectively be mapping the Peano curve to
        the cartesian coordinates that our computer needs.
        
        This is all done just given N which represents 
        the height slash width of image.
    """
    
    #Initial values:
    flipped = False
    x = 0
    y = 0
    starting_point = [x, y]

    #Begin construction of the Peano Curve to Coordinates (pc2c)
    pc2c = []
    pc2c.append(starting_point)

    #zeroth dimension is always just 0,0
    if(N == 0):
        return(pc2c)
    #N is one dimension of the photo.

    for pea_index in range(N*N):
        #define x and y for the current point:
        X = pc2c[pea_index][0]
        Y = pc2c[pea_index][1]

        #Where are we in the curve? See helper func for details
        step = pea_index % 9
        """
            Check if we need to flip the curve: this will be done by a flip flopping boolean.
            Variable "flipped" will act as the flag for flipping the base curve.
            The flag starts in the initial state False because the first peano curve is not flipped.

            The cycle re-ups every other mod 9 cycle, so var flipped should change then.
            Recall indexing in python starts at 0. So the first cycle completes at index 8.

            The first flip should be at 9, (the first index of the next peano curve).
            We don't want it to flip at index 0 since that is the first peano curve.
            
            Recall: step = pea_index % 9 and since 0 mod 9 is 0 we can ignore pea_index == 0.
        """
        if(step == 0 and pea_index != 0):
            flipped = not(flipped)

        nxt_point = next_point(X,Y,step,flipped)
        nxt_point = [ nxt_point[0], nxt_point[1] ]

        pc2c.append(nxt_point)

    return(pc2c)

def next_point(X:int,Y:int,step:int,flipped:bool) -> tuple:
    """
        Given the step, returns the changed position of x and y
          3
        []-[] []
        |2 4| 8|
        [] [] []
        |1 5| 7|
        [] []-[]
             6
        
        Steps along the peano curve:
                 |                               |
        [3]-[4] [9]-        [0, 2] - [1, 2]   [2, 2] - 
         |   |   |             |        |        |
        [2] [5] [8]         [0, 1]   [1, 1]   [2, 1]
         |   |   |             |        |        |
        [1] [6]-[7]         [0, 0]   [1, 0] - [2, 0]
        Represented as a numpy array this is: 
        base = np.array([[0, 0],
                     [0, 1],
                     [0, 2],
                     [1, 2],
                     [1, 1],
                     [1, 0],
                     [2, 0],
                     [2, 1],
                     [2, 2]])

        Sometimes we may need to flip it:
          |                     |
        -[9] [4]-[3]       - [0, 2]   [1, 2] - [2, 2]
          |   |   |             |        |        |
         [8] [5] [2]         [0, 1]   [1, 1]   [2, 1]
          |   |   |             |        |        |
         [7]-[6] [1]         [0, 0] - [1, 0]   [2, 0]
        Represented as a numpy array this is: 
        base = np.array([[2, 0],
                     [2, 1],
                     [2, 2],
                     [1, 2],
                     [1, 1],
                     [1, 0],
                     [0, 0],
                     [0, 1],
                     [0, 2]])

        Given the previous point, this function should return the next point.
        We can break this down into sub functions. For example, given point 1,
        we can say "go up by one". This can be translated into computer code to be
        y += 1.
        The only difference is that for 3 to 4, and 6 to 7, the direction is flipped
        each time.
        So if [something] %2 == 0, we go with the original direction of right (x+=1), otherwise, left.

        Enumerating/outlining the options here (a switch/case would be best here):
        step = peano_curve_index % 9
        flipped = every other curve

        if step == 1, "Go up by one" -> y += 1
        if step == 2, "Go up by one" -> y += 1
        if step == 3, 
            if flipped is even, "Go right by one" -> x += 1
            if flipped is odd, "Go left by one" -> x -= 1
        if step == 4, "Go down by one" -> y -= 1
        if step == 5, "Go down by one" -> y -= 1
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
        
        Optimization: It would be best if this was iterative and not recursive.
        As well, np arrays are better memory-wise than python lists
        Finally, potentially caching or saving lower order curves may speed it up.
    """
    """
        Side note: https://www.freecodecamp.org/news/python-switch-statement-switch-case-example/
        Python 3.10 and above has actually implimented the switch as match
    """
    """
        recall step = index % 9.
        So:
        if step % 9 == 1, then we are at the 1st spot
        if step % 9 == 2, then we are at the 2nd spot
        if step % 9 == 3, then we are at the 3rd spot
        if step % 9 == 4, then we are at the 4th spot
        if step % 9 == 5, then we are at the 5th spot
        if step % 9 == 6, then we are at the 6th spot
        if step % 9 == 7, then we are at the 7th spot
        if step % 9 == 8, then we are at the 8th spot
        if step % 9 == 0, then we are at the 9th spot
    """
    x = X
    y = Y
    match(step):
        case 1:
            y += 1
        case 2:
            y += 1
        case 3:
            if(flipped):
                x -= 1
            else:
                x += 1
        case 4:
            y -= 1
        case 5:
            y -= 1
        case 6:
            if(flipped):
                x -= 1
            else:
                x += 1
        case 7:
            y += 1
        case 8:
            y += 1
        case 0:
            #TODO make this work
            return(X,Y) 
        case _:
            print("Default case")

    return((x,y))

#TODO: make sure this works    
#initial goal, we need an image of power of 3 in area
def check_image(N:int) -> bool:
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

def pea_curve_list(photo_dim:int):
    if(check_image(photo_dim)):
        pc2c = iterative_pc(photo_dim)
    return(pc2c)