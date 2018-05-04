from neural_net import *

for i in range(100):
    neurons = ["m", "s", "g", "p", "q", "u"]
    graph = {"m": ["p", "q"], "s": ["q"], "g": ["u"], "q": ["u"], "p": ["u"]}
    neural_net = NeuralNet(neurons, graph)
    neural_net.neurons["m"].actual_return = 1
    neural_net.neurons["s"].actual_return = 0
    neural_net.neurons["g"].actual_return = 1
    # neural_net.forward_prop(neural_net.neurons["u"])

    for j in range(100000):
        # print i
        for name in ["m", "s", "g"]:
            inp = {"m": 1, "s": 0, "g": 1}
            out = {"u":0}
            neural_net.neurons["m"].actual_return = 1
            neural_net.neurons["s"].actual_return = 0
            neural_net.neurons["g"].actual_return = 1
            neural_net.learn(neural_net.neurons[name], inp, out, 1)
    neural_net.neurons["m"].test = 1
    neural_net.neurons["s"].test = 0
    neural_net.neurons["g"].test = 1
    print "test", neural_net.test_run(neural_net.neurons["u"])