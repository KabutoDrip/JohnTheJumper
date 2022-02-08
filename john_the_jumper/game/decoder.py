# Create a class called Decoder to set and decode the game word
import random

class Decoder():
# A constructor
#   Args: 
#       self (decoder): An instance of Decoder.
#
#   Attributes: To store the privat stirng word and the privat string hidden word.
#       self._set_game_word (string): The game word.
#       self._hidden_word (string): The underscors version of the game word, to guess against.
#       self._good_guess (boolean): If the current guess is part of the word.
    def __init__(self):
        self._game_word()
        self._hidden_word()
        self._good_guess = False

# A setter to set the game word from a list of potential words.
#   Args: 
#       self (decoder): An instance of Decoder.
    def _game_word(self):
        list = ["orange", "banana"]
        word = random.choice(list)
        return word

# A setter that sets underscores, as the new value for the hidden word, for each letter in the game word.
#   Args: 
#       self (decoder): An instance of Decoder.
    def _hidden_word(self):
        hidden_word = []
        for letter in self._game_word():
            hidden_word.append("_")
        hidden_word.append("\n")
        return hidden_word 

# a setter that takes the player guess, checks if the letter is in the game word, updates good guess boolean,
# updates the hidden word at the index of the letter(s) is in the game word.
#   Args: 
#       self (decoder): An instance of Decoder.
#       guess (string): A single letter from guess from terminal input.
    def guess_in_word(self, guess):
        letter_index = 0
        if guess in self._game_word():
            self._good_guess = True
            for char in self._game_word():
                if guess == char:
                    self._hidden_word()[letter_index] = guess # Broken. Need to figure out how to update the list at the index.
                letter_index += 1
        else:
            self._good_guess = False
        
        

# A getter to return the vaule of the hidden word.
#   Args: 
#       self (decoder): An instance of Decoder.
    def get_hidden_word(self):
        return " ".join(self._hidden_word())

# A getter to return the good guess boolean.
#   Args: 
#       self (decoder): An instance of Decoder.
    def get_good_guess(self):
        return self._good_guess

# For debuging
instance = Decoder()
instance.guess_in_word("n")
print(instance.get_hidden_word())
print(instance.get_good_guess())