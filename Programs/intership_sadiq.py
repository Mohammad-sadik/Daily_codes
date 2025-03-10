from itertools import permutations
pools = {
    'A': ['France', 'Italy', 'Namibia', 'New Zealand', 'Uruguay'],
    'B': ['Ireland', 'Scotland', 'South Africa', 'Romania', 'Tonga'],
    'C': ['Australia', 'Fiji', 'Georgia', 'Portugal', 'Wales'],
    'D': ['Argentina', 'Chile', 'England', 'Japan', 'Samoa']}
wr_top_10 = {
    'Ireland': 1,
    'South Africa': 2,
    'France': 3,
    'New Zealand': 4,
    'Scotland': 5,
    'Argentina': 6,
    'Fiji': 7,
    'England': 8,
    'Australia': 9,
    'Wales': 10
}
prob_order_maintain = 0.6

def calculate_pool_probability(pool, top_teams):
    permutations_list = list(permutations(top_teams))
    total_permutations = len(permutations_list)
    equal_prob = (1 - prob_order_maintain) / (total_permutations - 1)
    prob_dict = {perm: equal_prob for perm in permutations_list}
    prob_dict[top_teams] = prob_order_maintain
    return prob_dict

pool_probabilities = {}
for pool_name, teams in pools.items():
    top_teams = tuple(sorted([team for team in teams if team in wr_top_10], key=lambda x: wr_top_10[x]))
    pool_probabilities[pool_name] = calculate_pool_probability(pool_name, top_teams)

def calculate_matchup_probability():
    matchup_prob = 0
    for pool_A, prob_A in pool_probabilities['A'].items():
        for pool_B, prob_B in pool_probabilities['B'].items():
            for pool_C, prob_C in pool_probabilities['C'].items():
                for pool_D, prob_D in pool_probabilities['D'].items():
                    nz_vs_ireland = ((pool_A[0] == 'New Zealand' and pool_B[1] == 'Ireland') or 
                                     (pool_A[1] == 'New Zealand' and pool_B[0] == 'Ireland'))
                    fra_vs_sa = ((pool_A[0] == 'France' and pool_B[1] == 'South Africa') or 
                                 (pool_A[1] == 'France' and pool_B[0] == 'South Africa'))
                    if nz_vs_ireland and fra_vs_sa:
                        matchup_prob += prob_A * prob_B * prob_C * prob_D
    return matchup_prob

probability = calculate_matchup_probability()
print(f"The probability of the specific quarter-final matchups (New Zealand vs Ireland, and France vs South Africa) is: {probability:.4f}")
