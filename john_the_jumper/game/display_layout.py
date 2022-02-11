from lib2to3.pytree import LeafPattern
from turtle import back
from turtle import Screen
import pygame
from pygame import init, mixer
from decoder import Decoder
from terminal import TerminalService
class Display_game:
    guess = False
    print(guess)
    def __init__(self):
        ## initialize pygame and mixer
        pygame.init()
        mixer.init()
        pygame.font.init()
        
        
    def set_values():
        #gets boolean from decoder and returns a chute state for use in display
        global current_state
        global chute_state
        global letter
        current_state = 0
        chute_state = [0,1,2,3,4,5,6]
        letter = ["_" ,"_","_" ,"_" ,"_"]
        
        
        chute_state[0] = "john_the_jumper\game\images/6.png"
        chute_state[1] = "john_the_jumper\game\images/5.png"
        chute_state[2] = "john_the_jumper\game\images/4.png"
        chute_state[3] = "john_the_jumper\game\images/3.png"
        chute_state[4] = "john_the_jumper\game\images/2.png"
        chute_state[5] = "john_the_jumper\game\images/1.png"
        chute_state[6] = "john_the_jumper\game\images/0.png"
        return chute_state[current_state], letter
    
    
    def create_surface():
        ## creates the surface in which the images are manipulated
        global screen
        global background_surface
        global player_surface
        global word_surface
        
        screen = pygame.display.set_mode((624,434))
        pygame.display.set_caption("John The Jumper")
        background_surface = pygame.image.load("john_the_jumper\game\images\sky.jpg")
        player_surface = pygame.image.load("john_the_jumper\game\images\John.png")
        player_surface = pygame.transform.scale(player_surface,(200,200))
        word_surface = pygame.font.SysFont('Comic Sans MS', 50)
        return screen,background_surface,word_surface
    
    
    def mixer():
        ## loads mixer to play sounds
        mixer.music.load("john_the_jumper\game\sound\wind.wav")
        mixer.music.set_volume(0.7)
        mixer.music.play()
        
        
    def update_display(screen,letter,background_surface,player_surface,word_surface,chute_state,current_state):
        ## update display with parachute state if player guesses incorrectly
        incorrect = False
        
        if incorrect == True:
            current_state += 1
        parachute_surface = pygame.image.load(chute_state[current_state])
        parachute_surface1 = pygame.transform.scale(parachute_surface,(200,200))
        word_surface = word_surface.render(f"{letter[0]} {letter[1]}  {letter[2]} {letter[3]} {letter[4]}", False, (212, 212, 212))
        screen.blit(background_surface,(0,0))
        screen.blit(player_surface,(212,200))
        screen.blit(parachute_surface1,(200,78))    
        screen.blit((word_surface),(200,0))

        pygame.display.update()
        
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
        
    
    def terminal_response():
        ## responds in the terminal based on your guess showing if it was correct or not.
        print()
init()
Display_game.set_values()
Display_game.create_surface()    
Display_game.mixer()
Display_game.update_display(screen,letter,background_surface,player_surface,word_surface,chute_state,current_state)
