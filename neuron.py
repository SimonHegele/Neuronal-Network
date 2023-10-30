from numpy import average

class Neuron():
    '''
    Implements artificial neuron
    '''

    def __init__(self, activation_function):

        self.activation_function = activation_function
        self.input_neurons       = None
        self.external_input      = None
