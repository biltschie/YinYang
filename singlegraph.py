import matplotlib.pyplot as plt
import numpy as np

class SingleGraph:
    def __init__(self, ax):
        self.ax = ax
        self.ax.set_aspect('equal') # Keeps the aspect ratio of graphs
        # self.ax.axis('off') # Hides x-axis and y-axis
        self.start_x = 0
        self.start_y = 0
        self.color = 'black'
        self.start_and_end_line_length = 20
    
    def create_line(self, linelength, direction='right'):
        if direction == 'right':
            line_x = [self.start_x, self.start_x + linelength]
            line_y = [self.start_y, self.start_y]
            self.start_x += linelength
        elif direction == 'up':
            line_x = [self.start_x, self.start_x]
            line_y = [self.start_y, self.start_y + linelength]
            self.start_y += linelength
        elif direction == 'down':
            line_x = [self.start_x, self.start_x]
            line_y = [self.start_y, self.start_y - linelength]
            self.start_y -= linelength
    
        self.ax.plot(line_x,line_y, c=self.color)

    def create_semicircle(self, radius, positive):
        diameter = radius * 2
        shift = radius + self.start_x
        semi_circle_x = np.linspace(self.start_x, self.start_x+diameter, 10000)
        semi_circle_y = (np.sqrt(radius**2 - (semi_circle_x - shift)**2) * positive) + self.start_y
        self.ax.plot(semi_circle_x, semi_circle_y, c=self.color)
        self.start_x += diameter

    def create_steps(self, number, width, length, direction):
        # Direction can be 'up' or 'down'
        for i in range(number):
            self.create_line(linelength=width, direction=direction)
            self.create_line(linelength=length, direction='right')

    def create_hybrid_graphs(self, length, width, number, radius, distance):
        self.create_line(linelength=self.start_and_end_line_length)
        self.create_steps(number, width, length, 'up')
        self.create_semicircle(radius, 1)
        self.create_line(linelength=length)
        self.create_steps(number, width, length, 'down')
        self.create_line(linelength=distance)
        self.create_steps(number, width, length, 'down')
        self.create_semicircle(radius, -1)
        self.create_line(linelength=length)
        self.create_steps(number, width, length, 'up')
        self.create_line(linelength=self.start_and_end_line_length)
