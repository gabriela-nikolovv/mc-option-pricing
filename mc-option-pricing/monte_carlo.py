# Monte Carlo pricing logic for European options

import numpy as np

def monte_carlo_option_price(S0, K, r, sigma, T, n_paths, option_type="call", seed=None):
    if seed is not None:
        np.random.seed(seed)
    Z = np.random.standard_normal(n_paths)
    ST = S0 * np.exp((r - 0.5 * sigma**2) * T + sigma * np.sqrt(T) * Z)
    if option_type == "call":
        payoffs = np.maximum(ST - K, 0)
    else:
        payoffs = np.maximum(K - ST, 0)
    price = np.exp(-r * T) * np.mean(payoffs)
    return price, payoffs