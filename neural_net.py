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
        self.actual_return = 0
        self.desired_return = 0
        self.delta = 0.5
        self.test = 0.5
        self.is_input = False
        self.is_hidden = False
        self.is_final = False


class NeuralNet:
    def __init__(self,in_neurons, in_graph ):
        # init neural net
        self.neurons = {}

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
                node.is_input = True
            else:
                if node.to == []:
                    node.is_final = True
                else:
                    node.is_hidden = True

    def nonlin(self, x):
        return 1 / (1 + np.exp(-x))

    def learn(self, neuron, input, output,r):

        if neuron.is_input:
            neuron.actual_return = input[neuron.name]
            neuron.delta = input[neuron.name]
        ''''''
        for i in range(len(neuron.to)):
            change = r*neuron.actual_return*self.learn(neuron.to[i], input, output, r)
            neuron.weights[i].value += change

        if neuron.is_final:
            neuron.desired_return = output[neuron.name]
            # l2_error
            err = self.nonlin(neuron.desired_return - neuron.actual_return)
            # l2_delta
            neuron.delta = err*neuron.actual_return * (1-neuron.actual_return)
            for w, fromm in zip(neuron.weights_from, neuron.fromm):
                w.value += fromm.actual_return * neuron.delta
            return neuron.delta

        if neuron.is_hidden:
            sum = 0
            for next, weight in zip(neuron.to, neuron.weights):
                sum += weight*next.delta
            neuron.delta = neuron.actual_return*(1-neuron.actual_return)*sum

            for w, fromm in zip(neuron.weights_from, neuron.fromm):
                w.value += fromm.actual_return * neuron.delta
            return neuron.delta

    def test_run(self, neuron, input):
        if not neuron.is_input:
            sum = 0
            for i in range(len(neuron.fromm)):
                # print "name", neuron.fromm[i].name
                sum += self.test_run(neuron.fromm[i], input) * neuron.weights_from[i].value

            # print neuron.name, sum
            neuron.test = self.nonlin(sum)
        else:
            neuron.test = input[neuron.name]
        return neuron.test

    def fill_up(self, input):
        for name, neuron in self.neurons.iteritems():
            if neuron.is_input:
                neuron.actual_return = input[name]

        for name, neuron in self.neurons.iteritems():
            if neuron.is_final:
                self.forward_prop(neuron)
                break
        for name, neuron in self.neurons.iteritems():
            if neuron.is_final:
                sum = 0
                for w, fromm in zip(neuron.weights_from, neuron.fromm):
                    sum += self.nonlin(w.value * fromm.actual_return)
                neuron.actual_return = sum/8

    def forward_prop(self, neuron):
        if not neuron.is_input:
            sum = 0
            for i in range(len(neuron.fromm)):
                sum += self.forward_prop(neuron.fromm[i]) * neuron.weights_from[i].value
            neuron.actual_return = self.nonlin(sum)
        return neuron.actual_return

    def print_vertexes(self):
        for name, neuron in self.neurons.iteritems():
            for neib, w in zip(neuron.to, neuron.weights):
                print name, "to", neib.name, "with w:", w.value, " with actual val: ", neib.actual_return


    def learn_simple(self, neuron, input, output):
        for name, val in input.iteritems():
            self.neurons[name].actual_return = val
        for name, val in output.iteritems():
            self.neurons[name].desired_return = val

        l1 = 0
        # np.dot(l0,syn0)
        for neib, wei in zip(neuron.fromm, neuron.weights_from):
            l1 += wei.value * neib.actual_return
        # = nonlin(np.dot(l0,syn0))
        l1 = self.nonlin(l1)
        l1_error = neuron.desired_return - l1
        # print "error rate ", abs(error)
        l1_delta = l1_error * l1 * (1 - l1)
        for neib, wei in zip(neuron.fromm, neuron.weights_from):
            wei.value += l1_delta*neib.actual_return