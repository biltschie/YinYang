from singlegraph import SingleGraph

class SingleDomeGraph(SingleGraph):
    def __init__(self, ax, radius, distance):
        super().__init__(ax)
        self.radius = radius
        self.distance = distance
        self.create_dome_graph()

    def create_dome_graph(self):
        self.create_line(linelength=self.start_and_end_line_length)
        self.create_semicircle(self.radius, positive=1)
        self.create_line(self.distance)
        self.create_semicircle(self.radius, positive=-1)
        self.create_line(linelength=self.start_and_end_line_length)