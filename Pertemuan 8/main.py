import numpy as np

def avrg(arr):
    return np.median(arr)

def maxi(arr):
    return np.maximum(arr)

def mins(arr):
    return np.minimum(arr)

def ab_avg(arr):
    return sum(arr > avrg(arr))