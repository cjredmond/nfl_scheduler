class Team:
    def __init__(self,name,div,conf_div_home_1,conf_div_home_2,conf_div_away_1,conf_div_away_2,
           out_conf_home_1,out_conf_home_2,out_conf_away_1,out_conf_away_2,rank_home,rank_away):
           self.name = name
           self.div = div
           self.conf_div_home_1 = conf_div_home_1
           self.conf_div_home_2 = conf_div_home_2
           self.conf_div_away_1 = conf_div_away_1
           self.conf_div_away_2 = conf_div_away_2
           self.out_conf_home_1 = out_conf_home_1
           self.out_conf_home_2 = out_conf_home_2
           self.out_conf_away_1 = out_conf_away_1
           self.out_conf_away_2 = out_conf_away_2
           self.rank_home = rank_home
           self.rank_away = rank_away

    def do_they_play_this_week(self, week, ls):
        if [x for x in ls if x.week == week and x.home == self] or [x for x in ls if x.week == week and x.away == self]:
            return True
        return False

    def div_opponents(self,ls):
        opponents = []
        for team in ls:
            if team.name != self.name and team.div == self.div:
                opponents.append(team)
        return opponents

    def possible_away_opponents(self,week,ls):
        opponents = []
        for game in ls:
            if game.home == self:
                if not game.away.do_they_play_this_week(week,ls) and game.week == 0:
                    opponents.append(game.away)
        return opponents

    def weeks_already_played(self,ls):
        weeks = []
        for game in ls:
            if game.home == self or game.away == self:
                weeks.append(game.week)
        return weeks

    def games_available(self,ls):
        games = []
        for game in ls:
            if game.home == self or game.away == self:
                if game.week == 0:
                    games.append(game)
        return games

    def total_schedule(self,ls):
        sched = []
        for game in ls:
            if game.home == self or game.away == self:
                sched.append(game)
        return sched

class Game:
    def __init__(self,week,home,away):
        self.week = week
        self.home = home
        self.away = away

    def __str__(self):
        return str(self.week) + self.home.name + self.away.name

    def __unicode__(self):
        return str(self.week) + self.home.name + self.away.name

    def __repr__(self):
        return str(self.week) + str(self.home.name)+ str(self.away.name)
