#  from import 

class Director:
  #  A module that directs the game. 

  #  Attributes:
  #  _is_playing (boolean): Whether or not to keep playing.
  #  _decoder: instance of decoder class
  #  _terminal: instance of Terminal class
  #  _display: instance of display class
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
    # Uses a decoder method to check if the users guess is in the decoder
    # Updates the display with the correctly guessed letters or cuts the cord using display and decoder methods

     # Args:
     # self (Director): An instance of Director.
      
      
      
  def _do_outputs(self):
    # Uses a Terminal method to return the updated display
    
    # Args:
    # self (Director): An instance of Director.

    