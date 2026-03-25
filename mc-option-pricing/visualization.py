import matplotlib.pyplot as plt
import numpy as np

plt.style.use("Solarize_Light2")

def plot_gbm_paths(paths):
    for path in paths:
        plt.plot(path, lw=1)
    plt.title("Simulated GBM Paths")
    plt.xlabel("Time Step")
    plt.ylabel("Price")
    plt.tight_layout()
    plt.show()

def plot_mc_convergence(mc_prices, bs_price, option_type="call"):
    x = np.arange(1, len(mc_prices) + 1)
    plt.plot(x, mc_prices, lw=2, label="Monte Carlo Price")
    plt.axhline(bs_price, linestyle="--", lw=2, label="Black-Scholes Price")
    plt.title(f"Monte Carlo {option_type.title()} Price Convergence")
    plt.xlabel("Number of Paths")
    plt.ylabel("Option Price")
    plt.legend()
    plt.tight_layout()
    plt.show()

def plot_payoff_distribution(payoffs, option_type="call"):
    plt.hist(payoffs, bins=40, alpha=0.8)
    plt.title(f"Distribution of Payoffs ({option_type.title()})")
    plt.xlabel("Payoff")
    plt.ylabel("Frequency")
    plt.tight_layout()
    plt.show()

def visualize_all(paths, mc_prices, bs_price, payoffs, option_type="call"):
    plot_gbm_paths(paths)
    plot_mc_convergence(mc_prices, bs_price, option_type)
    plot_payoff_distribution(payoffs, option_type)