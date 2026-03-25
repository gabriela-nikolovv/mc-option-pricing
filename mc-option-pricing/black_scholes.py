# Analytical Black-Scholes formula for European options.

import numpy as np
from scipy.stats import norm

def black_scholes_price(S0, K, r, sigma, T, option_type="call"):
    if sigma == 0 or T == 0:
        return 0
        
    d1 = (np.log(S0 / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    if option_type == "call":
        price = S0 * norm.cdf(d1) - K * np.exp(-r * T) * norm.cdf(d2)
    else:
        price = K * np.exp(-r * T) * norm.cdf(-d2) - S0 * norm.cdf(-d1)
    return price