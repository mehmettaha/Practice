import numpy as np
import pandas as pd

def variable_correlation(variable1, variable2):
    
    direction1 = pd.Series([x-variable1.mean() > 0 for x in variable1])
    direction2 = pd.Series([x-variable2.mean() > 0 for x in variable2])
    same_or_not = direction1 == direction2
    
    num_same_direction = sum(same_or_not)        # Replace this with your code
    num_different_direction = len(variable1)-num_same_direction   # Replace this with your code
    print(direction1)
    print(direction2)
    print(same_or_not)
    
    return (num_same_direction, num_different_direction)
    
series1 = pd.Series([1,2,3,4])    
series2 = pd.Series([10,11,12,13])
variable_correlation(series1,series2)