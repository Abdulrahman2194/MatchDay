# MatchDay
A command-line tool for tracking a football team's season — record match results and view your record and recent form.
## Features

- Add Feature:saves opponent/score/result
- Season Feature:it calculates and displays totals from what's saved
- Form Feature:Displays recent form: the outcomes of your last 5 matches at a glance

## Requirements

Python 3
No External Packages

## Setup
Clone Command:git clone https://github.com/Abdulrahman2194/MatchDay.git
cd Command:cd MatchDay
Venv Creation:py -m venv venv
Venv Activation:venv\Scripts\activate

## Usage
python matchday.py add "vs Ismaily" 3-0
Result: match : vs Ismaily |  score : 3-0 | result : Win

python matchday.py season
Result: Played: 8 | W: 6 D: 1 L: 1 | Goals For: 19 Goals Against: 10

python matchday.py form
Result: W W W W W


## Data
Matches are stored in a matches.json file in the project folder. 
The file is created automatically the first time a match is added.