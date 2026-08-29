import sys
import json


match = sys.argv[2]
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
    
print(f"match : {match} |  score : {score} | result : {result}")

try:
    with open("matches.json", "r") as f:
        matches = json.load(f)
except FileNotFoundError:
    matches = []



new_match = {"match" : match, "score" : score, "result" : result}
matches.append(new_match)


with open("matches.json","w") as f:
    json.dump(matches, f, indent=2)

print(matches)