class Display_game:
    def __init__(self):
        self.current_state = 0
        self.chute_state = [0,1,2,3,4,5,6]
        self.set_values()
    def set_values(self):
        self.chute_state[0] = "john_the_jumper\game\images/6.png"
        self.chute_state[1] = "john_the_jumper\game\images/5.png"
        self.chute_state[2] = "john_the_jumper\game\images/4.png"
        self.chute_state[3] = "john_the_jumper\game\images/3.png"
        self.chute_state[4] = "john_the_jumper\game\images/2.png"
        self.chute_state[5] = "john_the_jumper\game\images/1.png"
        self.chute_state[6] = "john_the_jumper\game\images/0.png"
        return self.chute_state[self.current_state]

    def update_display(self):
        incorrect = False
        if incorrect == True:
            self.current_state += 1
             
display = Display_game()
display.set_values()
display.update_display()