class Player:
    id = int
    name = str
    club = str
    value = float
    goals = int
    assists = int
    clean_sheets = int
    game_time = float
    goals_per_game = float
    assists_per_game = float
    clean_sheets_game = float


class Team:
    id = int
    goalkeepers = list()
    defenders = list()
    midfielders = list()
    forwards = list()

    def make_chromosome:
        #make a binary chromosome based on the players in the list.
        #[0]*number_of_players
        #for each id in team:
        #   use id as list index, convert to 1
        pass




