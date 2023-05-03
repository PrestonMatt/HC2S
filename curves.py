
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
    #import itertools
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

def quirky_hil_curve(order):
    return(hilbert_curve_parser.hil_curve_list(order))

def snake_curve():

    return([[0,0]])

def peano_curve():

    return([[0,0]])

def macrotile_curve():

    return([[0,0]])

def e_curve():

    return([[0,0]])

def z_curve():

    return([[0,0]])

def moore_curve():

    return([[0,0]])

def random_curve():

    return([[0,0]])

def main():

    hcurve1 = hibert_curve(1,32)
    plotter(hcurve1)
    #proceed = input(">")
    
    #hilbert = hil_curve(64)
    hilbert = hil_curve(64)
    plotter(hilbert)
    #proceed = input(">")
    
    qhilbert = quirky_hil_curve(512)
    plotter(qhilbert)

    """
    snakes = snake_curve()
    plotter(snakes)
    plt.clf()

    peas = peano_curve()
    plotter(peas)
    plt.clf()

    macncheese = macrotile_curve()
    plotter(macncheese)
    plt.clf()

    ease = e_curve()
    plotter(ease)
    plt.clf()

    zese = z_curve()
    plotter(zese)
    plt.clf()

    mores = moore_curve()
    plotter(mores)
    plt.clf()

    randos = random_curve()
    plotter(randos)
    plt.clf()
    """
    
if __name__ == "__main__":
    main()
