"""
Script containing basic fundamentals of neural nets, implements them as graph with neurons as nodes.
Uses sigmoid function to calculate probabilities. learn_v2 is function, that implements self learning from input and
desired output.
"""


import random
import numpy as np

class Weight:
    def __init__(self, value):
        self.value = value


class Neuron:
    def __init__(self, name):
        self.name = name
        self.weights = []
        self.weights_from = []
        self.to = []
        self.fromm = []
        self.layer = -1
        self.actual_return = 0
        self.desired_return = 0
        self.delta = 0.5
        self.test = 0.5
        self.is_input = False
        self.is_hidden = False
        self.is_final = False
        self.is_calculated = False


class NeuralNet:
    def __init__(self,in_neurons, in_graph ):
        """Init net, create neurons, sort them out by layers and init random weights."""
        self.neurons = {}
        self.layers = []
        self.error = 0
        for n in in_neurons:
            neuron = Neuron(name = n)
            self.neurons[n] = neuron

        # connecting graph nodes
        for node, to in in_graph.iteritems():
            for vertex in to:
                weight = Weight(random.uniform(-1,1))
                self.neurons[node].to.append(self.neurons[vertex])
                self.neurons[node].weights.append(weight)
                self.neurons[vertex].fromm.append(self.neurons[node])
                self.neurons[vertex].weights_from.append(weight)

        # labeling neuron as input, hidden or final
        for name, node in self.neurons.iteritems():
            if node.fromm == []:
                self.__num_layers__(node, 0)
                node.is_input = True
            else:
                if node.to == []:

                    node.is_final = True
                else:
                    node.is_hidden = True

    def __str__(self):
        """Function to print all vertexes of graph."""
        for name, neuron in self.neurons.iteritems():
            for neib, w in zip(neuron.to, neuron.weights):
                print name, "to", neib.name, "with w:", w.value, " with actual val: ", neib.actual_return

    def __num_layers__(self, neuron, num):
        """Private function that numbers layers, starting with 0 as input node."""
        neuron.layer = num

        if len(self.layers) <= num:
            self.layers.append([neuron])
        else:
            self.layers[num].append(neuron)

        for neib in neuron.to:
            if neib.layer == -1:
                self.__num_layers__(neib, num + 1)

    def __nonlin__(self, x):
        """Returns sigmoid f(x)e(0,1)"""
        return 1 / (1 + np.exp(-x))

    def test_run(self, neuron, input):
        """Test function, returns output for given neuron and input."""
        if not neuron.is_input:
            sum = 0
            for i in range(len(neuron.fromm)):
                # print "name", neuron.fromm[i].name
                sum += self.test_run(neuron.fromm[i], input) * neuron.weights_from[i].value
            # print neuron.name, sum
            neuron.test = self.__nonlin__(sum)
        else:
            neuron.test = input[neuron.name]
        return neuron.test

    def fill_up(self, input):
        """Calculates return values for all neuron.s"""
        for name, neuron in self.neurons.iteritems():
            if neuron.is_input:
                neuron.actual_return = input[name]

        for name, neuron in self.neurons.iteritems():
            if neuron.is_final and not neuron.is_calculated:
                self.__forward_prop__(neuron)

    def __forward_prop__(self, neuron):
        """helper function for fill up (is recursive)"""
        if not neuron.is_input:
            sum = 0
            for i in range(len(neuron.fromm)):
                if neuron.fromm[i].is_calculated:
                    sum += neuron.fromm[i].actual_return * neuron.weights_from[i].value
                else:
                    sum += self.__forward_prop__(neuron.fromm[i]) * neuron.weights_from[i].value
            neuron.is_calculated = True
            neuron.actual_return = self.__nonlin__(sum)
        return neuron.actual_return

    def __change_weight__(self, neuron, delta):
        print "aaaaaa"
        for weight, neib in zip(final.weights, neuron.fromm):
            weight.value += delta*neib.actual_return

    def learn_v2(self, input, output):

        for name, val in input.iteritems():
            self.neurons[name].actual_return = val
        for name, val in output.iteritems():
            self.neurons[name].desired_return = val

        for name, node in self.neurons.iteritems():
            node.is_calculated = False

        # Feed forward through layers
        self.fill_up(input)
        delta = 0
        for final in self.layers[-1]:
            # how much did we miss the target value?
            error = final.desired_return - final.actual_return
            self.error += error
            # in what direction is the target value?
            # were we really sure? if so, don't change too much.
            delta = error * final.actual_return * (1 - final.actual_return)
            for weight, neib in zip(final.weights_from, final.fromm):
                weight.value += delta*neib.actual_return

        for i in range(len(self.layers)-1,0):
            error = []
            for final in self.layers[i]:
                error.append(0)
                for weight in final.weights:
                    error[-1] += weight.value*delta
            for er, final in zip(error, self.layers[i]):
                delta = er*final.actual_return*(1-final.actual_return)
                self.__change_weight__(delta, final)
