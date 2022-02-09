# Just taken from terminal_service.py for Seeker
# Will modify based on this as a template

#from xmlrpc.client import Fault


class TerminalService:
    """A service that handles terminal operations.
   
    The responsibility of a TerminalService is to provide input and output operations for the 
    terminal.
    """


    def read_a_character(self, prompt):

        """Gets a text input from the terminal. Directs the user with the given prompt.

        Args: 
            self (TerminalService): An instance of TerminalService.
            prompt (string): The prompt to display on the terminal.
        #    mode (default = a): selection for the kind of a imput character 

        Returns:
            string: The user's input as a text character. 
        """

        # result after lowered and checked between a to z.
        # will add a loop to check 
        #  

        '''
        accept only a-z or A to Z
        convert upper_case to lower_case
        '''
        judge = False
        while judge != True:
            input_letter = input(prompt).low()
            TerminalService.is_alphabetic_letter(input_letter)
      

        return input_letter



    def _is_alphabetic_letter(letter, num = 1):
        """
        Check the input - alphabetic or not.
        Args: 
            letter: A letter to be checked.
            num (integer): number of input character (default = 1) 
        Returns:
            True: When the letter is an alphabetic one. 
        """
        '''
        accept only a-z or A to Z
        convert upper_case to lower_case
        '''
 
        is_alphabetic = False
        if len(letter) == num:
            if letter.isalpha():
                if letter.isascii():
                   is_alphabetic = True

        return(is_alphabetic)


    

    
        
    def write_text(self, text):
        """
        Displays the given text on the terminal. 
        Args: 
            self (TerminalService): An instance of TerminalService.
            text (string): The text to display.
        """
        print(text)

