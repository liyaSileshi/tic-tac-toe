# Tic Tac Toe
# Reference: With modification from http://inventwithpython.com/chapter10.html. 

# TODOs:  
# 1. Find all TODO items and see whether you can improve the code. 
#    In most cases (if not all), you can make them more readable/modular.
# 2. Add/fix function's docstrings (use """ insted of # for function's header
#    comments)

import random

class TicTacToe:

  def __init__(self, board):
    self.board = board

  def draw_board(self):
    """
    This function prints out the board that it was passed.
    "board" is a list of 10 strings representing the board (ignore index 0).
    """
    print('   |   |')
    print(' ' + self.board[7] + ' | ' + self.board[8] + ' | ' + self.board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + self.board[4] + ' | ' + self.board[5] + ' | ' + self.board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + self.board[1] + ' | ' + self.board[2] + ' | ' + self.board[3])
    print('   |   |')

  def input_player_letter(self):
    """
    Lets the player type which letter they want to be.
    Returns a list with the player’s letter as the first item,
    and the computer's letter as the second.
    """
    letter = ''
    while not (letter == 'X' or letter == 'O'):
      print('Do you want to be X or O?')
      letter = input().upper()

    # the first element in the list is the player’s letter, 
    # the second is the computer's letter.
    if letter == 'X':
      return ['X', 'O']                    
    return ['O', 'X']

  def who_goes_first(self):
    """
    Randomly choose the player who goes first.
    """
    if random.randint(0, 1) == 0:
      return 'computer'                     
    return 'player'

  def play_again(self):
    """
    This function returns True if the player wants to play again,
    otherwise it returns False.
    """
    print('Do you want to play again? (yes or no)')
    return input().lower().startswith('y')

  def make_move(self, board, letter, move):
      board[move] = letter

  def is_winner(self, letter):
    """
    Given a board and a player’s letter, this function returns True if that player has won.
    We use bo instead of board and le instead of letter so we don’t have to type as much.
    """
    ac_top = (self.board[7] == letter and self.board[8] == letter and self.board[9] == letter)
    ac_middle = (self.board[4] == letter and self.board[5] == letter and self.board[6] == letter)
    ac_bottom = (self.board[1] == letter and self.board[2] == letter and self.board[3] == letter)
    do_left = (self.board[7] == letter and self.board[4] == letter and self.board[1] == letter)
    do_middle = (self.board[8] == letter and self.board[5] == letter and self.board[2] == letter)
    do_right = (self.board[9] == letter and self.board[6] == letter and self.board[3] == letter)
    diagonal_a = (self.board[7] == letter and self.board[5] == letter and self.board[3] == letter)
    diagonal_b = (self.board[9] == letter and self.board[5] == letter and self.board[1] == letter)

    return (ac_top or ac_middle or ac_bottom or do_left or
          do_middle or do_right or diagonal_a or diagonal_b)

  def get_board_copy(self):
    """
    Make a duplicate of the board list and return it the duplicate.
    """
    dupeBoard = []

    for i in range(len(self.board)):
        dupeBoard.append(self.board[i])

    return dupeBoard

  def is_space_free(self, board, move):
    """Return true if the passed move is free on the passed board."""
    return board[move] == ' '

  def get_player_move(self):
    """
    Let the player type in their move.
    """
    player_move = ' ' # TODO: W0621: Redefining name 'move' from outer scope. Hint: Fix it according to https://stackoverflow.com/a/25000042/81306
    while player_move not in '1 2 3 4 5 6 7 8 9'.split() or not self.is_space_free(int(player_move)):
        print('What is your next move? (1-9)')
        player_move = input()
    return int(player_move)

  def choose_random_move_from_list(self, moves_list):
    """
    Returns a valid move from the passed list on the passed board.
    Returns None if there is no valid move.
    """
    possible_moves = []
    for i in moves_list:
      if self.is_space_free(self.board, i):
        possible_moves.append(i)

    if len(possible_moves) != 0: # TODO: How would you write this pythanically? (You can google for it!)
        return random.choice(possible_moves)
    return None

#############Stopped here####################
###### fix is space free method to take in copy of board as well
  def get_computer_move(self, comp_letter): # TODO: W0621: Redefining name 'computerLetter' from outer scope. Hint: Fix it according to https://stackoverflow.com/a/25000042/81306
    """
    Given a board and the computer's letter, determine where to move and 
    return that move.
    """
    if comp_letter == 'X':
      player_letter = 'O'
    else:
      player_letter = 'X'

    # Here is our algorithm for our Tic Tac Toe AI:
    # First, check if we can win in the next move
    for i in range(1, 10):
      copy = self.get_board_copy()
      if self.is_space_free(copy, i):
        self.make_move(copy, comp_letter, i)
        if self.is_winner(copy, comp_letter):
          return i

    # Check if the player could win on their next move, and block them.
    for i in range(1, 10):
      copy = self.get_board_copy()
      if self.is_space_free(copy, i):
        self.make_move(copy, player_letter, i)
        if self.is_winner(copy, player_letter):
          return i

    # Try to take one of the corners, if they are free.
    move = self.choose_random_move_from_list(board, [1, 3, 7, 9])
    if move is not None:
        return move

    # Try to take the center, if it is free.
    if self.is_space_free(board, 5):
        return 5

    # Move on one of the sides.
    return self.choose_random_move_from_list(board, [2, 4, 6, 8])

  def is_board_full(self):
    """
    Return True if every space on the board has been taken. Otherwise return False.
    """
    for i in range(1, 10):
        if self.is_space_free(self.board, i):
            return False
    return True

  def set_up_board(self):
    # Reset the board
    self.board = [' '] * 10 # TODO: Refactor the magic number in this line (and all of the occurrences of 10 thare are conceptually the same.)
    player_letter, computer_letter = self.input_player_letter()
    turn = self.who_goes_first()
    print('The ' + turn + ' will go first.')

  def game_is_playing(self):
    while True: 
      # TODO: Usually (not always), loops (or their content) are good candidates to be extracted into their own function.
      # Use a meaningful name for the function you choose.
          if turn == 'player':
              # Player’s turn.
              drawBoard(theBoard)
              move = getPlayerMove(theBoard)
              makeMove(theBoard, playerLetter, move)

              if isWinner(theBoard, playerLetter):
                  drawBoard(theBoard)
                  print('Hooray! You have won the game!')
                  gameIsPlaying = False
              else:  # TODO: is this 'else' necessary?
                  if isBoardFull(theBoard):
                      drawBoard(theBoard)
                      print('The game is a tie!')
                      break
                  else:  # TODO: Is this 'else' necessary?
                      turn = 'computer'

          else:
              # Computer’s turn.
              move = getComputerMove(theBoard, computerLetter)
              makeMove(theBoard, computerLetter, move)

              if isWinner(theBoard, computerLetter):
                  drawBoard(theBoard)
                  print('The computer has beaten you! You lose.')
                  gameIsPlaying = False
              else:     # TODO: is this 'else' necessary?
                  if isBoardFull(theBoard):
                      drawBoard(theBoard)
                      print('The game is a tie!')
                      break
                  else: # TODO: Is this 'else' necessary?
                      turn = 'player'

if __name__ == "__main__":

  print('Welcome to Tic Tac Toe!')

  # TODO: The following mega code block is a huge hairy monster. Break it down 
  # into smaller methods. Use TODO s and the comment above each section as a guide 
  # for refactoring.

  while True:
      # Reset the board
      theBoard = [' '] * 10 # TODO: Refactor the magic number in this line (and all of the occurrences of 10 thare are conceptually the same.)
      playerLetter, computerLetter = inputPlayerLetter()
      turn = whoGoesFirst()
      print('The ' + turn + ' will go first.')
      gameIsPlaying = True # TODO: Study how this variable is used. Does it ring a bell? (which refactoring method?) 
                          #       See whether you can get rid of this 'flag' variable. If so, remove it.

      while gameIsPlaying: # TODO: Usually (not always), loops (or their content) are good candidates to be extracted into their own function.
                          #       Use a meaningful name for the function you choose.
          if turn == 'player':
              # Player’s turn.
              drawBoard(theBoard)
              move = getPlayerMove(theBoard)
              makeMove(theBoard, playerLetter, move)

              if isWinner(theBoard, playerLetter):
                  drawBoard(theBoard)
                  print('Hooray! You have won the game!')
                  gameIsPlaying = False
              else:  # TODO: is this 'else' necessary?
                  if isBoardFull(theBoard):
                      drawBoard(theBoard)
                      print('The game is a tie!')
                      break
                  else:  # TODO: Is this 'else' necessary?
                      turn = 'computer'

          else:
              # Computer’s turn.
              move = getComputerMove(theBoard, computerLetter)
              makeMove(theBoard, computerLetter, move)

              if isWinner(theBoard, computerLetter):
                  drawBoard(theBoard)
                  print('The computer has beaten you! You lose.')
                  gameIsPlaying = False
              else:     # TODO: is this 'else' necessary?
                  if isBoardFull(theBoard):
                      drawBoard(theBoard)
                      print('The game is a tie!')
                      break
                  else: # TODO: Is this 'else' necessary?
                      turn = 'player'

      if not playAgain():
          break