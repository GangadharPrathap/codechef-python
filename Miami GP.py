'''
Chef has finally got the chance of his lifetime to drive in the 
F1 tournament. But, there is one problem. Chef did not know about the 107% rule and now he is worried whether he will be allowed to race in the main event or not.
Given the fastest finish time as X seconds and Chef's finish time as Y seconds, determine whether Chef will be allowed to race in the main event or not.
Note that, Chef will only be allowed to race if his finish time is within 107% of the fastest finish time.
'''# cook your dish here
def will_chef_race(T, test_cases):
    results = []
    for X, Y in test_cases:
        max_allowed_time = X * 1.07  # Calculate 107% of the fastest time
        
        # Determine if Chef qualifies
        if Y <= max_allowed_time:
            results.append("YES")
        else:
            results.append("NO")
    
    return results
T = int(input())  
test_cases = [tuple(map(int, input().split())) for _ in range(T)] 
for result in will_chef_race(T, test_cases):
    print(result)
