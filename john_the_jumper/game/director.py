from game.decoder import Decoder
from game.terminal import TerminalService 
from game.display_layout import Display_game  

class Director:
  #  A module that directs the game. 

  #  Attributes:
  #  _is_playing (boolean): Whether or not to keep playing.
  #  _decoder: instance of decoder class
  #  _terminal: instance of Terminal class
  #  _display: instance of display class


  def __init__(self):
    # Constructs a new Director.
   
    # Args:
    # self (Director): an instance of Director.
     
    self._is_playing = True
    self._terminal = TerminalService()
    self._decoder = Decoder()
    self._display = Display_game()
              

  def start_game(self):    
    # Starts the game by running the main game loop.
    
    # Args:
    # self (Director): an instance of Director.
    
    self._terminal.write_text(self._decoder.get_hidden_word)

    while self._is_playing:
        self._get_inputs()
        self._do_updates()
        self._do_outputs()


  def _get_inputs(self):  
    # Uses a Terminal method to get the users guess? 
    
    # Args:
    # self (Director): An instance of Director.
    
    guess = self._terminal.read_a_character("\nGuess a letter [a-z]: ")
    return guess
      
  def _do_updates(self, guess):
    # Uses a decoder method to check if the users guess is in the decoder
    # Updates the display with the correctly guessed letters or cuts the cord using display and decoder methods

     # Args:
     # self (Director): An instance of Director.

    self._decoder.guess_in_word(guess)
          
      
  def _do_outputs(self):
    # Uses a Terminal method to return the updated display
    
    # Args:
    # self (Director): An instance of Director.
    
    self._terminal.write_text(self._decoder.get_hidden_word())
   
    if self._decoder.word_guessed() == True:
      self._terminal.write_text("\nGood Job! You guessed the secret word and landed safely!")
      self._is_playing = False


    if self._display.current_state == 0:
      self._terminal.write_text("\nSorry, you lose.")
      is_playing = False
