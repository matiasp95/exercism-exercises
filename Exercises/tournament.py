import pprint


def tally(rows):
    teams = gen_teams(rows)
    s_teams = sorted(sorted(teams,key=lambda x: x.name), key=lambda x: x.points, reverse=True)
    team_width = 30
    ret = ["Team                           | MP |  W |  D |  L |  P"]
    for team in s_teams:
        ret.append("{:<{team_width}} |  {mp} |  {w} |  {d} |  {l} | {p:{p_width}}".format(team.name,
                                                                                    team_width=team_width,
                                                                                    mp=team.matches_played,
                                                                                    w=team.wins, d=team.draws,
                                                                                    l=team.losses,
                                                                                    p=team.points,
                                                                                    p_width=2 if team.points < 10 else 2))
    return ret 
def gen_teams(rows):
    teams = []
    for i in rows:
        x = i.split(";")
        t1 = Team(x[0])
        t2 = Team(x[1])
        if t1 not in teams:
            teams.append(t1)
        if t2 not in teams:
            teams.append(t2)
        if x[2] == "win":
            for team in teams:
                if team.name == x[0]:
                    team.wins += 1
                    team.points += 3
                    team.matches_played += 1
                if team.name == x[1]:
                    team.losses += 1
                    team.matches_played += 1
        if x[2] == "loss":
            for team in teams:
                if team.name == x[0]:
                    team.losses += 1
                    team.matches_played += 1
                if team.name == x[1]:
                    team.wins += 1
                    team.points += 3
                    team.matches_played += 1
        if x[2] == "draw":
            for team in teams:
                if team.name == x[0]:
                    team.draws += 1
                    team.matches_played += 1
                    team.points += 1
                if team.name == x[1]:
                    team.draws += 1
                    team.points += 1
                    team.matches_played += 1
    return teams

class Team:
    def __init__(self, name, wins=None, losses=None, draws=None, matches_played=None):
        self.name = name
        self.wins = wins or 0
        self.losses = losses or 0
        self.draws = draws or 0
        self.matches_played = matches_played or 0
        self.points = 0

    def __str__(self):
        return "{} W:{} L:{} D:{} MP:{} P:{}".format(self.name, self.wins, self.losses, self.draws, self.matches_played, self.points)
    
    def __eq__(self, __value: object) -> bool:
        return self.name == __value.name
pprint.pprint(tally([    "Devastating Donkeys;Blithering Badgers;win",
    "Devastating Donkeys;Blithering Badgers;win",
    "Devastating Donkeys;Blithering Badgers;win",
    "Devastating Donkeys;Blithering Badgers;win",
    "Blithering Badgers;Devastating Donkeys;win",]))
pprint.pprint(tally(["Blithering Badgers;Allegoric Alaskans;loss"]))