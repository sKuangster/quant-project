
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
    return V1_up, V1_down

def exercise_3():
    print("Exercise 3: ")
    S0 = 100
    u = 1.2
    d = 0.8
    k = 50
    S1_up = u * S0
    S1_down = d * S0
    r = 0.05
    X0 = 40
    V1_up = european_option.payoff(S1_up, k)
    V1_down = european_option.payoff(S1_down, k)
    residuals1 = binomial_model.replication_residuals(S0, S1_up, S1_down, r, 0, X0, V1_up, V1_down)
    residuals2 = binomial_model.replication_residuals(S0, S1_up, S1_down, r, 1, X0, V1_up, V1_down)
    residuals3 = binomial_model.replication_residuals(S0, S1_up, S1_down, r, -1, X0, V1_up, V1_down)
    print(residuals1)
    print(residuals2)
    print(residuals3)
    print("Average: " + str(sum(residuals1)/2))
    print("Average: " + str(sum(residuals2)/2))
    print("Average: " + str(sum(residuals3)/2))
    print("Difference: " + str(residuals1[0]-residuals1[1]))
    print("Difference: " + str(residuals2[0]-residuals2[1]))
    print("Difference: " + str(residuals3[0]-residuals3[1]))
    

def main():
    exercise_1()
    exercise_2()
    exercise_3()
main()