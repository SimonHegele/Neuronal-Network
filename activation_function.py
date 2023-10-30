from math import exp

class Step_function():

    def __init__(self, threshold: float):

        self.threshold = threshold

    def eval(self, x: float)->int:

        return int(x>self.threshold)
    
class Generalized_logistic_function():

    def __init__(self, alpha: float, c=0)->float:

        if not alpha > 0:
            print('Alpha must be greater than 0')
        else:
            self.alpha = alpha
            self.c     = c

    def eval(self, x):

        return (1+exp(-x))**-self.alpha + self.c
    