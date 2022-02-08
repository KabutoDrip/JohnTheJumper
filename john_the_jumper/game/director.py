from game import decoder
from game import terminal
from display import display_layout  

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
    self._decoder = Decoder()
    self._terminal = Terminal()
    self._display = Display()
              

  def start_game(self):    
    # Starts the game by running the main game loop.
    
    # Args:
    # self (Director): an instance of Director.
    
    while self._is_playing:
        self._get_inputs()
        self._do_updates()
        self._do_outputs()


  def _get_inputs(self):  
    # Uses a Terminal method to get the users guess? 
    
    # Args:
    # self (Director): An instance of Director.
    
    guess = self._terminal.get_input()
    return guess
      
  def _do_updates(self, guess):
    # Uses a decoder method to check if the users guess is in the decoder
    # Updates the display with the correctly guessed letters or cuts the cord using display and decoder methods

     # Args:
     # self (Director): An instance of Director.

    guess_result = self._decoder.decode(self.guess)
    return guess_result  
      
      
  def _do_outputs(self, guess_result):
    # Uses a Terminal method to return the updated display
    
    # Args:
    # self (Director): An instance of Director.

   self._terminal.print_answer(guess_result)

   if self.display.cords == 0:
     self.terminal.write_text("Sorry, you loose")
     is_playing = False
  