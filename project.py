import numpy as np
import pandas as pd

class Player:
    def __init__(self, name, role, batting_avg, strike_rate, economy):
        self.name = name
        self.role = role
        self.batting_avg = batting_avg
        self.strike_rate = strike_rate
        self.economy = economy
    
    def get_batting_performance(self):
        return np.random.poisson(self.batting_avg)
    
    def get_bowling_performance(self):
        return np.random.poisson(self.economy)

class Team:
    def __init__(self, name, players):
        self.name = name
        self.players = players
    
    def get_team_performance(self):
        batting_scores = [player.get_batting_performance() for player in self.players if player.role in ['Batsman', 'All-Rounder']]
        bowling_performance = [player.get_bowling_performance() for player in self.players if player.role in ['Bowler', 'All-Rounder']]
        return sum(batting_scores), sum(bowling_performance)

class Match:
    def __init__(self, team1, team2):
        self.team1 = team1
        self.team2 = team2
    
    def simulate_match(self):
        score1, wickets1 = self.team1.get_team_performance()
        score2, wickets2 = self.team2.get_team_performance()
        
        print(f"{self.team1.name}: {score1}/{wickets1} in 20 overs")
        print(f"{self.team2.name}: {score2}/{wickets2} in 20 overs")
        
        if score1 > score2:
            print(f"{self.team1.name} wins!")
        elif score2 > score1:
            print(f"{self.team2.name} wins!")
        else:
            print("Match Drawn!")

mi_players = [
    Player("Rohit Sharma", "Batsman", 40, 130, 0),
    Player("Tilak Verma", "Batsman", 35, 125, 0),
    Player("Suryakumar Yadav", "Batsman", 38, 140, 0),
    Player("Hardik Pandya", "All-Rounder", 30, 145, 8),
    Player("Jasprit Bumrah", "Bowler", 10, 80, 6)
]

csk_players = [
    Player("MS Dhoni", "Batsman", 37, 135, 0),
    Player("Ruturaj Gaikwad", "Batsman", 36, 125, 0),
    Player("Shivam Dube", "All-Rounder", 32, 140, 7),
    Player("Ravindra Jadeja", "All-Rounder", 28, 120, 6),
    Player("khaleel Ahemad", "Bowler", 12, 70, 7)
]

mi = Team("Mumbai Indians", mi_players)
csk = Team("Chennai Super Kings", csk_players)

match = Match(mi, csk)
match.simulate_match()

data = {
    "Player": [p.name for p in mi_players + csk_players],
    "Team": ["MI"] * len(mi_players) + ["CSK"] * len(csk_players),
    "Batting Average": [p.batting_avg for p in mi_players + csk_players],
    "Strike Rate": [p.strike_rate for p in mi_players + csk_players],
    "Economy Rate": [p.economy for p in mi_players + csk_players]
}
df = pd.DataFrame(data)
print(df)
