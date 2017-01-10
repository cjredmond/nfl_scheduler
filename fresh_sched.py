from fresh_teams_class import Team, Game
import csv
import random

teams = []
games = []
finished_games = []

def find_team(name):
    for x in teams:
        if x.name == name:
            return x

def already_playing(home,away):
    for game in games:
        if game.week == 0:
            pass
        elif game.home == home and game.away == away:
            return True
        return False

def game_searcher(home,away):
    for game in games:
        if game.home == home and game.away == away:
            return game

def weekly_sched(week):
    sched = []
    for game in games:
        if game.week == week:
            sched.append([game.week,game.home.name,game.away.name])
    return sched

def possible_teams_week(week,ls):
    not_available = []
    for game in games:
        if game.week == week:
            not_available.append(game.home)
            not_available.append(game.away)
    return not_available

with open('teams.csv') as infile:
        reader = csv.reader(infile)
        for row in reader:
            teams.append(Team(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],
                              row[8],row[9],row[10],row[11]))

def create_blank_games(team):
        div_opponents = team.div_opponents(teams)
        for opp in div_opponents:
            games.append(Game(0,team,opp))
        games.append(Game(0,team,find_team(team.conf_div_home_1)))
        games.append(Game(0,team,find_team(team.conf_div_home_2)))
        games.append(Game(0,team,find_team(team.out_conf_home_1)))
        games.append(Game(0,team,find_team(team.out_conf_home_2)))
        games.append(Game(0,team,find_team(team.rank_home)))

for team in teams:
    create_blank_games(team)

def week_17():
    for _ in range(1,17):
        home = random.choice(teams)
        while home.do_they_play_this_week(17,games):
            home = random.choice(teams)
        opponents = []
        for x in teams:
            if x.name != home.name and x.div == home.div:
                opponents.append(x)
        away = random.choice(opponents)
        while away.do_they_play_this_week(17,games):
            away = random.choice(opponents)
        x = game_searcher(home,away)
        x.week = 17
week_17()

for game in games:
    if game.week != 0:
        finished_games.append(game)

def scheduler(team):
    bye_weeks = [4,5,6,7,8,9,10,11,13]
    non_byes = [1,2,3,12,14,15,16,17]
    for week in team.weeks_already_played(games):
        if week in bye_weeks:
            bye_weeks.remove(week)
        if week in non_byes:
            non_byes.remove(week)
    if len(bye_weeks) + len(non_byes) > 1:
        coinflip = random.random()
    if coinflip > .5:
        pass
    else:
        pass




scheduler(find_team('Packers'))
