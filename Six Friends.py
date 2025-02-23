'''
Six friends go on a trip and are looking for accommodation. After looking for hours, they find a hotel which offers two types of rooms — double rooms and triple rooms. A double room costs Rs. 
X, while a triple room costs Rs. Y.The friends can either get three double rooms or get two triple rooms. Find the minimum amount they will have to pay to accommodate all six of them.
'''def min_accommodation_cost(T, test_cases):
    results = []
    for X, Y in test_cases:
        cost_double = 3 * X  
        cost_triple = 2 * Y 
        if cost_double < cost_triple:
            results.append(cost_double)
        else:
            results.append(cost_triple)
    
    return results
T = int(input())  # Number of test cases
test_cases = [tuple(map(int, input().split())) for _ in range(T)]
for result in min_accommodation_cost(T, test_cases):
    print(result)
