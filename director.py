#  fill in: from import 

class Director:
  #  A module that directs the game. 

  #  Attributes:
  #  is_playing (boolean): Whether or not to keep playing.
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
    # 

    # Args:
    # self (Director): An instance of Director.
    
    
    
  def _do_updates(self):
     #

     # Args:
     # self (Director): An instance of Director.
      
      
      
  def _do_outputs(self):
    #
    
    # Args:
    # self (Director): An instance of Director.

    