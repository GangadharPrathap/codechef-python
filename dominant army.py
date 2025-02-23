def is_dominant_army(T, test_cases):
    results = []
    for NA, NB, NC in test_cases:
        # Check if any army is dominant
        if NA > (NB + NC) or NB > (NA + NC) or NC > (NA + NB):
            results.append("YES")
        else:
            results.append("NO")
    
    return results

# Reading input
T = int(input())  # Number of test cases
test_cases = [tuple(map(int, input().split())) for _ in range(T)]  # Read T test cases

# Computing results and printing them
for result in is_dominant_army(T, test_cases):
    print(result)
