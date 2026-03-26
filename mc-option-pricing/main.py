import numpy as np
from gbm_paths import generate_gbm_paths
from monte_carlo import monte_carlo_option_price
from black_scholes import black_scholes_price
from visualization import visualize_all

# user parameters
S0 = 100              # Spot price
K = 100               # Strike price
r = 0.03              # Risk-free rate
sigma = 0.25          # Volatility
T = 1.0               # Time to maturity years
steps = 252           # Time steps for GBM
paths = 10000         # Number of MC paths
option_type = "call"  # "call" or "put"

gbm_paths = generate_gbm_paths(S0, r, sigma, T, steps, paths, seed=42)

ST = gbm_paths[:, -1]
if option_type == "call":
    payoffs = np.maximum(ST - K, 0)
else:
    payoffs = np.maximum(K - ST, 0)

mc_price = np.exp(-r * T) * np.mean(payoffs)

mc_prices = np.cumsum(np.exp(-r * T) * payoffs) / np.arange(1, paths + 1)

bs_price = black_scholes_price(S0, K, r, sigma, T, option_type=option_type)

print(f"\nResults:\nMonte Carlo Price ({option_type}): {mc_price:.4f}")
print(f"Black-Scholes Price ({option_type}): {bs_price:.4f}")
print(f"Difference: {abs(mc_price - bs_price):.4f}\n")

visualize_all(gbm_paths, mc_prices, bs_price, payoffs, option_type)
