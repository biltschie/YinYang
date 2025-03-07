from singlegraph import SingleGraph

class SingleRectangleGraph(SingleGraph):
    def __init__(self, ax, length, width, distance):
        super().__init__(ax)
        self.length = length
        self.width = width
        self.distance = distance
        self.create_rectangle_graph()

    def create_rectangle_graph(self):
        self.create_line(linelength=self.start_and_end_line_length)
        self.create_rectangle(self.width, self.length, direction='up')
        self.create_line(linelength=self.distance)
        self.create_rectangle(self.width, self.length, direction='down')
        self.create_line(linelength=self.start_and_end_line_length)
