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
        self._game_word = ""
        self._set_game_word()
        self._hidden_word = []
        self._set_hidden_word()
        self._good_guess = False

# A setter to set the game word from a list of potential words.
#   Args: 
#       self (decoder): An instance of Decoder.
    def _set_game_word(self):
        list = ["orange", "apple", "banana", "pineapple", "mango", "grape", "passionfruit", "guava", "tomato"]
        self._game_word = random.choice(list)

# A setter that sets underscores, as the new value for the hidden word, for each letter in the game word.
#   Args: s
#       self (decoder): An instance of Decoder.
    def _set_hidden_word(self):
        for letter in self._game_word:
            self._hidden_word.append("_")

# a setter that takes the player guess, checks if the letter is in the game word, updates good guess boolean,
# updates the hidden word at the index of the letter(s) is in the game word.
#   Args: 
#       self (decoder): An instance of Decoder.
#       guess (string): A single letter from guess from terminal input.
    def guess_in_word(self, guess):
        if guess in self._game_word:
            self._good_guess = True
            letter_index = 0
            for char in self._game_word:
                if guess == char:
                    self._hidden_word[letter_index] = guess # Broken. Need to figure out how to update the list at the index.
                letter_index += 1
            return "Good Job!"
        else:
            self._good_guess = False
            return "Oops, try again."

    def word_guessed(self):
        return (self._game_word == "".join(self._hidden_word))
        

# A getter to return the vaule of the hidden word.
#   Args: 
#       self (decoder): An instance of Decoder.
    def get_hidden_word(self):
        return " ".join(self._hidden_word)

# A getter to return the good guess boolean.
#   Args: 
#       self (decoder): An instance of Decoder.
    def get_good_guess(self):
        return self._good_guess

