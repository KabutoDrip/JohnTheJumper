from lib2to3.pytree import LeafPattern
from turtle import back
from turtle import Screen
import pygame
from pygame import init, mixer

class Display_game:
    
    def __init__(self):
        ## initialize pygame, mixer, and pygame text
        pygame.init()
        mixer.init()
        pygame.font.init()
        self.current_state = 0
        self.chute_state
        self.set_values()
        self.create_surface()
        self.mixer()
    def set_values(self):
        #gets boolean from decoder and returns a chute state for use in display
        #makes all variables being sent between functions global for ease of access
        chute_state = [0,1,2,3,4,5,6]
        # letter is what gets printed so wherever these are stored need to be printed here
        
        #assigns an image to each parachute state
        chute_state[0] = "john_the_jumper\game\images/6.png"
        chute_state[1] = "john_the_jumper\game\images/5.png"
        chute_state[2] = "john_the_jumper\game\images/4.png"
        chute_state[3] = "john_the_jumper\game\images/3.png"
        chute_state[4] = "john_the_jumper\game\images/2.png"
        chute_state[5] = "john_the_jumper\game\images/1.png"
        chute_state[6] = "john_the_jumper\game\images/0.png"
        #returns the parachute state as well as the letters to be printed
        return chute_state[self.current_state]
    
    
    def create_surface(self):
        ## creates the surface in which the images are manipulated
        #makes all variables being sent between functions global for ease of access
        self.screen
        self.background_surface
        self.player_surface
        self.word_surface
        #creates the screen
        screen = pygame.display.set_mode((624,434))
        #names the screen
        pygame.display.set_caption("John The Jumper")
        #creates the background
        background_surface = pygame.image.load("john_the_jumper\game\images\sky.jpg")
        #creates and scales the player
        player_surface = pygame.image.load("john_the_jumper\game\images\John.png")
        player_surface = pygame.transform.scale(player_surface,(200,200))
        #creates the word locations
        word_surface = pygame.font.SysFont('Comic Sans MS', 50)
        #returns the necessary vars for updating
        return screen,background_surface,word_surface
    
    
    def mixer(self):
        ## loads mixer to play sounds
        mixer.music.load("john_the_jumper\game\sound\wind.wav")
        mixer.music.set_volume(0.7)
        mixer.music.play()
        
        
    def update_display(self,screen,background_surface,player_surface,word_surface,chute_state,current_state):
        ## update display with parachute state if player guesses incorrectly
        
        #!!!!!VAR THAT NEEDS TO BE UPDATED BY DECODER!!!!!
        incorrect = False
        
        if incorrect == True:
            current_state += 1
        #loads the updated images and words based on what has been changed
        parachute_surface = pygame.image.load(chute_state[current_state])
        parachute_surface1 = pygame.transform.scale(parachute_surface,(200,200))
        #physically creates objects
        screen.blit(background_surface,(0,0))
        screen.blit(player_surface,(212,200))
        screen.blit(parachute_surface1,(200,78))    
        screen.blit((word_surface),(250,0))

        pygame.display.update()
        
        #basic loop for exiting pygame
        
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
        
    

