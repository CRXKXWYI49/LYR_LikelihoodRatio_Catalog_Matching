import numpy as np
import pandas as pd

from adam_optimizer import AdamOptimizer
from typing import Callable


class LYROptimizer:
    
    def __init__(
            self, 
            learning_rate=0.001, 
            beta1=0.9, 
            beta2=0.999, 
            epsilon=1e-8, 
            num_iterations=1000
        ):
        self.learning_rate = learning_rate
        self.beta1=beta1
        self.beta2=beta2
        self.epsilon = epsilon
        self.num_iterations=num_iterations

        self.objective_function


    def run_gradient_descent(
            self,
            function: Callable, 
            gradient_function: Callable, 
            initial_params, 
        ):

        optimizer = AdamOptimizer(
            self.learning_rate, 
            self.beta1, 
            self.beta2, 
            self.epsilon
        )

        params = initial_params

        for i in range(self.num_iterations):
            grads = gradient_function(params)
            params = optimizer.update(params, grads)
            cost = function(params)
            print(f"Iteration {i}, Cost: {cost}")

        return params


    def objective_function(reliability, completeness):
        objective_function = -1 * reliability * completeness
        return objective_function
    


        
