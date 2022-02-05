# Create a class called Decoder to set and decode the game word

# A constructor
#   Args: 
#       self (decoder): An instance of Decoder.
#
#   Attributes: To store the privat stirng word and the privat string hidden word.
#       self.game_word (string): The game word.
#       self.hidden_word (string): The underscors version of the game word, to guess against.
#       self.good_guess (boolean): If the current guess is part of the word.

# A setter to set the game word from a list of potential words.
#   Args: 
#       self (decoder): An instance of Decoder.

# A setter that sets underscores, as the new value for the hidden word, for each letter in the game word.
#   Args: 
#       self (decoder): An instance of Decoder.

# a setter that takes the player guess, checks if the letter is in the game word, updates good guess boolean,
# updates the hidden word at the index of the letter(s) is in the game word.
#   Args: 
#       self (decoder): An instance of Decoder.
#       guess (string): A single letter from guess from terminal input.

# A getter to return the vaule of the hidden word.
#   Args: 
#       self (decoder): An instance of Decoder.

# A getter to return the good guess boolean.
#   Args: 
#       self (decoder): An instance of Decoder.

