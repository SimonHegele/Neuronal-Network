from numpy import average

from activation_function import *

class Neuron():
    '''
    Implements artificial neuron
    '''

    def __init__(self, activation_function):

        self.activation_function = activation_function
        self.input_neurons       = []
        self.weights             = {}
        self.external_input      = 0
        
    def add_input_node(self, input_neuron, weight=0):

        self.input_neurons.append(input_neuron)
        self.weights[input_neuron] = weight

    def remove_input_node(self, input_neuron):

        del self.weights[input_neuron]
        self.input_neurons.remove(input_neuron)

    def remove_input_node_by_index(self, index):

        input_neuron = self.input_neurons[index]
        self.remove_input_node(input_neuron)

    def activity(self):

        weighted_input_neuron_activities = [self.weight[input_neuron]*input_neuron.activity() for input_neuron in self.input_neurons]
        return self.activation_function(sum(weighted_input_neuron_activities)+self.external_input)

activation_function = Step_function()

n1 = Neuron(activation_function)
n2 = Neuron(activation_function)

n1.add_input_node(n2, 2)
print(n1.weights[n2])



    
