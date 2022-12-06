#!/usr/bin/env python

# 1st star
with open('day1/input', 'r') as f:
    max: int = 0
    curr_sum: int = 0
    
    for line in f.readlines():
        if line.isspace():
            max = curr_sum if curr_sum > max else max
            curr_sum = 0
            continue
        curr_sum += int(line) # Would error handle but I control input.
    
    print(max)

# 2nd star - it's probably fastest to just make three variables, but cleanest code-wise to sum, make a list of results, sort, and slice top 3.
with open('day1/input', 'r') as f:
    sums: list[int] = []
    curr_sum: int = 0
    for line in f.readlines():
        if line.isspace():
            sums.append(curr_sum)
            curr_sum = 0
            continue
        curr_sum += int(line)

    print(sum(sorted(sums, reverse = True)[:3]))
