#  from import 

class Director:
  #  A module that directs the game. 

  #  Attributes:
  #  is_playing (boolean): Whether or not to keep playing.
  #  word: instance of Word class
  #  terminal: instance of Terminal class
  #  parachute: instance of Parachute class
  #  etc.
        

  def __init__(self):
    # Constructs a new Director.
   
    # Args:
    # self (Director): an instance of Director.
     
    self._is_playing = True
              

  def start_game(self):    
    # Starts the game by running the main game loop.
    
    # Args:
    # self (Director): an instance of Director.
    
    while self._is_playing:
        self._get_inputs()
        self._do_updates()
        self._do_outputs()


  def _get_inputs(self):  
    # Uses a Terminal method to get the users guess 
    
    # Args:
    # self (Director): An instance of Director.
    
    
    
  def _do_updates(self):
    # Uses a Word method to check if the users guess is in the word
    # Updates the display with the correctly guessed letters or cuts the cord using Parachute and Word methods

     # Args:
     # self (Director): An instance of Director.
      
      
      
  def _do_outputs(self):
    # Uses a Terminal method to return the updated display
    
    # Args:
    # self (Director): An instance of Director.

    