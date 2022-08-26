import unittest
from LudoGame import Player, LudoGame


class Unitcases(unittest.TestCase):
    """
    Contains unit tests for player class
    """
    def test_player_class(self):
        """Test init, get and set methods for Player class"""

        # Verify players can be created, that the get_letter, get_token_p_step_count, get_token_q_step count,
        # get_completed, set_token_p_step_count, set_token_q_step_count and get_space name methods function

        player1= Player("A")
        player2= Player("D")

        self.assertEqual(player1.get_letter(), "A")             # Verify get_letter
        self.assertEqual(player2.get_letter(), "D")             # Verify get_letter
        self.assertEqual(player2.get_completed(), False)        # Verify get_completed returns False
        self.assertEqual(player2.get_token_p_step_count(), -1)  # Verify player2's p token starts at home
        self.assertEqual(player2.get_token_q_step_count(), -1)  # Verify player2's q token starts at home

        player2.set_token_p_step_count(58)                      # Verify get_completed returns False
        player2.set_token_q_step_count(58)                      # Verify get_completed returns False
        self.assertEqual(player2.get_completed(), True)         # Verify get_completed returns True

        self.assertEqual(player2.get_space_name(57), "E")       # Verify end space is "E"
        self.assertEqual(player2.get_space_name(51), "D1")      # Verify first safe space is "D1"

    def test_LudoGame_class(self):
        """Test Game Functionality"""

        #Verify

        players = ['A', 'B', 'C', 'D']
        turns = [('A', 6), ('A', 4), ('A', 5), ('A', 4), ('B', 6), ('B', 4), ('B', 1), ('B', 2), ('A', 6), ('A', 4),
                 ('A', 6), ('A', 3), ('A', 5), ('A', 1), ('A', 5), ('A', 4), ('B', 5), ('B', 2), ('B', 2), ('A', 1),
                 ('A', 2), ('B', 20), ('B', 20), ('B', 1), ('B', 6), ('B', 56), ('B', 1)]

        game = LudoGame()

        current_tokens_space = game.play_game(players, turns)
        self.assertEqual(current_tokens_space,
                         ['Player A:Token-P H', 'Player A:Token-Q H',
                          'Player B:Token-P E', 'Player B:Token-Q E',
                          'Player C:Token-P H', 'Player C:Token-Q H',
                          'Player D:Token-P H', 'Player D:Token-Q H'])

        Ryan = game.get_player_by_position("A")                 # Can assign a name to player by calling object
        self.assertEqual(Ryan.get_token_p_step_count(), -1)     # Ryan still at home
        game.move_token(Ryan, 6)
        self.assertEqual(Ryan.get_token_p_step_count(), 0)      # Confirm Ryan's p token is moved to ready position 1st
        game.move_token(Ryan, 6, "p")
        self.assertEqual(Ryan.get_token_p_step_count(), 6)      # Confirm Ryan can override alogrithm and move p 6
        game.move_token(Ryan, 5, "q")
        self.assertEqual(Ryan.get_token_q_step_count(), -1)     # Confirm Ryan can't override algorithm and move q
        game.move_token(Ryan, 6, "q")
        game.move_token(Ryan, 6)
        self.assertEqual(Ryan.get_token_q_step_count(), 6)      # Confirm Ryan can't override algorithm and move q
        game.move_token(Ryan, 3)
        self.assertEqual(Ryan.get_token_q_step_count(), 9)      # Confirm p&q stacked
        self.assertEqual(Ryan.get_token_p_step_count(), 9)      # Confirm p&q stacked


        Dwight = game.get_player_by_position("D")              # Confirm Dwight knocks Ryan's tokens back to home
        game.move_token(Dwight, 6)
        game.move_token(Dwight, 9)
        game.move_token(Dwight, 14)

        p_step_count = Dwight.get_token_p_step_count()
        self.assertEqual(Dwight.get_space_name(p_step_count), "9")

        self.assertEqual(Ryan.get_token_q_step_count(), -1)
        self.assertEqual(Ryan.get_token_p_step_count(), -1)     # Confirmed

        game.move_token(Ryan, 6)                                # Confirm p token now separated from q
        game.move_token(Ryan, 3)
        self.assertEqual(Ryan.get_token_p_step_count(), 3)
        self.assertEqual(Ryan.get_token_q_step_count(), -1)     # Confirmed


        print(game.get_game_status())            # Confirm that get_game_status_post_play_game works

                                                                # Confirm that if a piece is in home and if a roll gets
        game.move_token(Dwight, 31)                             # a player in to home, that moving the player to the end
        game.move_token(Dwight, 6)                              # space is prioritized (unless it's a 6)
        game.move_token(Dwight, 4)
        game.move_token(Dwight, 3)
        self.assertEqual(Dwight.get_token_p_step_count(), 57)     # Confirmed

    def test_case_1(self):
        players = ['A', 'B', 'C', 'D']
        turns = [('A', 6), ('A', 1), ('B', 6), ('B', 2), ('C', 6), ('C', 3), ('D', 6), ('D', 4)]
        game2 = LudoGame()
        current_tokens_space = game2.play_game(players, turns)
        self.assertEqual(current_tokens_space, ["Player A:Token-P 1", 'Player A:Token-Q H',
                                                "Player B:Token-P 16", 'Player B:Token-Q H',
                                                "Player C:Token-P 31", 'Player C:Token-Q H',
                                                "Player D:Token-P 46", 'Player D:Token-Q H'])



    def test_case_2(self):
        players = ['A', 'B']
        turns = [('B', 6), ('B', 4), ('B', 5), ('B', 4), ('B', 4), ('B', 3), ('B', 4), ('B', 5), ('B', 4), ('B', 4),
              ('B', 5), ('B', 4), ('B', 1), ('B',4), ('B', 5), ('B', 5), ('B', 5)]
        game2 = LudoGame()
        current_tokens_space = game2.play_game(players, turns)
        self.assertEqual(current_tokens_space, ["Player A:Token-P H", 'Player A:Token-Q H',
                                                "Player B:Token-P B6", 'Player B:Token-Q H'])

#
    def test_case_3(self):
        players = ['A', 'B']
        turns = [('A', 6), ('A', 3), ('A', 6), ('A', 3), ('A', 6), ('A', 5), ('A', 4), ('A', 6), ('A', 4)]
        game2 = LudoGame()
        current_tokens_space = game2.play_game(players, turns)
        self.assertEqual(current_tokens_space, ["Player A:Token-P 28", 'Player A:Token-Q 28',
                                                "Player B:Token-P H", 'Player B:Token-Q H'])

    def test_case_4(self):
        players = ['A', 'C']
        turns = [('A', 6), ('A', 4), ('A', 4), ('A', 4), ('A', 5), ('A', 6), ('A', 4), ('A', 6), ('A', 4), ('A', 6),
             ('A', 6), ('A', 6), ('A', 4), ('A',6), ('A', 6), ('C', 6), ('C', 4)]
        game2 = LudoGame()
        current_tokens_space = game2.play_game(players, turns)
        self.assertEqual(current_tokens_space, ["Player A:Token-P 33", 'Player A:Token-Q H',
                                           "Player C:Token-P 32", 'Player C:Token-Q H'])


    def test_case_5(self):
        players = ['A', 'B']
        turns = [('A', 6), ('A', 4), ('A', 4), ('A', 4), ('A', 5), ('A', 6), ('A', 4), ('A', 6), ('A', 4), ('A', 6),
              ('A', 6), ('A', 4), ('A', 6), ('A',4), ('A', 6), ('A', 6), ('A', 4), ('A', 6), ('A', 6), ('A', 4),
                 ('A', 6), ('A', 6), ('A', 4), ('A', 6), ('A', 3), ('A', 6), ('B', 6), ('A', 6)]
        game2 = LudoGame()
        current_tokens_space = game2.play_game(players, turns)
        self.assertEqual(current_tokens_space, ["Player A:Token-P E", 'Player A:Token-Q E',
                                                "Player B:Token-P R", 'Player B:Token-Q H'])


    def test_case_6(self):
        players = ['A', 'B']
        turns = [('A', 6), ('A', 2), ('A', 2), ('A', 6), ('A', 4), ('A', 5), ('A', 4), ('A', 4), ('B', 6), ('B', 3),
             ('A', 6), ('A', 3)]
        game2 = LudoGame()
        current_tokens_space = game2.play_game(players, turns)
        self.assertEqual(current_tokens_space, ["Player A:Token-P 3", 'Player A:Token-Q H',
                                                "Player B:Token-P 17", 'Player B:Token-Q H'])


    def test_case_7(self):
        players = ['A', 'B']
        turns = [('A', 6), ('A', 4), ('A', 5), ('A', 4), ('A', 4), ('A', 4), ('A', 5), ('A', 4), ('A', 5), ('A', 5),
              ('A', 3), ('A', 5), ('A', 3), ('A',6)]
        game2 = LudoGame()
        current_tokens_space = game2.play_game(players, turns)
        self.assertEqual(current_tokens_space, ["Player A:Token-P A1", 'Player A:Token-Q R',
                                                "Player B:Token-P H", 'Player B:Token-Q H'])


    def test_case_8(self):
        players = ['A', 'B']
        turns = [('A', 6), ('A', 4), ('A', 5), ('A', 4), ('A', 4), ('A', 4), ('A', 5), ('A', 4), ('A', 5), ('A', 5),
              ('A', 3), ('A', 5), ('A', 5), ('A',6), ('A', 5), ('A', 5), ('A', 3), ('B', 6), ('B', 3), ('A', 4)]
        game2 = LudoGame()
        current_tokens_space = game2.play_game(players, turns)
        self.assertEqual(current_tokens_space, ["Player A:Token-P E", 'Player A:Token-Q 13',
                                                "Player B:Token-P 17", 'Player B:Token-Q H'])


    def test_case_9(self):
        players = ['A', 'B']
        turns = [('A', 6), ('A', 4), ('A', 4), ('A', 4), ('A', 6), ('A', 5), ('A', 3), ('B', 6), ('B', 2), ('A', 2),
              ('A', 4)]
        game2 = LudoGame()
        current_tokens_space = game2.play_game(players, turns)
        self.assertEqual(current_tokens_space, ["Player A:Token-P 16", 'Player A:Token-Q 10',
                                                "Player B:Token-P H", 'Player B:Token-Q H'])

    def test_case_10(self):
        # KNOCK OUT OPPONENT WITH FORWARD PLAYER WHEN BOTH ARE OUT.
        players = ['A', 'D']
        turns = [('A', 6), ('A', 1), ('A', 6), ('A', 10), ('D',6), ('D', 16), ('D',6), ('D', 20), ('D', 4)]
        game2 = LudoGame()
        current_tokens_space = game2.play_game(players, turns)
        print(current_tokens_space)

    def test_case_11(self):
        # BOTH TOKENS HAVE KNOCKOUT OPPORTUNITY SHOULD BE ONE IN BACK
        players = ['A', 'D']
        turns = [('A', 6), ('A', 5), ('A', 6), ('A', 10), ('D',6), ('D', 16), ('D',6), ('D', 21), ('D', 3) ]
        game2 = LudoGame()
        current_tokens_space = game2.play_game(players, turns)
        print(current_tokens_space)

    def test_case_12(self):
        # KNOCKOUT STACKED TOKENS
        players = ['A', 'D']
        turns = [('A', 6), ('A', 5), ('A', 6), ('A', 10), ('D',6), ('D', 16), ('D',6), ('D', 21), ('A', 5), ('D', 3)]
        game2 = LudoGame()
        current_tokens_space = game2.play_game(players, turns)
        print(current_tokens_space)







