from pickle import TRUE


class Display_game:
    def __init__(self):
        self.current_state = 0
        self.chute_state = [0,1,2,3,4,5,6]
        self._set_values()
        
    def _set_values(self):
        self.chute_state[0] = "1"
        self.chute_state[1] = "2"
        self.chute_state[2] = "3"
        self.chute_state[3] = "4"
        self.chute_state[4] = "5"
        self.chute_state[5] = "6"
        self.chute_state[6] = "7"
        
    def update_display(self,incorrect):
        if incorrect == False:
            returned = self.chute_state[self.current_state]

        elif incorrect == True:
            self.current_state += 1
            returned = self.chute_state[self.current_state]

        return returned   
    
c = Display_game()
c.update_display(True)