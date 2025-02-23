'''
Alice has a bucket of water initially having W litres of water in it. The maximum capacity of the bucket is X liters.
Alice turned on the tap and the water starts flowing into the bucket at a rate of Y litres/hour. She left the tap running for exactly Z hours. Determine whether the bucket has been overflown, filled exactly, or is still left unfilled.'''
def bucket_state(T, test_cases):
    results = []
    for W, X, Y, Z in test_cases:
        total_water = W + (Y * Z)  # Calculate total water after inflow
        if total_water > X:
            results.append("overflow")
        elif total_water == X:
            results.append("filled")
        else:
            results.append("unfilled")
    return results
T = int(input())  # Number of test cases
test_cases = [tuple(map(int, input().split())) for _ in range(T)]  # Read T test cases
for result in bucket_state(T, test_cases):
    print(result)
