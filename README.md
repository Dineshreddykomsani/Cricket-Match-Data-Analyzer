# Cricket Match Data Analyzer

This is a simple Python program that simulates a cricket match between two teams: Mumbai Indians (MI) and Chennai Super Kings (CSK). The program uses NumPy and Pandas to generate and analyze match data.

 Features:
* Simulates a match between two teams based on player statistics.
* Uses Poisson distribution to estimate batting and bowling performance.
* Displays the match score and announces the winner.
* Creates a Pandas DataFrame containing player statistics.

Requirements:
This project requires the following Python libraries:
*`numpy`
*`pandas`

You can install them using:
```bash
pip install numpy pandas
```

 How It Works
1. Player Class : Represents a player with attributes like batting average, strike rate, and economy.
2. Team Class: Represents a team with a list of players.
3. Match Class : Simulates a match between two teams and determines the winner.
4. DataFrame : Stores player statistics in a tabular format using Pandas.

 Usage:
Run the program using Python:
```bash
python cricket_match.py
```
It will display:
* The match score for both teams.
* The winner of the match.
* A table with player statistics.

 Example Output:
```
Mumbai Indians: 120/12 in 20 overs
Chennai Super Kings: 115/11 in 20 overs
Mumbai Indians wins!

         Player  Team  Batting Average  Strike Rate  Economy Rate
0  Rohit Sharma    MI               40         130             0
1   Tilak Verma    MI               35         125             0
...
```

 Contribution:
Feel free to improve this project by adding features like:
* More realistic performance calculations
* Additional teams and players
* Graphical representation of match statistics

 License:
This project is open-source and free to use.

