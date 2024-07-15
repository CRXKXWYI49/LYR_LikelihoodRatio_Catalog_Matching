import numpy as np
from typing import Callable

from adam_optimizer import AdamOptimizer



class GradientDescent:
    def __init__(
        self, 
        learning_rate=0.001, 
        beta1=0.9, 
        beta2=0.999, 
        epsilon=1e-8, 
        num_iterations=1000
    ):
        self.learning_rate = learning_rate
        self.beta1 = beta1
        self.beta2 = beta2
        self.epsilon = epsilon
        self.num_iterations = num_iterations

    def run_gradient_descent(
        self,
        function: Callable, 
        initial_params, 
    ):
        optimizer = AdamOptimizer(
            self.learning_rate, 
            self.beta1, 
            self.beta2, 
            self.epsilon
        )

        params = np.array(initial_params, dtype=float)

        for i in range(self.num_iterations):
            
            grads = self.numerical_gradient(function, params)
            params = optimizer.update(params, grads)

            cost = function(*params)
            print(f"Iteration {i}, Cost: {cost}")

        return params


    def numerical_gradient(self, f, params, epsilon):
        grads = np.zeros_like(params)
        for i in range(len(params)):
            params_up = np.array(params, dtype=float)
            params_down = np.array(params, dtype=float)

            params_up[i] += epsilon
            params_down[i] -= epsilon

            grads[i] = (f(*params_up) - f(*params_down)) / (2 * epsilon)

        return grads