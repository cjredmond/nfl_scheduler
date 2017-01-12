

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

    def non_bye_options(self,ls):
        total = 0
        for game in self.total_schedule(ls):
            total += game.matching_weeks_non_bye(ls)
        return total

    def bye_options(self,ls):
        total = 0
        for game in self.total_schedule(ls):
            total += game.matching_weeks(ls)
        return total

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name

    def __repr__(self):
        return self.name


class Game:
    def __init__(self,week,home,away):
        self.week = week
        self.home = home
        self.away = away
        self.london = False

    def __str__(self):
        return str(self.week) + self.home.name + self.away.name

    def __unicode__(self):
        return str(self.week) + self.home.name + self.away.name

    def __repr__(self):
        return str(self.week) + str(self.home.name)+ str(self.away.name)

    def matching_weeks_non_bye(self,ls):
        weeks = [1,2,3,12,14,15,16,17]
        for game in self.home.total_schedule(ls):
            if game.week != 0:
                weeks.remove(game.week)
        for game in self.away.total_schedule(ls):
            if game.week != 0:
                if game.week in weeks:
                    weeks.remove(game.week)
        return len(weeks)

    def matching_weeks(self, ls):
        weeks = [4,5,6,7,8,9,10,11,13]
        for game in self.home.total_schedule(ls):
            if game.week in weeks:
                weeks.remove(game.week)
        for game in self.away.total_schedule(ls):
            if game.week in weeks:
                if game in weeks:
                    weeks.remove(game.week)
        return len(weeks)

    def delete_target(self,ls):
        return self.home.non_bye_options(ls) + self.away.non_bye_options(ls)

    def bye_delete_target(self,ls):
        return self.home.bye_options(ls) + self.away.bye_options(ls)

    def new_matching_weeks(self,ls):
        weeks = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17]
        for game in self.home.total_schedule(ls):
            if game.week in weeks:
                weeks.remove(game.week)
        for game in self.away.total_schedule(ls):
            if game.week in weeks:
                weeks.remove(game.week)
        return len(weeks)

    def new_delete_target(self,ls):
        return self.home.bye_options(ls) + self.away.bye_options(ls)
