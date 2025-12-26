
from market import binomial_model
from instruments import european_option
def exercise_1():
    print("Exercise 1: ")
    S0 = 100
    u = 1.2
    d = 0.8
    r = 0.05
    X0 = 0

    s1_up = u*S0
    s1_down = d*S0

    x1_H_delta_0 = binomial_model.one_period_wealth(S0, s1_up, r, 0, X0)
    x1_L_delta_0 = binomial_model.one_period_wealth(S0, s1_down, r, 0, X0)
    x1_H_delta_pos = binomial_model.one_period_wealth(S0, s1_up, r, 1, X0)
    x1_L_delta_pos = binomial_model.one_period_wealth(S0, s1_down, r, 1, X0)
    x1_H_delta_neg = binomial_model.one_period_wealth(S0, s1_up, r, -1, X0)
    x1_L_delta_neg = binomial_model.one_period_wealth(S0, s1_down, r, -1, X0)

    print(x1_H_delta_0)
    print(x1_L_delta_0)
    print(x1_H_delta_pos)
    print(x1_L_delta_pos)
    print(x1_H_delta_neg)
    print(x1_L_delta_neg)

def exercise_2():
    print("Exercise 2: ")
    S0 = 100
    u = 1.2
    d = 0.8
    k = 50
    S1_up = u * S0
    S1_down = d * S0
    V1_up = european_option.payoff(S1_up, k)
    V1_down = european_option.payoff(S1_down, k)

    print(V1_up, V1_down)


def main():
    exercise_1()
    exercise_2()

main()