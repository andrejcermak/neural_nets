from neural_net import *

neurons = ["m", "s", "g", "p","q", "u"]
graph = {"m": ["p", "q"], "s": ["q"], "g": ["u"], "q": ["u"], "p": ["u"]}
neural_net = NeuralNet(neurons, graph)
# for name, node in neural_net.neurons.iteritems():
    # print node.name, node.weights

for name, neuron in neural_net.neurons.iteritems():
    for neib in neuron.to:
        print name, "to", neib.name

neural_net.neurons["m"].test = 1
neural_net.neurons["s"].test = 0
neural_net.neurons["g"].test = 1
print "start", neural_net.test_run(neural_net.neurons["u"])
print "start", neural_net.test_run(neural_net.neurons["u"])

print "0"
neural_net.print_vertexes()

neural_net.forward_prop(neural_net.neurons["u"])
print "1"
neural_net.print_vertexes()
tests = [{"m": 1, "s":0, "g": 1}, {"m": 1, "s":0, "g": 1},{"m": 1, "s":0, "g": 1}]
for i in range(1000000):
    # print i
    for name in ["m", "s", "g"]:
        inp = {"m": 1, "s":0, "g": 1}
        out = 0
        neural_net.neurons["m"].actual_return = 1
        neural_net.neurons["s"].actual_return = 0
        neural_net.neurons["g"].actual_return = 1
        neural_net.learn(neural_net.neurons[name], inp, out,1)
print "2"
neural_net.print_vertexes()

neural_net.neurons["m"].test = 1
neural_net.neurons["s"].test = 0
neural_net.neurons["g"].test = 1
print "start", neural_net.test_run(neural_net.neurons["u"])

# print neural_net.forward_prop(neural_net.neurons["u"])
