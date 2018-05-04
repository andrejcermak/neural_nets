from neural_net import *

neurons = ["x1","x2", "x3", "x4", "x5", "x6", "x7", "x8", "h1", "h2", "h3", "c1", "c2", "c3", "c4", "c5", "c6", "c7","c8"]
graph = {"x1": ["h1", "h2", "h3"],"x2": ["h1", "h2", "h3"], "x3": ["h1", "h2", "h3"], "x4": ["h1", "h2", "h3"],
         "x5": ["h1", "h2", "h3"], "x6": ["h1", "h2", "h3"], "x7": ["h1", "h2", "h3"], "x8": ["h1", "h2", "h3"],
         "h1":["c1", "c2", "c3", "c4", "c5", "c6", "c7","c8"], "h2":["c1", "c2", "c3", "c4", "c5", "c6", "c7","c8"],
         "h3":["c1", "c2", "c3", "c4", "c5", "c6", "c7","c8"]}

'''
# neural net with 2 hidden layers, not used right now
neurons = ["x1","x2", "x3", "x4", "x5", "x6", "x7", "x8", "a", "b", "c","q", "r", "s", "c1", "c2", "c3", "c4", "c5", "c6", "c7","c8"]
graph = {"x1": ["a", "b", "c"],"x2": ["a", "b", "c"], "x3": ["a", "b", "c"], "x4": ["a", "b", "c"],
         "x5": ["a", "b", "c"], "x6": ["a", "b", "c"], "x7": ["a", "b", "c"], "x8": ["a", "b", "c"],
         "a":["q", "r", "s"], "b":["q", "r", "s"],
         "c":["q", "r", "s"], "q":["c1", "c2", "c3", "c4", "c5", "c6", "c7","c8"], "r":["c1", "c2", "c3", "c4", "c5", "c6", "c7","c8"],
         "s":["c1", "c2", "c3", "c4", "c5", "c6", "c7","c8"]}
'''
neural_net = NeuralNet(neurons, graph)

for neuron in ["c1", "c2", "c3", "c4", "c5", "c6", "c7","c8"]:
    neural_net.forward_prop(neural_net.neurons[neuron])


# teaching
test = [{"input": {"x1": 1, "x2": 0, "x3": 0, "x4": 0, "x5": 0, "x6": 0, "x7": 0, "x8": 0},
        "output": {"c1": 1, "c2": 0, "c3": 0, "c4": 0, "c5": 0, "c6": 0, "c7": 0, "c8": 0}},
        {"input": {"x1": 1, "x2": 1, "x3": 1, "x4": 1, "x5": 0, "x6": 0, "x7": 0, "x8": 0},
        "output": {"c1": 1, "c2": 1, "c3": 1, "c4": 1, "c5": 0, "c6": 0, "c7": 0, "c8": 0}},
        {"input": {"x1": 1, "x2": 1, "x3": 1, "x4": 1, "x5": 1, "x6": 1, "x7": 1, "x8": 1},
        "output": {"c1": 1, "c2": 1, "c3": 1, "c4": 1, "c5": 1, "c6": 1, "c7": 1, "c8": 1}}]

for i in range(60000):
    ran = random.choice(test)
    neural_net.fill_up(ran["input"])
    neural_net.learn_v2(ran["input"], ran["output"])

neural_net.print_vertexes()

neural_net.print_vertexes()
