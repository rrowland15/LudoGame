# Author: Ryan Rowland
# GitHub username: rrowland15
# Date: 07/31/2022
# Description: Project 9 Portfolio Project Pseudocode

class Player:
    """ Represents a player of the LudoGame who will have a chosen position and two tokens (p & q) that have
    a position on the board"""


    def __init__(self, player_letter):
    """Contains a position_dictionary with the player positions (A, B, C, D) as the key and the values
            for each key are a list containing the start position, end position and a dictionary of the safe spaces
            {step counts: safe spaces} for each position """

    """Data members include the player_letter, the step count for the p token, the step count for the q
    token, the start_space for that players letter (from the position_dictionary), the end_space for that players
    letter (from the position_dictionary) and the safe space dictionary (from the position_dictionary)"""


    def get_letter(self):
    """ Param: N/A"""
    """ Returns: the letter for the player object"""


    def get_completed(self):
    """ Param: N/A"""
    """ Returns: True if both the p and q token step count data members are equal to 57. Otherwise
    it returns false"""


    def get_token_p_step_count(self):
    """ Param: N/A"""
    """ Returns: the p token step count data member"""


    def get_token_q_step_count(self):
    """ Param: N/A """
    """ Returns: the q token step count data member"""


    def set_token_p_step_count(self, step):
    """ Param: Step is an integer that the token is supposed to increment by"""
    """ Returns: N/A """
    """ Function: Moves the p token step count by the specified number of steps and contains a conditional
        that decrements the appropriate number of steps if the token trys to go beyond the end space on the 
        board (i.e. step count greater than 57)."""


    def set_token_q_step_count(self, step):
    """ Param: Step is an integer that the token is supposed to increment by"""
    """ Function: Moves the q token step count by the specified number of steps and contains a conditional
    that decrements the appropriate number of steps if the token trys to go beyond the end space on the 
    board (i.e. step count greater than 57)."""


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


class LudoGame:
    """ Represents a game of Ludo where there are 2 to 4 players"""


    def __init__(self):
    """Data members include a dictionary of players with the player_letter being the key and a list
    of values containing the player object, the players p token step count, the players q token step
    count, the players p token board position and the players q token board position"""


    def add_player(self, player_letter):
    """ Param: Takes the desired player letter"""
    """ Returns: N/A """
    """ Function: Uses the Player class to construct a new player and adds it to the Ludogame dictionary
    of players. If the player_letter is not "A", "B","C" or "D" the function will return that that is 
    "Not a position" """


    def get_player_by_position(self, player_letter):
    """ Param: Takes the specified player letter"""
    """ Returns: the player object associated with that letter or if the player_letter is not in the
    player dictionary it will return "player not found" """


    def evaluate_move_six(player_object):
    """ Param: Takes the specified player_object"""
    """ Returns:The token (p or q) to move based on the algorithm below and the player_object letter to knock 
            back to home if applicable"""
    """ Function: Pulls the player object's token step_counts from the player_dictionary
            -- Since the number of specified steps is 6 it will look to see if the player has a token with a 
            step_count that indicates the token is in the home position or if the player has a token with 
            a step_count within 6 of the end space. It will prioritize: 
                    -- moving the token within 6 of the end space followed by 
                    -- moving the token out of the home space followed by 
            If neither of those are true:
                initializes evaluate_move_not_six method to return the list that algorithm generates """


    def evaluate_move_not_special(player_object, steps):
    """ Param: Takes the specified player_object"""
    """ Returns:The token (p or q or both) to move based on the algorithm below and the player_object letter to knock 
            back to home if applicable"""
    """ Function: Pulls the players object's token step_counts from the player_dictionary
            -- Initiates a new 3 member list containing [None, None, None]
            -- Evaluate both of the potential p and q destinations (using the get_step_count and get_space_name methods)
                -- Iterate through the player_dictionary to determine if any of the players are on the potential 
                p or q destinations

                        If yes to both AND on the same step_count (overwrite 1st, 2nd and 3rd element of list)
                            -- return: both tokens and the player knocked out

                        If yes to both AND not on the same step_count,  (overwrite 1st or 2nd and 3rd element of the list)
                            -- return the token that is at a lower step count and the player knocked out

                        If yes to one, (overwrite 1st or 2nd and 3rd element of the list)
                            -- return the token that lands on another players token 

                        If no to both and on the same step_count,(overwrite 1st and 2nd element of the list)
                            -- return the token that is closer to the home space, if they are at the same space move both. 

                        If no to both and not on the same step_count, (overwrite 1st or 2nd element of the list)
                            -- return the token that is closer to the home space, if they are at the same space move both."""


    def move_token(self, player_object, steps):
    """ Param: Takes the designated player_object and the specified number of steps to
    move the token"""
    """ Returns: N/A """
    """ Function1: Takes the specified player_object and steps and uses either the evaluate_move_six or 
            evaluate_move_not_six method to determine which token should be moved
            -- increments the player's optimal token the number of steps using the player set_token_p_stepcount 
            and/or set_token_q_stepcount methods to update the token step counts
            -- also moves the other player back to home if the move algorithms indicate a shared location by
            checking the returned player_objects p and q tokens and using the set_token_p_stepcount and/or the
            set_token_q_stepcount methods to reset them back to home (-1)."""


    def play_game(self, players, turns):
    """ Param: Takes a list of players and a list of tuples containing those players moves"""
    """ Returns: List of strings for each player and their token space_name"""
    """ Function: Generates the initial player dictionary from the players list parameter and then iterates
            through the tuples within the turns list advancing the players tokens using the move_token method
            when the iteration is complete it then returns where all of the tokens are now located"""


"""
1. Determining whether you will need a board class and how to store and update the token positions with the movement 
of tokens

    No board class is necessary because all of the players and pieces are being managed internally to the LudoGame Class
    within a player_dictionary.
    
2. Initializing the Players and LudoGame classes

    This is handled through the play_game method. After a new Ludo_game class has been initiated the play_game method
    should be called which will generate a list of players (adding them to the player dictionary), the dictionary will
    then be used to track the players moves logged by the turns
    
3. Determining how to implement get_space_name method in the Players class for different player positions
    
    This is handled by incrementing off of the start position for the specified player_letter key inside the 
    position_dictionary. Additional details around how the step_count will be used to cycle back to the lower number
    space names is included above on lines 61-66
    
4. Determining how to implement move_token method in the LudoGame class and what parameters needs to be updated after 
the move of the token
    
    The evaluate_move_six and evaluate_move_not_special are used within the move_token method in order to simplify the 
    implementation into smaller pieces. The evaluate_move_six method handles moving a piece into the end square, moving 
    a piece out of the home square and if neither of those is possible it calls the evaluate_move_not_special method
    to iterate through the possible options and prioritize accordingly. For additional details see lines 111-130
    
    After determining the token(s) to move and the potential opponent to be knocked back to home, the function uses the 
    appropriate set_count method (p or q or both if stacked) to advance the token. If an opponent is included in the 
    return list it will also check both of the opponents p and q tokens and reset whichever one is at the same space name
    as the moving player back to the home position of -1.

5. Determining where to implement the priority rule and how many different cases there will be with the combinations of 
different token states
    
    The priority rule is split between the evaluate move_six and evaluate_move_not_special methods.
        1. No tokens on board and moving p token out - Evaluate_move_six
        2. Step 6, within 6 of end space - Evaluate_move_six    (can be stacked)
        3. Step 6, not within 6 and moving q token out - Evaluate_move_six
        4. Knocking out an opponent - Evaluate_move_not_special (can be stacked)
        5. Moving the piece closest to home - Evaluate_move_not_special (can be stacked)
        
6. Determining how you will implement and use the get_token_p(q)_step_count method
        
        The get_token_step_count methods just returns the token_step_count data members. Rather than call it every
        time I have it registered within the player_dictionary in the LudoGame Class
        
7. Determining how you will implement the stacking state of two tokens for one player
        
        This is handled in the evaluate_move_six and evaluate_move_not_special methods. If the stepcount for the two are
        identical going in to the move, then both the p and q token will end up in the list that gets passed to the 
        move_token member. 
"""