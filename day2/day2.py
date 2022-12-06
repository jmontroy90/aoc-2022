#!/usr/bin/env python

from enum import Enum

# Trying to learn about enums and fiddling with char ordinality
# This is not how I would code this if this were my job, b/c this is all way too cute
# Like clearly the path of least resistance is a bunch of dicts
class Outcome(Enum):
    # Values are tethered to how enum indexing works, woooo
    LOSE = -1
    DRAW = 0
    WIN = 1

    @classmethod
    def lookup_outcome(cls, input: str):
        return list(cls)[ord(input) - 88]

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

    def score(self, opponent_in: 'RPS') -> int:
        score: int = 0
        if opponent_in is list(RPS)[self.value - 1]: # The choice to the left loses to us
            score += 6
        elif self is opponent_in: # Handle ties; don't need to handle loses.
            score += 3
        return score + self.value + 1 # Enum helps score!

    def choose_for_outcome(self, outcome: Outcome) -> 'RPS':
        ix = self.value + outcome.value 
        if ix >= len(list(RPS)): # Handling overflow, is there a cuter way to do this?
            ix -= len(list(RPS))
        return list(RPS)[ix] 

# 1st star
with open('day2/input', 'r') as f:
    total_score: int = 0
    for line in f.readlines():
        choices = [choice.strip() for choice in line.split(" ")]
        total_score += RPS.lookup_self(choices[1]).score(RPS.lookup_opponent(choices[0]))
    print(total_score)


# 2nd star
with open('day2/input', 'r') as f:
    total_score: int = 0
    for line in f.readlines():
        ins = [choice.strip() for choice in line.split(" ")]
        opponent_choice = RPS.lookup_opponent(ins[0])
        my_choice = opponent_choice.choose_for_outcome(Outcome.lookup_outcome(ins[1]))
        total_score += my_choice.score(opponent_choice)
    print(total_score)
    