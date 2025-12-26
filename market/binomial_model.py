"""
S0: price of stock at T = 0
S1: price of stock at T = 1
r: interest rate
delta: how many longs/shorts, delta=0 means none
X0: initial wealth
"""
def one_period_wealth(S0, S1, r, delta, X0):
    return delta*S1+(1+r)*(X0-delta*S0)

S0 = 100
u = 1.2
d = 0.8
r = 0.05
X0 = 0

s1_up = u*S0
s1_down = d*S0

x1_H_delta_0 = one_period_wealth(S0, s1_up, r, 0, X0)
x1_L_delta_0 = one_period_wealth(S0, s1_down, r, 0, X0)
x1_H_delta_pos = one_period_wealth(S0, s1_up, r, 1, X0)
x1_L_delta_pos = one_period_wealth(S0, s1_down, r, 1, X0)
x1_H_delta_neg = one_period_wealth(S0, s1_up, r, -1, X0)
x1_L_delta_neg = one_period_wealth(S0, s1_down, r, -1, X0)

print(x1_H_delta_0)
print(x1_L_delta_0)
print(x1_H_delta_pos)
print(x1_L_delta_pos)
print(x1_H_delta_neg)
print(x1_L_delta_neg)