import json
import sys


if len(sys.argv) < 2:
    print("Should be python matchday.py [add|season|form] ")
    sys.exit(1)

command = sys.argv[1]

if command == "add":
    
    if len(sys.argv) < 4:
        print("input should be like this : python matchday.py add match score")
        sys.exit(1)

    match = sys.argv[2]
    score = sys.argv[3]
    try:
        goals = score.split("-")
        if len(goals) == 2:
            goals_for = int(goals[0])
            goals_against = int(goals[1])
        else:
            raise ValueError
    except (ValueError, IndexError):
        print("Score should be in the format 'X-Y' where X and Y are integers.")
        sys.exit(1)
    

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

    new_match = {"match": match, "score": score, "result": result}
    matches.append(new_match)

    with open("matches.json", "w") as f:
        json.dump(matches, f, indent=2)

  

elif command == "season":
    try:
        with open("matches.json", "r") as f:
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

    played = len(matches)
    print(
        f"Played: {played} | W: {wins} D: {draws} L: {losses} | Goals For:"
        f" {goals_for} Goals Against: {goals_against}"
    )

elif command == "form":
    try:
        with open("matches.json","r") as f:
            matches=json.load(f)
    except FileNotFoundError:
        matches = []

    
    form = matches[-5:]
    form_list = []
    for match in form:
        if match["result"] == "Win":
            form_list.append("W")
        elif match["result"] == "Draw":
            form_list.append("D")
        elif match["result"] == "Lose":
            form_list.append("L")
    print(" ".join(form_list))
else:
    print("Unknown command. Use 'add', 'season', or 'form'.")
    sys.exit(1)

