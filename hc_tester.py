try:
    import sys
    from matplotlib import pyplot as plt
    import hilbert_curve_parser
    import imageInterpreter
    from numpy import linspace
except ModuleNotFoundError:
    print("Import failed; module not found.\nTry running the following command:\npip3 install -r requirements.txt")

def main():
    app = imageInterpreter.ImageIngestApp()
    app.mainloop()
    #for order in range(6):
        #print("Plotting Hilbert Curve of order %d" % order)
        #plot_hcurve(2**order)
    #img = imageInterpreter.return_image()
    #imageInterpreter.write_resized_image_to_filesys(img)
    #hilbert_curve_parser.getting_image_and_curve()

def plot_hcurve(order:int):
    colors = list(linspace(0.0, 1.0, order*order))
    #print(colors)

    curves_points_order = hilbert_curve_parser.hil_curve_list(order)
    print(curves_points_order)
    print("Points successfully gathered.")
    for point_index in range(len(curves_points_order)):
        try:
            curr = curves_points_order[point_index]
            next_pnt = curves_points_order[point_index+1]

            xs = [curr[0], next_pnt[0]]
            ys = [curr[1], next_pnt[1]]

            #print("Current point: ", curr, "Next point: ", next_pnt)
            plt.plot(xs, ys, color = [colors[point_index],colors[point_index],colors[point_index]])
        except IndexError:
            break
        try:
            if(point_index / len(curves_points_order) == .25):
                print("\nQuarterway.")
            elif(point_index / len(curves_points_order) == .5):
                print("\nHalfway.")
            elif(point_index / len(curves_points_order) == .75):
                print("\nThree quarters way.")
        except ZeroDivisionError:
            continue
    
    print("\nPlotted.")
    plt.show()

if __name__ == "__main__":
    main()
