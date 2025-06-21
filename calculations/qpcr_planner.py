import numpy as np
from scipy.stats import linregress

def calculate_regression(ct_values, log_copies):
    slope, intercept, r_value, _, _ = linregress(log_copies, ct_values)
    return {"slope": slope, "intercept": intercept, "r_squared": round(r_value**2, 4)}

def estimate_log_copy(ct, slope, intercept):
    return (ct - intercept) / slope

def estimate_ct(log_copy, slope, intercept):
    return slope * log_copy + intercept