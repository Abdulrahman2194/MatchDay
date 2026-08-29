import sys


Match = sys.argv[2]
score = sys.argv[3]
goals=score.split("-")
goals_for = int(goals[0])
goals_against = int(goals[1])
if goals_for > goals_against:
    result = "Win"
elif goals_for == goals_against:
    result = "Draw"
else:
    result = "Lose"
    
print(f"Match : {Match} |  Score : {score} | Result : {result}")