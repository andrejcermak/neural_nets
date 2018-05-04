import Tkinter as tk
from shadow import *


class NeuronPic:
    def __init__(self, x, y, lenght, height):
        self.x = x
        self.y = y
        self.xm = x + lenght / 2
        self.ym = y + height / 2
        self.lenght = lenght
        self.height = height
        self.pic = None
        self.filling = None

    def show(self):
        self.pic = canvas.create_rectangle(self.x, self.y, self.x + self.lenght, self.y + self.height, fill="white")

    def fill(self, percentage):
        self.pic = canvas.create_rectangle(self.x, self.y, self.x + self.lenght, self.y + self.height, fill="white")
        self.filling = canvas.create_rectangle(self.x, self.y, self.x + self.lenght*percentage, self.y + self.height, fill="gray80")


neurons = {}


def bad_test():
    global neurons, neural_net
    for name, node in neural_net.neurons.iteritems():
        node.is_calculated = False

    test = [{"input": {"x1": 1, "x2": 1, "x3": 0, "x4": 0, "x5": 0, "x6": 0, "x7": 0, "x8": 0},
             "output": {"c1": 1, "c2": 0, "c3": 0, "c4": 0, "c5": 0, "c6": 0, "c7": 0, "c8": 0}},
            {"input": {"x1": 1, "x2": 1, "x3": 1, "x4": 0, "x5": 0, "x6": 0, "x7": 0, "x8": 0},
             "output": {"c1": 1, "c2": 1, "c3": 1, "c4": 1, "c5": 0, "c6": 0, "c7": 0, "c8": 0}},
            {"input": {"x1": 1, "x2": 1, "x3": 1, "x4": 1, "x5": 1, "x6": 1, "x7": 0, "x8": 0},
             "output": {"c1": 1, "c2": 1, "c3": 1, "c4": 1, "c5": 1, "c6": 1, "c7": 1, "c8": 1}}]

    neural_net.fill_up(random.choice(test)["input"])
    for name, neuron in neurons.iteritems():
        neuron.fill(neural_net.neurons[name].actual_return)

def good_test():
    global neurons, neural_net, test
    for name, node in neural_net.neurons.iteritems():
        node.is_calculated = False

    neural_net.fill_up(random.choice(test)["input"])
    for name, neuron in neurons.iteritems():
        neuron.fill(neural_net.neurons[name].actual_return)


root = tk.Tk()
canvas = tk.Canvas(root, width=1000, height=1000, bd=0, background = "white")
canvas.pack()
for i in range(8):
    neurons["x"+str(i+1)] = NeuronPic(50, 200+i*100, 100, 50)

for i in range(3):
    neurons["h" + str(i + 1)] = NeuronPic(300, 500 + i * 100, 100, 50)

for i in range(8):
    neurons["c" + str(i + 1)] = NeuronPic(550, 200+i*100, 100, 50)

for name, neuron in neural_net.neurons.iteritems():
    for neib, w in zip(neuron.to, neuron.weights):
        a = neuron.name
        b = neib.name
        i =0
        reds = ["firebrick1","firebrick2","firebrick3","firebrick4"]
        greens = ["chartreuse","green2","green3","green4"]
        if w.value<0.0:
            canvas.create_line(neurons[a].xm, neurons[a].ym, neurons[b].xm, neurons[b].ym, fill = "firebrick3")
        else:
            canvas.create_line(neurons[a].xm, neurons[a].ym, neurons[b].xm, neurons[b].ym, fill = "green3")
for name, neuron in neurons.iteritems():
    neuron.show()

a = tk.Button(root, text="Good sample", command=good_test, height = 50, width = 50)
b = tk.Button(root, text="Bad sample", command=bad_test, height = 50, width = 50)

a.pack(side=tk.LEFT)
b.pack(side=tk.LEFT)
root.mainloop()


