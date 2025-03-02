from singlegraph import SingleGraph

class SingleStepsGraph(SingleGraph):
    def __init__(self, ax, length, width, number, distance):
        super().__init__(ax)
        self.length = length
        self.width = width
        self.distance = distance
        self.number = number
        self.create_steps_graph()

    def create_steps_graph(self):
        self.create_line(linelength=self.start_and_end_line_length, direction='right')
        self.create_steps('up')
        self.create_steps('down')
        self.create_line(linelength=self.distance, direction='right')
        self.create_steps('down')
        self.create_steps('up')
        self.create_line(linelength=self.start_and_end_line_length, direction='right')

