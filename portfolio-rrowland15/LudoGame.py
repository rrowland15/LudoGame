# Author: Ryan Rowland
# GitHub username: rrowland15
# Date: 07/28/2022
# Description: Project 9 Portfolio Project


class Player:
    """ Represents a player of the LudoGame who will have a chosen position and two tokens (p & q) that have
        a position on the board"""

    def __init__(self, player_letter):
        """Contains a position_dictionary with the player positions (A, B, C, D) as the key and the values
        for each key are a list containing the start position, end position and a dictionary of the safe spaces
        {step counts: safe spaces} for each position """

        player_pos_dict = {"A": [1, 50, {51:"A1",52:"A2",53:"A3",54:"A4",55:"A5",56:"A6",57:"E"}],
                           "B": [15, 8, {51:"B1",52:"B2",53:"B3",54:"B4",55:"B5",56:"B6",57:"E"}],
                           "C": [29, 22, {51:"C1",52:"C2",53:"C3",54:"C4",55:"C5",56:"C6",57:"E"}],
                           "D": [43, 36, {51:"D1",52:"D2",53:"D3",54:"D4",55:"D5",56:"D6",57:"E"}]
                           }                                # {player_letter :[start space, end space, {safe spaces}]}
        self._player_letter = player_letter                 # A, B, C, or D
        self._token_p_step_count = -1   # home yard (-1), ready to go (0), somewhere on the board, or has finished (57)
        self._token_q_step_count = -1   # home yard (-1), ready to go (0), somewhere on the board, or has finished (57)
        self._start_space = player_pos_dict[player_letter][0]    # starting space once moving onto the board
        self._end_space = player_pos_dict[player_letter][1]      # last space before entering the positions safe spaces
        self._safe_spaces = player_pos_dict[player_letter][2]    # safe space position dictionary maps step_counts to safe spaces


    def get_letter(self):
        """ Param: N/A"""
        """ Returns: the letter for the player object"""

        return self._player_letter

    def get_completed(self):
        """ Param: N/A"""
        """ Returns: True if both the p and q token step count data members have reached the end space (57). 
        Otherwise it returns false"""

        if self._token_p_step_count == 57 and self._token_q_step_count == 57:
            return True
        else:
            return False

    def get_token_p_step_count(self):
        """ Param: N/A"""
        """ Returns: the p token step count data member"""

        return self._token_p_step_count

    def get_token_q_step_count(self):
        """ Param: N/A """
        """ Returns: the q token step count data member"""

        return self._token_q_step_count

    def set_token_p_step_count(self, step):
        """ Param: Step is an integer that the token is supposed to increment by"""
        """ Returns: N/A """
        """ Function: Moves the p token step count by the specified number of steps and contains a conditional
            that decrements the appropriate number of steps if the token trys to go beyond the end space on the 
            board (i.e. step count greater than 57)."""

        self._token_p_step_count += step
        if self._token_p_step_count > 57:
            self._token_p_step_count = 57 - (self._token_p_step_count - 57)
            return self._token_p_step_count
        return self._token_p_step_count

    def set_token_q_step_count(self, step):
        """ Param: Step is an integer that the token is supposed to increment by"""
        """ Function: Moves the q token step count by the specified number of steps and contains a conditional
        that decrements the appropriate number of steps if the token trys to go beyond the end space on the 
        board (i.e. step count greater than 57)."""

        self._token_q_step_count += step
        if self._token_q_step_count > 57:
            self._token_q_step_count = 57 - (self._token_q_step_count - 57)
            return self._token_q_step_count
        return self._token_q_step_count

    def send_token_home(self, token):
        """NOT IN ORIGINAL PSEUDOCODE"""
        """ Param: Takes a players token ("p" or "q")"""
        """ Returns: N/A"""
        """ Function: Sends the token back to the home space by resetting the tokens step count to -1. Called by
        the move_token method inside the LudoGame class"""

        if token == "p":
            self._token_p_step_count = -1

        if token == "q":
            self._token_q_step_count = -1

    def get_space_name(self, step_count):
        """ Param: Takes an integer for the step_count"""
        """ Returns: The board space name (string) for the specified step count for that player"""
        """ Function: 
                -- Handles non-safe space names by incrementing off of the players start_space data member
                by the step count. 
                -- When the step count is < 50 and the space name exceeds 56 the appropriate number will
                be decremented so the space names remain within the allowable 56 numbers.
                -- When the step count is >50 it handles space names within a players safe space by 
                looking up the step count within the players safe space dictionary"""

        if step_count == -1:
            space_name = "H"
            return space_name

        if step_count == 0:
            space_name = "R"
            return space_name

        if step_count <= 50:
            temp_space_name = self._start_space - 1 + step_count
            if temp_space_name > 56:
                space_name = temp_space_name - 56
            else:
                space_name = temp_space_name
            return str(space_name)

        if step_count > 50 and step_count <= 57:
            space_name = self._safe_spaces[step_count]
            return str(space_name)


class LudoGame:
    """ Represents a game of Ludo where there are 2 to 4 players"""

    def __init__(self):
        """Data members include a dictionary of players with the player_letter being the key and a list
            of values containing the player object, the players p token step count, the players q token step
            count, the players p token board position and the players q token board position"""
        self._players = {}

    def add_player(self, position):
        """ Param: Takes the desired player letter"""
        """ Returns: N/A """
        """ Function: Uses the Player class to construct a new player and adds it to the Ludogame dictionary
        of players. If the player_letter is not "A", "B","C" or "D" the function will return that that is 
        "Not a position" """
        if position not in self._players:
            if position == "A" or "B" or "C" or "D":
                self._players[position] = [Player(position),
                                           Player(position).get_token_p_step_count(),
                                           Player(position).get_token_q_step_count(),
                                           Player(position).get_space_name(Player(position).get_token_p_step_count()),
                                           Player(position).get_space_name(Player(position).get_token_q_step_count())]
                # Position: [Player_object, p_count, q_count, p position, q position]
            else:
                print("Not a position")
            return

    def update_player_dictionary(self, position):
        """ Param: Takes the designated position """
        """ Returns: N/A """
        """ Function: Updates LudoGame player dictionary after a players token is moved. Called by """
        player = self.get_player_by_position(position)
        self._players[position][1] = player.get_token_p_step_count()
        self._players[position][2] = player.get_token_q_step_count()
        self._players[position][3] = player.get_space_name(player.get_token_p_step_count())
        self._players[position][4] = player.get_space_name(player.get_token_q_step_count())
        return


    def get_player_by_position(self, position):
        """ Param: Takes the specified player letter"""
        """ Returns: the player object associated with that letter or if the player_letter is not in the
        player dictionary it will return "player not found" """

        if position in self._players:
            return self._players[position][0]

        else:
            return "Player not found!"                            # check to see if anything else needs added

    def opponent_knockout(self, new_space_name, player_position):
        """ Param: Takes the specified new_space name and player_position """
        """ Returns:N/A """
        """ Function: Knocks out opponents who are on the player_positions new destination and sends them home"""

        for position in self._players:
            if position != player_position:
                if self._players[position][3] == new_space_name:  # send them home
                    self._players[position][0].send_token_home("p")  #
                    self.update_player_dictionary(player_position)
                    self.update_player_dictionary(position)
                if self._players[position][4] == new_space_name:  # send them home!
                    self._players[position][0].send_token_home("q")  #
                    self.update_player_dictionary(player_position)
                    self.update_player_dictionary(position)

    def evaluate_move_helper(self, player_object, steps, token=None):
        """ Param: Takes the specified player_object (NOT IN ORIGINAL PSEUDOCODE: AND STEPS)"""
        """ Returns:The token (p or q or both) to move based on the algorithm below and the player_object letter to knock 
                back to home if applicable"""

        player_position = player_object.get_letter()
        token_list = [None, None]                       # will contain p and/or q if able to knock opponent to home
        knockout_list = []                              # will contain opponent letters and tokens that
                                                        # could be knocked out
        if token != None:
            final_token = token
            return final_token

        elif self._players[player_position][1] == 57 and self._players[player_position][2] == 57:
            return

        elif self._players[player_position][1] == 57:
            p_new_step_count = 1000000                            # Set to number outside of board range when complete

        elif self._players[player_position][1] != -1:
            p_new_step_count = (self._players[player_position][1]+steps)

        else:
            p_new_step_count = -1

        if self._players[player_position][2] == 57:
            q_new_step_count = 1000000                             # Set to number outside of board range when complete

        elif self._players[player_position][2] != -1:
            q_new_step_count = (self._players[player_position][2]+steps)

        else:
            q_new_step_count = -1

        p_new_destination = player_object.get_space_name(p_new_step_count)         # the space p could end up
        q_new_destination = player_object.get_space_name(q_new_step_count)         # the space q could end up

        if p_new_destination == "E":
            final_token = "p"
            return final_token

        if q_new_destination == "E":
            final_token = "q"
            return final_token

        if p_new_destination != "H":
            for player_key in self._players:
                if player_key != player_position:
                    if self._players[player_key][3] == p_new_destination: # check the other player's p-token against p
                        token_list[0] = "p"
                        knockout_list.append([player_key, "p"])      # record player key and token
                    if self._players[player_key][4] == p_new_destination:   # check the other player's q-token against p
                        token_list[0] = "p"
                        knockout_list.append([player_key, "p"])     # record player key and token

        if q_new_destination != "H":
            for player_key in self._players:
                if player_key != player_position:
                    if self._players[player_key][3] == q_new_destination:  # check the other player's p-token against q
                        token_list[1] = "q"
                        knockout_list.append([player_key, "q"])  # record player key and token
                    if self._players[player_key][4] == q_new_destination:  # check the other player's q-token against q
                        token_list[1] = "q"
                        knockout_list.append([player_key, "q"])      # record player key and token

        if token_list[0] == "p" and token_list[1] == "q" and \
                p_new_destination == q_new_destination:                 # p and q stacked and knocking it out
            final_token = "pq"
            return final_token

        elif token_list[0] == "p" and token_list[1] == "q" and \
                p_new_destination != q_new_destination:                 # p and q not stacked and both can knock out

            if p_new_step_count > q_new_step_count:                     # decide p or q based on location
                final_token = "q"

            else:                                                       # decide p or q based on location
                final_token = "p"

            return final_token

        elif token_list[0] == "p":                                       # p knocking it out
            final_token = "p"
            return final_token

        elif token_list[1] == "q":                                       # q knocking it out
            final_token = "q"
            return final_token

        elif p_new_step_count == q_new_step_count and q_new_destination != "H":   # stacked!
            final_token = "pq"
            return final_token

        elif p_new_step_count > q_new_step_count and q_new_destination != "H":   # q further back needs to catch up
            final_token = "q"
            return final_token

        elif q_new_step_count > p_new_step_count and p_new_destination != "H":   # p further back needs to catch up
            final_token = "p"
            return final_token

        elif p_new_step_count > q_new_step_count and q_new_destination == "H":  # q further back needs to catch up
            final_token = "p"
            return final_token

        elif q_new_step_count > p_new_step_count and p_new_destination == "H":   # p further back needs to catch up
            final_token = "q"
            return final_token

        elif q_new_destination == "H" and p_new_destination == "H":  # both are stuck in home
            final_token = None
            return final_token

    def evaluate_move_six(self, player_object, steps, token):
        """ Param: Takes the specified player_object"""
        """ Returns:The token (p or q) to move based on the algorithm below and the player_object letter to knock 
                back to home if applicable"""

        player_position = player_object.get_letter()

        if token != None:
            if token == "p":
                if player_object.get_token_p_step_count() == -1:
                    player_object.set_token_p_step_count(1)          # move p_token
                    self.update_player_dictionary(player_position)
                else:
                    player_object.set_token_p_step_count(6)
                    self.update_player_dictionary(player_position)

            if token == "q":
                if player_object.get_token_q_step_count() == -1:
                    player_object.set_token_q_step_count(1)         # move q_token
                    self.update_player_dictionary(player_position)
                else:
                    player_object.set_token_q_step_count(6)
                    self.update_player_dictionary(player_position)

        elif self._players[player_position][1] == -1:             # if p-token still in home
            player_object.set_token_p_step_count(1)                  # move p_token
            self.update_player_dictionary(player_position)

        elif self._players[player_position][1] == 51 and \
                self._players[player_position][2] == 51:        # both within reach of E
            player_object.set_token_p_step_count(6)               # get stacked p_token to E
            player_object.set_token_q_step_count(6)               # get stacked q_token to E
            self.update_player_dictionary(player_position)

        elif self._players[player_position][1] == 51 and self._players[player_position][2] != -1:
             player_object.set_token_p_step_count(6)               # get p_token to E
             self.update_player_dictionary(player_position)

        elif self._players[player_position][2] == 51 and self._players[player_position][1] != -1:
             player_object.set_token_p_step_count(6)               # get q_token to E
             self.update_player_dictionary(player_position)

        elif self._players[player_position][2] == -1:           # if q- token still in home
            player_object.set_token_q_step_count(1)                  # move p_token
            self.update_player_dictionary(player_position)


        else:
             final_token = self.evaluate_move_helper(player_object, steps)     # just a normal evaluation go to evaluate_move_helper
             return final_token

    def move_token(self, player_object, steps, token=None):
        """ Param: Takes the designated player_object and the specified number of steps to
        move the token"""
        """ Returns: N/A """

        player_position = player_object.get_letter()

        if steps == 6 and (self._players[player_position][1] == -1 or self._players[player_position][2] == -1
                           or self._players[player_position][1] == 51 or self._players[player_position][2] == 51):

            self.evaluate_move_six(player_object, steps, token)
            return

        else:
            token = self.evaluate_move_helper(player_object, steps, token)


        if token == "p" and player_object.get_token_p_step_count() != -1:               # Move P Token
            player_object.set_token_p_step_count(steps)
            self.update_player_dictionary(player_position)
            new_space_name = self._players[player_position][3]

            return self.opponent_knockout(new_space_name, player_position)

        if token == "q" and player_object.get_token_q_step_count() != -1:               # Move Q Token
            player_object.set_token_q_step_count(steps)
            self.update_player_dictionary(player_position)
            new_space_name = self._players[player_object.get_letter()][4]

            return self.opponent_knockout(new_space_name, player_position)

        if token == "p" and player_object.get_token_p_step_count == -1:                 # can't make that move
            return print("Invalid Move")                                                # doesn't work

        if token == "q" and player_object.get_token_q_step_count == -1:                 # can't make that move
            return print("Invalid Move")                                                # doesn't work

        if token == "pq":                                                               # Move P and Q Tokens- Stacked
            player_object.set_token_q_step_count(steps)
            player_object.set_token_p_step_count(steps)
            self.update_player_dictionary(player_position)
            new_space_name = self._players[player_object.get_letter()][4]

            return self.opponent_knockout(new_space_name, player_position)

    def get_game_status(self):
        """ Param: Takes the LudoGame Object"""
        """ Returns: Game_status (a List of strings for each player and their tokens space_name)"""
        """ Used by the play_game method"""

        Game_Status = []
        for_gradescope = "no"

        if for_gradescope == "yes":
            for position in self._players:
                Game_Status.append(self._players[position][3])
                Game_Status.append(self._players[position][4])

        if for_gradescope == "no":
            for position in self._players:
                Game_Status.append("Player" + " " + str(position) + ":" + "Token-P" + " " + self._players[position][3])
                Game_Status.append("Player" + " " + str(position) + ":" + "Token-Q" + " " + self._players[position][4])

        return Game_Status


    def play_game(self, players, turns):
        """ Param: Takes a list of players and a list of tuples containing those players moves"""
        """ Returns: List of strings for each player and their token space_name"""
        """ Function: Generates the initial player dictionary from the players list parameter and then iterates
                through the tuples within the turns list advancing the players tokens using the move_token method
                when the iteration is complete it then returns where all of the tokens are now located"""

        for position in players:
            self.add_player(position)

        for turn_tuple in turns:
            player_object = self.get_player_by_position(turn_tuple[0])
            steps = turn_tuple[1]
            self.move_token(player_object,steps)

        return self.get_game_status()


def main():
    # Verify that get_completed and get_space name function
    # Ryan = Player("B")
    # print(Ryan.get_completed())
    # print(Ryan._start_space, Ryan._end_space)
    # print("Check space names:")
    # print("\t"+Ryan.get_space_name(-1))
    # print("\t"+Ryan.get_space_name(0))
    # print("\t"+Ryan.get_space_name(50))
    # print("\t"+Ryan.get_space_name(51))
    # print("\t"+Ryan.get_space_name(55))
    # print("\t"+Ryan.get_space_name(57))
    # print("\t"+Ryan.get_space_name(58))

    players = ['A', 'B']
    turns = [('A', 6), ('A', 4), ('A', 5), ('A', 4), ('B', 6), ('B', 4), ('B', 1), ('B', 2), ('A', 6), ('A', 4), ('A', 6),
         ('A', 3), ('A', 5), ('A', 1), ('A', 5), ('A', 4), ('B', 5), ('B', 2),('B', 2), ('A', 1), ('A', 2), ('B', 20),
         ('B', 20), ('B', 1),('B', 6), ('B', 56), ('B', 1), ('A', 6), ('A',2), ('B',2)]
    game = LudoGame()
    current_tokens_space = game.play_game(players, turns)
    player_A = game.get_player_by_position('A')
    #print(player_A)
    #print(game._players["A"])
    #print(player_A.get_completed())
    #print(player_A.get_token_p_step_count())
    print(current_tokens_space)
    player_B = game.get_player_by_position('B')
    #print(player_B.get_space_name(55))
    game_status = game.get_game_status()
    print(player_B.get_completed())
    game.move_token(player_A, 7, "q")
    game.move_token(player_A, 6)
    game_status = game.get_game_status()
    print(game_status)
    game.move_token(player_A, 20)
    game_status = game.get_game_status()
    print(game_status)
    game.move_token(player_A, 20)
    game_status = game.get_game_status()
    print(game_status)
    game.move_token(player_A, 2)
    game_status = game.get_game_status()
    print(game_status)
    game.move_token(player_A, 6)
    game_status = game.get_game_status()
    print(game_status)


def given():
    players = ['A', 'B']
    turns = [('A', 6), ('A', 4), ('A', 5), ('A', 4), ('B', 6), ('B', 4), ('B', 1), ('B', 2), ('A', 6), ('A', 4),
             ('A', 6), ('A', 3), ('A', 5), ('A', 1), ('A', 5), ('A', 4)]
    game = LudoGame()
    current_tokens_space = game.play_game(players, turns)
    player_A = game.get_player_by_position('A')
    print(player_A.get_completed())
    print(player_A.get_token_p_step_count())
    print(current_tokens_space)
    player_B = game.get_player_by_position('B')
    print(player_B.get_space_name(55))



