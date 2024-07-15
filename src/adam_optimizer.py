import numpy as np

class AdamOptimizer:
    def __init__(self, learning_rate=0.001, beta1=0.9, beta2=0.999, epsilon=1e-8):
        self.learning_rate = learning_rate
        self.beta1 = beta1
        self.beta2 = beta2
        self.epsilon = epsilon
        self.m = None
        self.v = None
        self.t = 0

    def update(self, params, grads):
        if self.m is None:
            self.m = np.zeros_like(params)
            self.v = np.zeros_like(params)

        self.t += 1

        self.m = self.beta1 * self.m + (1 - self.beta1) * grads
        self.v = self.beta2 * self.v + (1 - self.beta2) * (grads ** 2)

        m_hat = self.m / (1 - self.beta1 ** self.t)
        v_hat = self.v / (1 - self.beta2 ** self.t)

        params -= self.learning_rate * m_hat / (np.sqrt(v_hat) + self.epsilon)

        return params

def gradient_descent_adam(function, gradient_function, initial_params, learning_rate=0.001, beta1=0.9, beta2=0.999, epsilon=1e-8, num_iterations=1000):
    optimizer = AdamOptimizer(learning_rate, beta1, beta2, epsilon)
    params = initial_params

    for i in range(num_iterations):
        grads = gradient_function(params)
        params = optimizer.update(params, grads)
        
        if i % 100 == 0:
            cost = function(params)
            print(f"Iteration {i}, Cost: {cost}")

    return params
