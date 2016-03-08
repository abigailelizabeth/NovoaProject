from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window

data = []
flows = []

with open('testfile.txt', 'r') as input:
    size, seed = [int(x) for x in input.readline().split()]
    # data = [[int(x) for x in line.split()] for line in input]
    for x in range(size):
        data.append([int(x) for x in input.readline().split()])
    for x in range(size):
        flows.append([int(x) for x in input.readline().split()])

class TestApp(App):
    def build(self):
        return self.root
    def generate_grid(self):
        size = int(self.root.ids.input_size.text)
        self.root.ids.output_label.text = 'Generating Matrix of ' + str(size) + '...'
        self.root.ids.matrix.cols = size
        self.root.ids.matrix.rows = size
        for x in range(0, size):
            self.root.ids.matrix.add_widget



TestApp().run()