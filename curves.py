try:
    from matplotlib import pyplot as plt
    from matplotlib import cm
    from matplotlib.colors import LinearSegmentedColormap, ListedColormap
    #from matplotlib.pyplot import cycler
    #from matplotlib import colors as col
    import numpy as np
    from hilbertcurve.hilbertcurve import HilbertCurve
    from hilbert import decode, encode
    import hilbert_curve_parser
    import peano_curve_parser
    #import itertools
    from random import sample
except ModuleNotFoundError:
    print("Import failed; module not found.\nTry running the following command:\npip3 install -r requirements.txt")

def plotter(space_filling_curve):
    """
        This function inputs the given array (representing the
        space-filling curve) and plots it on matplotlib for visualization.
        The curve's color pallet is rainbowed so that you can easily follow the path of the curve.
        
        Refrence for matplotlib's rainbow-ization of lines:
        https://stackoverflow.com/questions/30079590/use-matplotlib-color-map-for-color-cycle/57227821#57227821
    """

    #plt.cla()

    N = 0
    try:
        N = space_filling_curve.size
    except AttributeError:
        N = len(space_filling_curve)

    """
        Other options for the gradiation include:
        plt.rcParams["axes.prop_cycle"] = plt.cycler("color", plt.cm.tab20c.colors)
        plt.rcParams["axes.prop_cycle"] = plt.cycler("color", plt.cm.viridis(np.linspace(0,1,N)))
        plt.rcParams["axes.prop_cycle"] = plt.cycler("color", plt.cm.plasma(np.linspace(0,1,N)))
        plt.rcParams["axes.prop_cycle"] = plt.cycler("color", plt.cm.inferno(np.linspace(0,1,N)))
        plt.rcParams["axes.prop_cycle"] = plt.cycler("color", plt.cm.magma(np.linspace(0,1,N)))
        Personally, I like gist_ncar, rainbow, and nipy_spectral
        etc.
        See: https://matplotlib.org/2.0.2/examples/color/colormaps_reference.html
    """
    plt.rcParams["axes.prop_cycle"] = plt.cycler("color", plt.cm.nipy_spectral(np.linspace(0,1,N)))
    fig, ax = plt.subplots()

    for point_index in range(N):
        try:
            curr = space_filling_curve[point_index]
            next_pnt = space_filling_curve[point_index+1]

            xs = [curr[0], next_pnt[0]]
            ys = [curr[1], next_pnt[1]]

            #print("Current point: ", curr, "Next point: ", next_pnt)
            ax.plot(xs, ys)
        except IndexError:
            break
        try:
            if(point_index / len(space_filling_curve) == .25):
                print("\nQuarterway.")
            elif(point_index / len(space_filling_curve) == .5):
                print("\nHalfway.")
            elif(point_index / len(space_filling_curve) == .75):
                print("\nThree quarters way.")
        except ZeroDivisionError:
            continue
    
    print("\nPlotted.")
    plt.show()
    
def hil_curve(num_of_points:int):
    indeces = np.array([])
    """
    for p in range (num_of_points):
        indeces = np.append(indeces, [p])
    """

    h_curve = decode([np.array(x) for x in range(num_of_points)],2,3)

    print(len(h_curve))

    return(h_curve)

#Refrence: https://pypi.org/project/hilbertcurve/
def hibert_curve(dimension,order):
    h = HilbertCurve(dimension, order)
    #Think of  this like when you lay out the curve on a 1d line how long it is
    total_distance = list(range(order*order))
    curve = h.points_from_distances(total_distance)
    #print(type(curve))
    print(curve)
    return(curve)

def quirky_hil_curve(order: int) -> list:
    return(hilbert_curve_parser.hil_curve_list(order))

def snake_curve(width:int) -> list:
    """
        Generates an S-curve given the side length of the
        square (image) it's trying to fill.
        This is the niave approach in the original video,
        and is meant for demonstration purposes.
        The problem with higher orders (larger widths) is
        that the locality of points is not preserved.
    """
    points = []
    for y in range(width+1):
        if(y % 2 == 0):
            for x in range(0,width+1,1):
                points.append([x,y])
        else: #y is odd
            for x in range(width,-1,-1): #starts at width, goes down until 0
                points.append([x,y])
    
    return(points)

def peano_curve(order):
    """
        Generates a sequence of points on the x,y
        plane for a Peano curve of given order.
    """
    return(peano_curve_parser.pea_curve_list(order))

def macrotile_curve_3():

    return([[0,0]])

def macrotile_curve_4():

    return([[0,0]])

def e_curve():

    return([[0,0]])

def z_curve(x:int, y:int, order:int) -> np.array:

    return([[0,0]])

def moore_curve():

    return([[0,0]])

def random_curve(width:int) -> list:
    
    points = []
    for x in range(width):
        for y in range(width):
            points.append([x,y])

    #Randomize it:
    points = sample(points,len(points))
    #print(points)
    
    return(points)

def main():
    peas = peano_curve(3)
    plotter(peas)
    """
    #hcurve1 = hibert_curve(1,32)
    #plotter(hcurve1)
    #proceed = input(">")
    
    #hilbert = hil_curve(64)
    #hilbert = hil_curve(64)
    #plotter(hilbert)
    #proceed = input(">")

    #un comment this when you want, but it current takes a long time.
    qhilbert = quirky_hil_curve(128)
    plotter(qhilbert)

    snakes = snake_curve(128)
    plotter(snakes)

    randos = random_curve(128)
    plotter(randos)

    peas = peano_curve(3)
    plotter(peas)

    #zese = z_curve(0,0,3)
    #plotter(zese)

    macncheese = macrotile_curve()
    plotter(macncheese)
  
    ease = e_curve()
    plotter(ease)
 
    mores = moore_curve()
    plotter(mores)
    """
    
if __name__ == "__main__":
    main()
