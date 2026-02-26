import sqlite3

connect = sqlite3.connect("soccer.db")
cursor = connect.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS teams(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR(50) NOT NULL
    )
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS players(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR(50) NOT NULL,
        position VARCHAR(20) NOT NULL,
        goals INTEGER NOT NULL,
        team_id INTEGER NOT NULL,
        FOREIGN KEY (team_id) REFERENCES teams(id)
    )
""")

connect.commit()


def create_team(name):
    cursor.execute(f'INSERT INTO teams (name) VALUES ("{name}")')
    connect.commit()
    print("Team added")

def create_player(name, position, goals, team_id):
    cursor.execute(
        f'INSERT INTO players (name, position, goals, team_id) '
        f'VALUES ("{name}", "{position}", {goals}, {team_id})'
    )
    connect.commit()
    print("Player added")

def get_teams_and_players():
    cursor.execute("""
        SELECT teams.name, players.name, players.position, players.goals
        FROM teams
        INNER JOIN players ON teams.id = players.team_id
    """)
    data = cursor.fetchall()
    for i in data:
        print(f"Team: {i[0]} | Player: {i[1]} | Pos: {i[2]} | Goals: {i[3]}")


#def add_test_data():
    #create_team("Barcelona")
    #create_team("Real Madrid")
    #create_team("Manchester City")

    #create_player("Lewandowski", "ST", 18, 1)
    #create_player("Pedri", "CM", 4, 1)

    #create_player("Bellingham", "CM", 16, 2)
    #create_player("Vinicius", "LW", 10, 2)

    #create_player("Haaland", "ST", 20, 3)
    #create_player("De Bruyne", "CM", 6, 3)

#add_test_data() 

def create_view():
    cursor.execute("""
        CREATE VIEW IF NOT EXISTS top_scorers AS
        SELECT teams.name AS team, players.name AS player, players.goals
        FROM teams
        INNER JOIN players ON teams.id = players.team_id
        WHERE players.goals >= 15
    """)
    connect.commit()
    print("View created")

def get_view():
    cursor.execute("SELECT * FROM top_scorers")
    data = cursor.fetchall()
    print(data)


get_teams_and_players()
create_view()
get_view()