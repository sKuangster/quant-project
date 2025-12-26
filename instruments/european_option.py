def payoff(S1, K):
    # have the option to buy S1 or not @ time 1
    # should only buy if S1 > K, else don't buy it
    return max(0, S1-K) # returns V1, payoff @ t1 from buying the option at strike price K