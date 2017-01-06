from team_class import Team, Game
import csv
import random

teams = []
games = []

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

############################################################################################
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


# with open('blank.csv') as infile:
#     reader = csv.reader(infile)
#     for row in reader:
#         x.append(Game(row[0],row[1],row[2]))



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

def non_bye_weeks(team):
    print(team.name,team.non_bye_options(games))
    weeks = [1,2,3,12,14,15,16]
    for week in team.weeks_already_played(games):
        if week in weeks:
            weeks.remove(week)
    if len(weeks) > 0:
        rand_week = random.choice(weeks)
        weeks.remove(rand_week)
        avl_games = team.games_available(games)
        choice = random.choice(avl_games)
        frozen = 0
        while choice.home.do_they_play_this_week(rand_week,games) or choice.away.do_they_play_this_week(rand_week,games):
            choice = random.choice(avl_games)
            frozen += 1
            if frozen == 50:
                freeze_stopper(team)
                return 'ehh'
        choice.week = rand_week
        #print(choice.week,choice.home.name,choice.away.name)
        amount.append(choice)
        print(len(amount))
    else:
        return freeze_stopper(team)

def freeze_stopper(team):
    choices = [game for game in games if game.home == team or game.away == team]
    for game in choices:
        if game.week == 0 or game.week == 17:
            choices.remove(game)
    choices = sorted(choices, key= lambda t: -t.delete_target(games))
    choices = choices[:2]
    print(choices)
    x = random.choice(amount)
    print(x)
    choices.append(x)
    for game in choices:
        if game.week == 17:
            pass
        else:
            if game in amount:
                amount.remove(game)
            game.week = 0

# print(possible_teams_week(1,teams))
x = find_team('Packers')


# with open('correct_non_bye_weeks.csv') as infile:
#     reader = csv.reader(infile)
#     for row in reader:
#         amount.append(Game(int(row[0]),find_team(row[1]),find_team(row[2])))

def bye_weeks(team):
    print(team.name)
    weeks = [4,5,6,7,8,9,10,11,13]
    for week in team.weeks_already_played(games):
        if week in weeks:
            weeks.remove(week)
    if len(weeks) > 1:
        rand_week = random.choice(weeks)
        weeks.remove(rand_week)
        avl_games = team.games_available(games)
        choice = random.choice(avl_games)
        frozen = 0
        while choice.home.do_they_play_this_week(rand_week,games) or choice.away.do_they_play_this_week(rand_week,games):
            choice = random.choice(avl_games)
            frozen += 1
            if frozen == 50:
                bye_freeze_stopper(team)
                return 'ehh'
        choice.week = rand_week
        #print(choice.week,choice.home.name,choice.away.name)
        amount.append(choice)
        print(len(amount))
    else:
        return bye_freeze_stopper(team)

def bye_freeze_stopper(team):
    choices = [game for game in games if game.home == team or game.away == team]
    new_choices = []
    for game in choices:
        non_bye_weeks = [0,1,2,3,12,14,15,16,17]
        if not int(game.week) in non_bye_weeks:
            new_choices.append(game)
    choices = sorted(new_choices, key= lambda t: -t.bye_delete_target(games))
    choices = choices[:2]
    x = random.choice(amount)
    while x.week in non_bye_weeks:
        x = random.choice(amount)
    choices.append(x)
    for game in choices:
        if game in amount:
            amount.remove(game)
        game.week = 0

amount = []
for game in games:
    if game.week != 0:
        amount.append(game)

while len(amount) < 100:
    team = random.choice(teams)
    non_bye_weeks(team)

while len(amount) < 128:
    team = sorted(teams, key= lambda t: -t.non_bye_options(games))[0]
    non_bye_weeks(team)
    if len(amount) > 115:
        new_amount = sorted(amount, key = lambda t: t.week)
        a = open('blank_game_output.csv', 'w')
        b = csv.writer(a)
        for y in new_amount:
            a.write(str(y.week) + "," + y.home.name + "," + y.away.name+ "\n")

while len(amount) < 200:
    team = random.choice(teams)
    bye_weeks(team)

while len(amount) < 256:
    team = sorted(teams, key= lambda t: -t.bye_options(games))[0]
    bye_weeks(team)
    if len(amount) > 220:
        new_amount = sorted(amount, key = lambda t: t.week)
        a = open('blank_game_output.csv', 'w')
        b = csv.writer(a)
        for y in new_amount:
            a.write(str(y.week) + "," + y.home.name + "," + y.away.name+ "\n")
