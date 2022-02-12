from pickle import TRUE


class Display_game:
    def __init__(self):
        self.current_state = 0
        self.chute_state = [0,1,2,3,4,5,6]
        self._set_values()
        
    def _set_values(self):
        self.chute_state[0] = "hello"
        self.chute_state[1] = "L"
        self.chute_state[2] = "hello"
        self.chute_state[3] = "john_the_jumper\game\images/3.png"
        self.chute_state[4] = "john_the_jumper\game\images/2.png"
        self.chute_state[5] = "john_the_jumper\game\images/1.png"
        self.chute_state[6] = "john_the_jumper\game\images/0.png"
        
    def update_display(self,incorrect):
        if incorrect == True:
            self.current_state += 1
            print(self.chute_state[self.current_state])

        return self.chute_state[self.current_state]   
    
c = Display_game()
c.update_display(True)