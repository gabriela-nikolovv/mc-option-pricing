# Monte Carlo Option Pricing 

### Overview

This project implements **Monte Carlo simulation** to price European options and compares the results with the analytical **Black-Scholes model**.

It demonstrates key concepts in quantitative finance:

* Stochastic processes (Geometric Brownian Motion)
* Risk-neutral pricing
* Monte Carlo estimation and convergence
* Analytical vs numerical pricing methods

---

### Features

* Simulation of asset price paths using **Geometric Brownian Motion (GBM)**
* Monte Carlo pricing of European **call and put options**
* Analytical pricing using the **Black-Scholes formula**
* Visualization of:

  * Simulated GBM paths
  * Monte Carlo convergence to the analytical price
  * Distribution of option payoffs
* Modular and reusable code structure

---

## Mathematical Background

### Geometric Brownian Motion

The underlying asset price is modeled as:

```
dS_t = r S_t dt + σ S_t dW_t
```

Discretized solution:

```
S_{t+Δt} = S_t * exp((r - 0.5σ²)Δt + σ√Δt Z)
```

### Monte Carlo Pricing

The option price is estimated as:

```
C ≈ e^{-rT} * (1/N) * Σ payoff(S_T)
```

Where:

* ( S_T ) = simulated terminal price
* Payoff (call) = max(S_T - K, 0)

### Black-Scholes Formula

Used as a benchmark for validation:

```
C = S_0 N(d1) - K e^{-rT} N(d2)
```

---

## Example Parameters

```python
S0 = 100              # Spot price
K = 100               # Strike price
r = 0.03              # Risk-free rate
sigma = 0.25          # Volatility
T = 1.0               # Time to maturity years
steps = 252           # Time steps for GBM
paths = 20            # Number of MC paths
option_type = "call"  # "call" or "put"
```

---

## Output

The script produces:

1. **GBM Paths**
   Simulated trajectories of the underlying asset

2. **Monte Carlo Convergence**
   Shows how the estimate approaches the Black-Scholes price

3. **Payoff Distribution**
   Histogram of simulated option payoffs

Console output:

```
Monte Carlo Price (call): 10.32
Black-Scholes Price (call): 10.45
Difference: 0.13
```

---

## Key Insights

* Monte Carlo estimates converge to the analytical price as the number of simulations increases
* The convergence illustrates the **Law of Large Numbers**
* Simulation-based methods are flexible and extendable to more complex derivatives

---

## Future

* Add confidence intervals to Monte Carlo estimates
* Support American options (e.g., Longstaff-Schwartz method)
* Introduce variance reduction techniques:

  * Antithetic variates
  * Control variates
* Add interactive UI (e.g., Streamlit)
* Parallelize simulations for performance

