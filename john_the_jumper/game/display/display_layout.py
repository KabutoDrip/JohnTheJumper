from turtle import back
from turtle import Screen
import pygame
from pygame import mixer

class Display_game:
    
    def __init__(self):
        ## initialize pygame and mixer
        pygame.init()
        mixer.init()
        
    def set_values():
        #gets boolean from decoder and returns a chute state for use in display
        current_state = 0
        if bool == False:
            current_state += 1
        chute_state = [0,1,2,3,4,5,6]
        chute_state[0] = "images/6.png"
        chute_state[1] = "images/5.png"
        chute_state[2] = "images/4.png"
        chute_state[3] = "images/3.png"
        chute_state[4] = "images/2.png"
        chute_state[5] = "images/1.png"
        chute_state[6] = "images/0.png"
        return chute_state[current_state]
    def create_surface():
        ## creates the surface in which the images are manipulated
        screen = pygame.display.set_mode((624,434))
        pygame.display.set_caption("John The Jumper")
        background_surface = pygame.image.load("images/sky.jpg")
        player_surface = pygame.image.load("images/John.png")
        player_surface = pygame.transform.scale(player_surface,(200,200))
        return screen,background_surface
    def mixer():
        ## loads mixer to play sounds
        mixer.music.load("sound/wind.wav")
        mixer.music.set_volume(0.7)
        mixer.music.play()
    def update_display(screen,background_surface,player_surface,chute_state):
        ## update display with parachute state if player guesses incorrectly
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

            for i in range (0,6):
                parachute_surface = pygame.image.load(chute_state[i])
                parachute_surface1 = pygame.transform.scale(parachute_surface,(200,200))
                screen.blit(background_surface,(0,0))
                screen.blit(player_surface,(212,200))
                screen.blit(parachute_surface1,(200,78))    
                
                pygame.display.update()
    
    def terminal_response():
        ## responds in the terminal based on your guess showing if it was correct or not.
        print()
