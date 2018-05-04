from neural_net import *
'''
neurons = ["x1","x2", "a", "c1", "c2"]
graph = {"x1": ["a"], "x2": ["a"], "a":["c1", "c2"]}
'''

neurons = ["x1","x2","x3", "a"]
graph = {"x1": ["a"], "x2": ["a"], "x3": ["a"]}

test = [{"input": {"x1": 1, "x2": 1},
        "output": {"a": 1}},
        {"input": {"x1": 1, "x2": 0},
         "output": {"a": 1}},
        {"input": {"x1": 0, "x2": 1},
        "output": {"a": 0}},
        {"input": {"x1": 0, "x2": 0},
         "output": {"a": 0}}]

test = [{"input": {"x1": 0, "x2": 0, "x3": 1},
        "output": {"a": 0}},
        {"input": {"x1": 1, "x2": 1, "x3": 1},
         "output": {"a": 1}},
        {"input": {"x1": 1, "x2": 0, "x3": 1},
        "output": {"a": 1}},
        {"input": {"x1": 0, "x2": 1, "x3": 1},
         "output": {"a": 0}}]

neural_net = NeuralNet(neurons, graph)
neural_net.print_vertexes()
print neural_net.test_run(neural_net.neurons["a"],test[0]["input"])

'''
for i in range(100000):
    t = random.choice(test)
    neural_net.fill_up(t["input"])
    neural_net.learn_simple(neural_net.neurons["a"], t["input"], t["output"])
'''

# neural_net.print_vertexes()
for i in range(10000):
    for t in test:
        neural_net.fill_up(t["input"])
        neural_net.learn_v2(t["input"], t["output"])

neural_net.print_vertexes()
x = neural_net.test_run(neural_net.neurons["a"],test[0]["input"])
print x
x = neural_net.test_run(neural_net.neurons["a"],test[1]["input"])
print x
x = neural_net.test_run(neural_net.neurons["a"],test[2]["input"])
print x
x = neural_net.test_run(neural_net.neurons["a"],test[3]["input"])
print x
x = neural_net.test_run(neural_net.neurons["a"],test[3]["input"])
print x
# neural_net.print_vertexes()