try:
    from matplotlib import pyplot as plt
    import hilbert_curve_parser
    from numpy import linspace
except ModuleNotFoundError:
    print("Import failed; module not found.")

N = 8

colors = list(linspace(0.0, 1.0, N*N))
#print(colors)

curves_points_order = hilbert_curve_parser.hil_curve_list(N)
print(curves_points_order)
print("points successfully gathered")
for point_index in range(len(curves_points_order)):
    try:
        curr = curves_points_order[point_index]
        next_pnt = curves_points_order[point_index+1]

        xs = [curr[0], next_pnt[0]]
        ys = [curr[1], next_pnt[1]]

        print("Current point: ", curr, "Next point: ", next_pnt)
        plt.plot(xs, ys, color = [colors[point_index],colors[point_index],colors[point_index]])
    except IndexError:
        break
    try:
        if(point_index / len(curves_points_order) == .25):
            print("\n", "quarterway")
        elif(point_index / len(curves_points_order) == .5):
            print("\n", "halfway")
        elif(point_index / len(curves_points_order) == .75):
            print("\n", "three quarters way")
    except ZeroDivisionError:
        continue
    
print("\n", "plotted")
plt.show()
