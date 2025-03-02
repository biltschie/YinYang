import matplotlib.pyplot as plt
import random
from singlegraph import SingleGraph
from dome import SingleDomeGraph
from rectangle import SingleRectangleGraph
from steps import SingleStepsGraph

def set_up(nrows, ncolumns):
    fig, axes = plt.subplots(nrows, ncolumns, sharex=True, sharey=True)
    fig.set_size_inches(20, 6)
    fig.tight_layout()
    # Setting the values for all axes.
    axes[0,0].set_xlim(0,240)
    axes[0,0].set_ylim(-56,56)
    return axes

def create_dome_graphs():
    nrows = 2
    ncolumns = 4
    axes = set_up(nrows, ncolumns)
    constant_radius = 30
    constant_distance = 10
    random_radii = random.sample(list(range(5, 50, 10)), ncolumns)
    random_distances = random.sample(list(range(5, 111, 20)), ncolumns)
    for i in range(ncolumns): # Change 0, 1 with row numbers
        SingleDomeGraph(axes[0,i], random_radii[i], constant_distance)
        SingleDomeGraph(axes[1,i], constant_radius, random_distances[i])
    plt.show()

def create_rectangle_graphs():
    nrows = 2
    ncolumns = 4
    axes = set_up(nrows, ncolumns)
    constant_length = 50
    constant_width = 20
    constant_distance = 20
    random_lengths = random.sample(list(range(5, 100, 10)), ncolumns)
    random_widths = random.sample(list(range(5, 50, 10)), ncolumns)
    random_distances = random.sample(list(range(5, 101, 20)), ncolumns)
    for i in range(ncolumns):
        SingleRectangleGraph(axes[0,i], random_lengths[i], random_widths[i], constant_distance)
        SingleRectangleGraph(axes[1,i], constant_length, constant_width, random_distances[i])
    plt.show()

def create_steps_graphs():
    nrows = 2 
    ncolumns = 4
    axes = set_up(nrows, ncolumns)
    constant_length = 5
    constant_width = 5
    constant_no_of_steps = 5
    constant_distance = 20
    random_lengths = random.sample(list(range(2, 10)), ncolumns)
    random_widths = random.sample(list(range(2, 10)), ncolumns)
    random_no_of_steps = random.sample(list(range(1, 6)), ncolumns)
    random_distances = random.sample(list(range(5, 101, 20)), ncolumns)
    for i in range(ncolumns):
        SingleStepsGraph(axes[0,i], random_lengths[i], random_widths[i], random_no_of_steps[i], constant_distance)
        SingleStepsGraph(axes[1,i], constant_length, constant_width, constant_no_of_steps, random_distances[i])
    plt.show()

def create_hybrid_graphs():
    nrows = 2 
    ncolumns = 4
    axes = set_up(nrows, ncolumns)
    constant_length_steps = 5
    constant_width_steps = 5
    constant_length_rectangle = 12
    constant_width_rectangle = 8
    constant_no_of_steps = 5
    constant_radius = 10
    constant_distance = 20
    random_lengths_rectangle = random.sample(list(range(14, 24)), ncolumns)
    random_widths_rectangle = random.sample(list(range(7, 12)), ncolumns)
    random_lengths_steps = random.sample(list(range(2, 6)), ncolumns)
    random_widths_steps = random.sample(list(range(2, 6)), ncolumns)
    random_no_of_steps = random.sample(list(range(1, 6)), ncolumns)
    random_radii = random.sample(list(range(5, 20, 3)), ncolumns)
    random_distances = random.sample(list(range(5, 74, 20)), ncolumns)
    
    for i in range(ncolumns):
        SingleGraph(axes[0,i]).create_hybrid_graph(random_lengths_rectangle[i], random_widths_rectangle[i], random_lengths_steps[i], random_widths_steps[i], random_no_of_steps[i], random_radii[i], constant_distance)
        SingleGraph(axes[1,i]).create_hybrid_graph(constant_length_rectangle, constant_width_rectangle, constant_length_steps, constant_width_steps, constant_no_of_steps, constant_radius, random_distances[i])
    plt.show()


if __name__ == "__main__":
    create_dome_graphs()
    create_rectangle_graphs()
    create_steps_graphs()
    create_hybrid_graphs()