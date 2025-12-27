
"""
S0: price of stock at T = 0
S1: price of stock at T = 1
r: interest rate
delta: how many longs/shorts, delta=0 means none
X0: initial wealth
"""
def one_period_wealth(S0, S1, r, delta, X0):
    return delta*S1+(1+r)*(X0-delta*S0)

def is_arbitrage(x1_up, x1_down):
    return (
        x1_up >= 0 and
        x1_down >= 0 and
        (x1_up > 0 or x1_down > 0)
    )

def replication_residuals(S0, S1_up, S1_down, r, delta, X0, V1_up, V1_down):
    """
    Returns (residual_up, residual_down) where each residual is:
    portfolio_wealth_at_time1 - derivative_payoff
    """
    X1_up = one_period_wealth(S0, S1_up, r, delta, X0)
    X1_down = one_period_wealth(S0, S1_down, r, delta, X0)
    return (X1_up-V1_up, X1_down-V1_down)
    