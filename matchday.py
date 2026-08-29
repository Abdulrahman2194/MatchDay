import json
import sys

command = sys.argv[1]

if command == "add":
    match = sys.argv[2]
    score = sys.argv[3]
    goals = score.split("-")
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
        with open("matches_backup.json", "r") as f:
            matches = json.load(f)
    except FileNotFoundError:
        matches = []

    new_match = {"match": match, "score": score, "result": result}
    matches.append(new_match)

    with open("matches_backup.json", "w") as f:
        json.dump(matches, f, indent=2)

    print(matches)

elif command == "season":
    try:
        with open("matches_backup.json", "r") as f:
            matches = json.load(f)
    except FileNotFoundError:
        matches = []
        
        

    wins = 0
    draws = 0
    losses = 0
    goals_for = 0
    goals_against = 0
    for match in matches:
        if match["result"] == "Win":
            wins += 1
        elif match["result"] == "Draw":
            draws += 1
        else:
            losses += 1
        score = match["score"]
        goals = score.split("-")
        goals_for += int(goals[0])
        goals_against += int(goals[1])

    
            
    
    played=len(matches)
    print(f"Played: {played} | W: {wins} D: {draws} L: {losses} | Goals For: {goals_for} Goals Against: {goals_against}")
    
            