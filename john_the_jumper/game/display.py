
class Display_game:
    def __init__(self):
        self.current_state = 0
        self.chute_state = [0,1,2,3,4,5,6]
        self._set_values()
        
    def _set_values(self):
        self.chute_state[0] = " ___ \n/___\\\n\\   /\n \ /\n  O\n /|\\\n / \\"
        self.chute_state[1] = "/___\\\n\\   /\n \ /\n  O\n /|\\\n / \\"
        self.chute_state[2] = "\\   /\n \ /\n  O\n /|\\\n / \\"
        self.chute_state[3] = " \ /\n  O\n /|\\\n / \\"
        self.chute_state[4] = "  X\n /|\\\n / \\"
        self.chute_state[5] = "  O\n /|\\\n / \\"
        self.chute_state[6] = "  O\n /|\\\n / \\"
        
    def update_display(self,incorrect):
        returned = ""
        if incorrect == True:
            returned = self.chute_state[self.current_state]
            print(returned)
           
        elif incorrect == False:
            self.current_state += 1
            returned = self.chute_state[self.current_state]
            print(returned)
        return returned   
    def get_current_state(self):
        return self.current_state
