#!/usr/bin/env python

from enum import Enum

# Trying to learn about enums and fiddling with char ordinality
# This is not how I would code this if this were my job, b/c this is all way too cute
# Like clearly the path of least resistance is a bunch of dicts
class RPS(Enum):
    ROCK = 0
    PAPER = 1
    SCISSOR = 2

    @classmethod
    def lookup_opponent(cls, input: str):
        return list(cls)[ord(input) - 65]

    @classmethod
    def lookup_self(cls, input: str):
        return list(cls)[ord(input) - 88]

class Outcome(Enum):
    # Values are tethered to how enum indexing works, woooo
    LOSE = -1
    DRAW = 0
    WIN = 1

    @classmethod
    def lookup_outcome(cls, input: str):
        return list(cls)[ord(input) - 88]

def calculate_score(my_in: RPS, opponent_in: RPS) -> int:
    score: int = 0
    if opponent_in is list(RPS)[my_in.value - 1]: # The choice to the left loses to us
        score += 6
    elif my_in is opponent_in: # Handle ties; don't need to handle loses.
        score += 3
    return score + my_in.value + 1 # Enum helps score!

def get_choice_for_outcome(outcome: Outcome, opponent_in: RPS) -> RPS:
    ix = opponent_in.value + outcome.value 
    if ix >= len(list(RPS)): # Handling overflow, is there a cuter way to do this?
        ix -= len(list(RPS))
    return list(RPS)[ix] 

# 1st star
with open('day2/input', 'r') as f:
    total_score: int = 0
    for line in f.readlines():
        choices = [choice.strip() for choice in line.split(" ")]
        total_score += calculate_score(RPS.lookup_self(choices[1]), RPS.lookup_opponent(choices[0]))
    print(total_score)


# 2nd star
with open('day2/input', 'r') as f:
    total_score: int = 0
    for line in f.readlines():
        ins = [choice.strip() for choice in line.split(" ")]
        opponent_choice = RPS.lookup_opponent(ins[0])
        my_choice = get_choice_for_outcome(Outcome.lookup_outcome(ins[1]), opponent_choice)
        total_score += calculate_score(my_choice, opponent_choice)
    print(total_score)
    