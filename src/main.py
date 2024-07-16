import sys
from typing import Callable

import numpy as np
sys.path.append("/Users/admin/Documents/GitHub/LYR_LikelihoodRatio_Catalog_Matching/src/LYR")

from run_lyr import run_lyr
from adam_optimizer import AdamOptimizer


file_input = "/Users/admin/Documents/GitHub/LYR_LikelihoodRatio_Catalog_Matching/src/data/edff_LYR.txt"
file_output = "/Users/admin/Documents/GitHub/LYR_LikelihoodRatio_Catalog_Matching/src/data/erass_LYR.txt"
file1 = "/Users/admin/Documents/GitHub/LYR_LikelihoodRatio_Catalog_Matching/src/data/edff_LYR.txt"
data_input = np.genfromtxt(file_input, delimiter=',')
data_output = np.genfromtxt(file_output, delimiter=',')
data1 = np.genfromtxt(file1, delimiter=',')

def objective_function(
        r_in_tm,
        r_fr,
        r_min_nm, 
        r_max_nm,
    ):
    LRth , CLRth, RLRth = run_lyr(
        r_in_tm,
        r_fr,
        r_min_nm, 
        r_max_nm,
        data_input,
        data_output,
        data1,
        21,
    )
    print(f"Completeness: {CLRth:.6f} Reliability: {RLRth:.6f} LR-Threshold: {LRth:.6f}")
    objective_value = -1 * (RLRth + CLRth)
    return objective_value

learning_rate = 1
beta1 = 0.9
beta2 = 0.999
epsilon = 1e-8
num_iterations = 100000

def numerical_gradient(f, params, epsilon):
    grads = np.zeros_like(params, dtype=float)
    for i in range(len(params)):
        params_up = np.array(params, dtype=float)
        params_down = np.array(params, dtype=float)
        params_up[i] += epsilon
        params_down[i] -= epsilon
        grads[i] = (f(*params_up) - f(*params_down)) / (2 * epsilon)
    return grads

def run_gradient_descent(
        function: Callable, 
        initial_params, 
    ):
        optimizer = AdamOptimizer(
            learning_rate,
            beta1,
            beta2,
            epsilon, 
        )
        params = np.array(initial_params, dtype=float)
        for i in range(num_iterations):
            grads = numerical_gradient(function, params, epsilon)
            params = optimizer.update(params, grads)
            if(params[0] > params[1]): params[1] = params[0] + epsilon
            if(params[1] > params[2]): params[2] = params[1] + epsilon
            if(params[2] > params[3]): params[3] = params[2] + epsilon 
            if(params[3] > 60): params[3] = 50
            cost = function(*params)
            print(f"Iteration {i}, Cost: {cost}")
            print(f"New parameters: {params}")
        return params

initial_params = [5, 6, 10, 30]

optimized_params = run_gradient_descent(
    objective_function, initial_params
)

print("Optimized parameters:", optimized_params)
